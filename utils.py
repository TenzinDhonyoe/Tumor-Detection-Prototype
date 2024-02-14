import cv2
import numpy as np

def rectContours(contours):
    
    rectCon = []
    for i in contours:
        area = cv2.contourArea(i)
        #print("Area", area)
        if area > 15000:
            peri = cv2.arcLength(i, True)
            #approx polygon
            approx = cv2.approxPolyDP(i, 0.01*peri, True)
            #print(len(approx))
            if len(approx) == 4:
                rectCon.append(i)
    #print(rectCon)
    rectCon = sorted(rectCon, key=cv2.contourArea, reverse=True) #gives us in order of rect based on size
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    #approx polygon
    approx = cv2.approxPolyDP(cont, 0.01*peri, True)
    return approx

def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4,1,2), np.int32)
    add = myPoints.sum(1)
    
    myPointsNew[0] = myPoints[np.argmin(add)] # [0, 0]
    myPointsNew[3] = myPoints[np.argmax(add)] # [w, h]
    diff = np.diff(myPoints, axis = 1)
    myPointsNew[1] = myPoints[np.argmin(diff)] # This is our [width and 0]
    myPointsNew[2] = myPoints[np.argmax(diff)] # This is our [height and 0]
    
    return myPointsNew

def highlight(img, original):
    # Ensure the image is in grayscale
    if len(img.shape) > 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Apply a threshold where the black circle is black in the binary image
    _, img_thresh = cv2.threshold(img_blur, 130, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours on the thresholded image
    contours, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If there are contours found
    if contours:
        # Assuming the largest contour is the black circle (since we did not invert colors)
        largest_contour = max(contours, key=cv2.contourArea)

        # Fill the largest contour on the original image
        cv2.drawContours(original, [largest_contour], -1, (0, 255, 0), thickness=cv2.FILLED)
    
    return original 


