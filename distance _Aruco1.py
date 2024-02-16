# import the OpenCV library for computer vision
import cv2
import math
# Load the dictionary that was used to generate the markers.
# There's different aruco marker dictionaries, this code uses 6x6
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# Initialize the detector parameters using default values
parameters = cv2.aruco.DetectorParameters_create()
l = 0.00
a = 0.00
b = 0.00
cx1 = 0
cx2 = 0
cy1 = 0
cy2 = 0
# initialize the webcam as "camera" object
camera = cv2.VideoCapture(0)

# loop that runs the program forever
# at least until the "q" key is pressed
while True:

    # creates an "img" var that takes in a camera frame
    _, img = camera.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect aruco tags within the frame
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

    # draw box around aruco marker within camera frame
    img = cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

    # if a tag is found...
    if markerIds is not None:
        # for every tag in the array of detected tags...
        for i in range(len(markerIds)):

            print(markerIds[0])
            if 1 in markerIds:
                cv2.putText(img, "Tag 1 Detected!", (25, 400), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)
            if 2 in markerIds:
                cv2.putText(img, "Tag 2 Detected!", (25, 425), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)
            if 1 in markerIds and 2 in markerIds:
                cv2.putText(img, "Tag 1 AND 2 Detected!", (25, 450), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)
            # get the center point of the tag
               
            center = markerCorners[i][0]
            M = cv2.moments(center)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draws a red dot on the marker center
            cv2.circle(img, (cX, cY), 1, (0, 0, 255), 8)
            # writes the coordinates of the center of the tag
            cv2.putText(img, str(cX) + "," + str(cY), (cX + 40, cY - 40), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
            (topLeft, topRight, bottomRight, bottomLeft) = markerCorners[i][0]
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            # draw the bounding box of the ArUCo detection
            cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)
            
            if(markerIds[i] == 0):
                print(cX, "  " ,cY, "   ", "ID 1")
                cx2 = cX
                cy2 = cY
            if(markerIds[i] == 1):
                print(cX, "  " ,cY, "   ", "ID 2") 
                cx1 = cX
                cy1 = cY      
            a = cx1 - cx2
            b = cy1 - cy2

            # cv2.line(img,(cx1,cy1),(cx2,cy2),(255,0,0),2)
            cv2.line(img,(cx1,cy1),(cx1,cy2) ,(0,255,255),2 )

            cv2.line(img,(cx2,cy2),(cx1,cy2) ,(0,255,255),2 )

            cv2.line(img,(cx1,cy1),(cx2,cy2) ,(0,255,255),2 )
            l = ((cx1-cx2)^2 + (cy1-cy2)^2)
            


            cv2.putText(img,str(cx1 - cx2) + "  "+ str(cy1 -cy2) + "   "  + str(l), ( 40, 40), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    (0, 0, 255), 2)
            

            print(a,"   ",b)
            # if(markerIds[i] == 0 and markerIds[i] == 1):
            #     center1 = markerCorners[i][0]
            #     M1 = cv2.moments(center)
            #     cX1 = int(M1["m10"] / M1["m00"])
            #     cY1 = int(M1["m01"] / M1["m00"])
            #     # draws a red dot on the marker center
            #     cv2.circle(img, (cX1, cY1), 1, (0, 0, 255), 8)
            #     # writes the coordinates of the center of the tag
            #     cv2.putText(img, str(cX1) + "," + str(cY1), (cX1 + 40, cY1 - 40), cv2.FONT_HERSHEY_COMPLEX, 0.7,
            #                 (0, 255, 0), 2)
            #     (topLeft, topRight, bottomRight, bottomLeft) = markerCorners[i][0]
            #     # convert each of the (x, y)-coordinate pairs to integers
            #     topRight = (int(topRight[0]), int(topRight[1]))
            #     bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            #     bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            #     topLeft = (int(topLeft[0]), int(topLeft[1]))

            #     # draw the bounding box of the ArUCo detection
            #     cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
            #     cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
            #     cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
            #     cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)

            #     center2 = markerCorners[i][0]
            #     M2 = cv2.moments(center)
            #     cX2 = int(M2["m10"] / M2["m00"])
            #     cY2 = int(M2["m01"] / M2["m00"])
            #     # draws a red dot on the marker center
            #     cv2.circle(img, (cX2, cY2), 1, (0, 0, 255), 8)
            #     # writes the coordinates of the center of the tag
            #     cv2.putText(img, str(cX2) + "," + str(cY2), (cX2 + 40, cY2 - 40), cv2.FONT_HERSHEY_COMPLEX, 0.7,
            #                 (0, 255, 0), 2)
            #     (topLeft, topRight, bottomRight, bottomLeft) = markerCorners[i][0]
            #     # convert each of the (x, y)-coordinate pairs to integers
            #     topRight = (int(topRight[0]), int(topRight[1]))
            #     bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            #     bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            #     topLeft = (int(topLeft[0]), int(topLeft[1]))

            #     # draw the bounding box of the ArUCo detection
            #     cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
            #     cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
            #     cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
            #     cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)

            


    # Display the resulting frame
    cv2.imshow('frame', img)

    # handler to press the "q" key to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
