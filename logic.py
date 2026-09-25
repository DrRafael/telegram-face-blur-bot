import cv2


def process_image(input_path: str, output_path: str) -> bool:
    """Detects faces in an image using OpenCV Haar Cascades and applies Gaussian Blur for privacy protection."""
    # Load pre-trained Haar Cascade face detector classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    image = cv2.imread(input_path)
    if image is None:
        raise ValueError(f"Failed to load image from path: {input_path}")

    # Convert to grayscale for optimal face detection performance
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Apply Gaussian blur to each detected face region
    for (x, y, w, h) in faces:
        face_region = image[y:y + h, x:x + w]
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
        image[y:y + h, x:x + w] = blurred_face

    # Save processed image to disk
    cv2.imwrite(output_path, image)
    return True
