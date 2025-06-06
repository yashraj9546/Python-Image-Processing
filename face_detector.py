# in this face recognizor is build using haar_cascade which is an xml  file found in
# github repository of opencv.
import cv2 as cv

img = cv.imread('images/faces.jpg')
cv.imshow('image',img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grey',grey)

haar_cascade = cv.CascadeClassifier('haarcascade.xml')

face_rect = haar_cascade.detectMultiScale(grey,1.1,3)

print(f'number of faces found are: {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected faces',img)
cv.waitKey(0)