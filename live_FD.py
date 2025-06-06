import cv2 as cv

video_capture = cv.VideoCapture(0)
while True:
    ret,video = video_capture.read()
    grey = cv.cvtColor(video,cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haarcascade.xml')

    face_rect = haar_cascade.detectMultiScale(grey,1.1,3)
    for (x, y, w, h) in face_rect:
        cv.rectangle(video,(x,y),(x+w,y+h),(0,255,0),thickness=2)

    cv.imshow('live_video', video)
    #     now we need to end the video also otherwise it will never end and the computer will crash
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.waitKey(0)