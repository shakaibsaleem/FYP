import imutils
import cv2
import sys
import numpy as np
cascPath = "haarcascade_fullbody.xml"
bodyCascade = cv2.CascadeClassifier(cascPath)

filename = "behenji.jpg"
img = cv2.imread(filename,0)
frame=imutils.resize(img, width=min(500, img.shape[1]))
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
upper=bodyCascade.detectMultiScale(frame,1.4,1)
##faces = bodyCascade.detectMultiScale(
##    img,
##    scaleFactor=1.1,
##    minNeighbors=5,
##    flags=cv2.CASCADE_SCALE_IMAGE
##)

for (a,b,c,d) in upper:
    cv2.rectangle(frame,(a,b),(a+c,b+d),(0,0,255),2)
#print len(upper)
cv2.imshow('detect',frame)

'''to view a image'''
##cv2.imshow('Behenji',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

# faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )

# # Draw a rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# # Display the resulting frame
# cv2.imshow('Video', frame)

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# # When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()
