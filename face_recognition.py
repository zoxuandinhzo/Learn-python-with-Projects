import cv2
from mtcnn import MTCNN
import os

file_run_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_run_dir, 'images', 'it_s_ok_2.png')

# read the image
img = cv2.imread(file_path)

# conver img to grayscale: 3D -> 2D
# gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# MTCNN: Load Face Recognition Detector
face_detector = MTCNN()

# use detector to find face landmarks
faces = face_detector.detect_faces(img)

for face in faces:
    x1 = face['box'][0]  # left Point
    y1 = face['box'][1]  # top Point
    x2 = x1 + face['box'][2]  # right Point
    y2 = y1 + face['box'][3]  # bottom Point

    # Draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)

    # Loop through all 5 keypoints
    for key, value in face['keypoints'].items():
        x = value[0]
        y = value[1]

        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=2, color=(0, 0, 255), thickness=1)

# show the image
cv2.imshow(winname="Face Recognition App", mat=img)

# wait for a key press to exit
cv2.waitKey(delay=0)

# Close All windows
cv2.destroyAllWindows()
