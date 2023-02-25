import cv2
#reading image
# img = cv2.imread("Photos\dp.jpg")

# cv2.imshow("My DP", img)

# cv2.waitKey(0)

# reading image from webcam

# capture = cv2.VideoCapture(0)

# Reading images from saved videos 

capture = cv2.VideoCapture("Videos\pexels-ivan-samkov-6448145.mp4")

while True:
    isTrue, frame = capture.read()
    cv2.imshow("Video", frame)


    if cv2.waitKey(20) &  0xFF == ord("d"):
        break

capture.release()
cv2.destroyAllWindows()