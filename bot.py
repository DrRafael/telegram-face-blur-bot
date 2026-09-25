import os
import telebot
from config import TOKEN
from logic import process_image

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    """Sends onboarding instructions for face anonymization."""
    welcome_text = (
        "Hello! Send me any photo containing faces, "
        "and I will automatically detect and blur them to protect privacy."
    )
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    """Downloads user image, applies face blurring via OpenCV, and returns result."""
    input_file_path = f"input_{message.chat.id}.jpg"
    output_file_path = f"output_{message.chat.id}.jpg"

    try:
        status_msg = bot.reply_to(message, "Processing image, please wait...")

        # Download highest resolution photo version
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(input_file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Process image with Computer Vision
        process_image(input_file_path, output_file_path)

        # Send back anonymized photo
        with open(output_file_path, 'rb') as processed_photo:
            bot.send_photo(message.chat.id, processed_photo)

        bot.delete_message(message.chat.id, status_msg.message_id)

    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred while processing: {str(e)}")

    finally:
        # Guarantee cleanup of temporary local files
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
        if os.path.exists(output_file_path):
            os.remove(output_file_path)


if __name__ == "__main__":
    bot.polling(none_stop=True)
