import cv2

# Setting up a function to resize
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame, dimensions, cv2.INTER_AREA)

# Reading images from saved videos 

capture = cv2.VideoCapture("Videos\pexels-ivan-samkov-6448145.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv2.imshow("Video", frame)
    cv2.imshow("Video Rescaled", frame_resized)


    if cv2.waitKey(20) &  0xFF == ord("d"):
        break

capture.release()
cv2.destroyAllWindows()