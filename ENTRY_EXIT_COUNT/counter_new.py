import cv2

# capturing video
capture = cv2.VideoCapture("/Users/sarthakumarani/Documents/Mask and Face Detection/people-capture.mp4")
xvalues = []
while capture.isOpened():
    # to read frame by frame
    _, img_1 = capture.read()
    _, img_2 = capture.read()

    # find difference between two frames
    diff = cv2.absdiff(img_1, img_2)

    # to convert the frame to grayscale
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # apply some blur to smoothen the frame
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)

    # to get the binary image
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    # to find contours
    contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # to draw the bounding box when the motion is detected
    for c in contours:
        if cv2.contourArea(c) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        xvalues.append(x)
        cv2.rectangle(img_1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        flag = False
    # cv2.drawContours(img_1, contours, -1, (0, 255, 0), 2)

    # display the output
    cv2.imshow("Detecting Motion...", img_1)
    if cv2.waitKey(100) == 13:
        exit()