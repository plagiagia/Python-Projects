# Imports
import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("./cascades/haarcascade_eye.xml")


# Function for face detection
def detect_face_eyes(original_image, gray_image):
    faces: tuple = face_cascade.detectMultiScale(image=gray_image, scaleFactor=1.3, minNeighbors=6)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(img=original_image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)
        # Center the image around the face
        centered_gray = gray_image[y:y + h, x:x + w]
        centered_original = original_image[y:y + h, x:x + w]
        eyes: tuple = eye_cascade.detectMultiScale(image=centered_gray, scaleFactor=1.1, minNeighbors=6)
        for eye in eyes:
            eye_x, eye_y, eye_w, eye_h = eye
            cv2.rectangle(img=centered_original, pt1=(eye_x, eye_y), pt2=(eye_x + eye_w, eye_y + eye_h),
                          color=(0, 0, 255), thickness=5)
    return original_image


# Capture video
video = cv2.VideoCapture(0)  # 0 for internal camera, 1 for external device
while True:
    # Capture the last incoming frame from camera
    _, frame = video.read()
    # Turn the frame into grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_faces = detect_face_eyes(frame, gray_frame)
    cv2.imshow('Video', detect_faces)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Terminate the video capturing
video.release()
cv2.destroyWindow('Video')
