import cv2
import numpy as np
import utils
import time

width = 700
height = 700

cap = cv2.VideoCapture(0)
pTime = 0

while True:
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    success, img = cap.read()
    
    #preprocess the video
    img = cv2.resize(img, (width, height))
    imgContours = img.copy()
    imgLine = img.copy()
    finalImage = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 10, 50)
    
    #FIND all Contours
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)
    #Find rectangle box
    rectCon = utils.rectContours(contours)
    if len(rectCon) > 0:
        biggestContour = utils.getCornerPoints(rectCon[0])
        print(biggestContour.shape)
        if biggestContour.size != 0:
            cv2.drawContours(imgLine, biggestContour, -1, (0,255,0), 20)
            biggestContour = utils.reorder(biggestContour)
            
            pt1 = np.float32(biggestContour)
            pt2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
            matrix = cv2.getPerspectiveTransform(pt1,pt2)
            imgWarpColored = cv2.warpPerspective(img, matrix, (width, height))
        
            #APPLY TRESHOLD
            imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
            img_blur = cv2.GaussianBlur(imgWarpGray, (5, 5), 0)
            imgThresh = cv2.threshold(imgWarpGray, 130, 255, cv2.THRESH_BINARY)[1]
            
            #FIND A WAY TO Highlight the part with the darkest area
            imgHighlight = utils.highlight(imgThresh, imgWarpColored)
            #best_threshold, largest_contour, best_img = utils.find_best_threshold(imgWarpGray)

            cv2.putText(imgHighlight, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
            cv2.imshow("Video", imgHighlight)
            key = cv2.waitKey(1)
            if key == 27:  # Press 'ESC' to exit
                break
            
    else:
        print("No contours found")
        
    cv2.putText(imgLine, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow("Image", imgLine)
    key = cv2.waitKey(1)
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()

