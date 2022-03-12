#Imports
import numpy as np
import cv2 as cv
import os

# Creating and checking the data directories
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")


mode = "train"
directory = "data/"+mode+"/"

cap=cv.VideoCapture(0)

while True:
    found,frame = cap.read()

    ##Simulating mirror image
    frame = cv.flip(frame, 1)

    # Getting count of existing images
    count={"zero" : len(os.listdir(directory+"/0")),
            "one" : len(os.listdir(directory+"/1")),
            "two" : len(os.listdir(directory+"/2")),
            "three" : len(os.listdir(directory+"/3")),
            "four" : len(os.listdir(directory+"/4")),
            "five" : len(os.listdir(directory+"/5"))}

    ## Printing the count calculated above on the screen 
    ##  cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    cv.putText(frame, "MODE : "+mode,(10,50),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "IMAGE COUNT : ",(10,100),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "ZERO : "+str(count["zero"]),(10,120),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "ONE : "+str(count["one"]),(10,140),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "TWO : "+str(count["two"]),(10,160),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "THREE : "+str(count["three"]),(10,180),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "FOUR : "+str(count["four"]),(10,200),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv.putText(frame, "FIVE : "+str(count["five"]),(10,220),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),1)

    # Co-ordinates for ROI(Region of Interest)
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5*frame.shape[1])

    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255, 0, 0), 1)

    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv.resize(roi, (64, 64))

    cv.imshow("Frame", frame)

    cv.imshow("ROI", roi)

    # the waitKey(1) refreshes the screen after 1ms
    interrupt = cv.waitKey(1)

    if interrupt & 0xFF == 27:
        break
    elif interrupt & 0xFF == ord('0'):
        cv.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    elif interrupt & 0xFF == ord('1'):
        cv.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    elif interrupt & 0xFF == ord('2'):
        cv.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    elif interrupt & 0xFF == ord('3'):
        cv.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    elif interrupt & 0xFF == ord('4'):
        cv.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    elif interrupt & 0xFF == ord('5'):
        cv.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)

cap.release()
cv.destroyAllWindows()