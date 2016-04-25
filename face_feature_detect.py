#Credit to https://realpython.com/blog/python/face-recognition-with-python/
#Credit for XML files for feature recognition: https://github.com/peterbraden/node-opencv/blob/master/data/

import cv2
import sys
import numpy
# Get user supplied values

def normalMouth():
    imagePath = "./testimages/anthonynormal.jpg" #sys.argv[1]

    cascPath = "./cascade-files/haarcascade_mcs_mouth.xml"


    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=2.9,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # break
    crop_img = image[(y+2):(y-2+h-2),(x+2):(x-1+w-1)]

    imgYCC = cv2.cvtColor(crop_img, cv2.COLOR_BGR2YCR_CB)


    crop_img = cv2.GaussianBlur(crop_img,(5,5),0)
    canned = cv2.Canny(crop_img,50,100)

    # print "post ycc"
    # print imgYCC

    minPursed = 10000000000
    maxPursed = 0

    minNonPursed = 10000000000
    maxNonPursed = 0

    shape = canned.shape

    for x in range(shape[0]-2):
        for y in range(shape[1]-2):
            # print canned[x,y]
            if canned[x,y] ==255:
                if y< minNonPursed:
                    minNonPursed = y
                if y > maxNonPursed:
                    maxNonPursed = y

    print "max and min non pursed"
    print minNonPursed  # 0
    print maxNonPursed  # 120
            # if crop_img[x,y]
    differenceTopLipToBottom = maxNonPursed-minNonPursed

    cv2.imshow("Faces found", canned)

    cv2.imshow("faces found", image)
    cv2.waitKey(0)
    return differenceTopLipToBottom

########### begin for pursed

def pursedMouth():
    # Get user supplied values
    imagePath = "./testimages/PursedLips.jpg" #sys.argv[1]

    cascPath = "./cascade-files/haarcascade_mcs_mouth.xml"


    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5, #5.9 got the mouth
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    count = 0
    for (x, y, w, h) in faces:
        # count +=1
        # if count !=1:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break
    crop_img = image[(y+2):(y-2+h-2),(x+2):(x-1+w-1)]

    imgYCC = cv2.cvtColor(crop_img, cv2.COLOR_BGR2YCR_CB)


    crop_img = cv2.GaussianBlur(crop_img,(5,5),0)
    canned = cv2.Canny(crop_img,50,100)

    # print "post ycc"
    # print imgYCC

    minPursed = 10000000000
    maxPursed = 0

    minNonPursed = 10000000000
    maxNonPursed = 0

    shape = canned.shape

    for a in range(shape[0]-2):
        for b in range(shape[1]-2):
            # print canned[x,y]
            if canned[a,b] ==255:
                if b< minPursed:
                    minPursed = b
                if b > maxPursed:
                    maxPursed = b

    print "max and min non pursed"
    print minPursed  # 0
    print maxPursed  # 120
            # if crop_img[x,y]
    pursedDifferenceTopLipToBottom = maxPursed-minPursed

    cv2.imshow("Faces found", canned)

    cv2.imshow("faces found", crop_img)
    cv2.waitKey(0)


    ########### begin for pursed
    return pursedDifferenceTopLipToBottom

def getSquint():
    imagePath = "./testimages/squints.jpg" #sys.argv[1]

    cascPath = "./cascade-files/haarcascade_righteye_2splits.xml"


    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.007,
        minNeighbors=5,
        minSize=(10, 10),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break
    crop_img = image[(y+2):(y-2+h-2),(x+2):(x-1+w-1)]
    #
    imgYCC = cv2.cvtColor(crop_img, cv2.COLOR_BGR2YCR_CB)
    #
    #
    crop_img = cv2.GaussianBlur(crop_img,(5,5),0)
    canned = cv2.Canny(crop_img,50,100)
    #
    # # print "post ycc"
    # # print imgYCC
    #
    minPursed = 10000000000
    maxPursed = 0

    minNonPursed = 10000000000
    maxNonPursed = 0

    shape = canned.shape

    for x in range(shape[0]-2):
        for y in range(shape[1]-2):
            # print canned[x,y]
            if canned[x,y] ==255:
                if y< minNonPursed:
                    minNonPursed = y
                if y > maxNonPursed:
                    maxNonPursed = y
    #
    # print "max and min non pursed"
    # print minNonPursed  # 0
    # print maxNonPursed  # 120
    #         # if crop_img[x,y]
    differenceTopEye = maxNonPursed-minNonPursed

    cv2.imshow("Faces found", canned)
    cv2.waitKey(0)
    cv2.imshow("faces found", crop_img)
    cv2.waitKey(0)
    return differenceTopEye

def eye():
    imagePath = "./testimages/BarackObama.jpg" #sys.argv[1]

    cascPath = "./cascade-files/haarcascade_righteye_2splits.xml"


    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.007,
        minNeighbors=5,
        minSize=(10, 10),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break
    crop_img = image[(y+2):(y-2+h-2),(x+2):(x-1+w-1)]
    #
    imgYCC = cv2.cvtColor(crop_img, cv2.COLOR_BGR2YCR_CB)
    #
    #
    crop_img = cv2.GaussianBlur(crop_img,(5,5),0)
    canned = cv2.Canny(crop_img,50,100)
    #
    # # print "post ycc"
    # # print imgYCC
    #
    minPursed = 10000000000
    maxPursed = 0

    minNonPursed = 10000000000
    maxNonPursed = 0

    shape = canned.shape

    for x in range(shape[0]-2):
        for y in range(shape[1]-2):
            # print canned[x,y]
            if canned[x,y] ==255:
                if y< minNonPursed:
                    minNonPursed = y
                if y > maxNonPursed:
                    maxNonPursed = y
    #
    # print "max and min non pursed"
    # print minNonPursed  # 0
    # print maxNonPursed  # 120
    #         # if crop_img[x,y]
    differenceTopEye = maxNonPursed-minNonPursed

    cv2.imshow("Faces found", canned)
    cv2.waitKey(0)
    cv2.imshow("faces found", image)
    cv2.waitKey(0)

    return differenceTopEye

def hands():
    imagePath = "./testimages/fist.jpg" #sys.argv[1]

    cascPath = "./cascade-files/fist.xml"


    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #
    # Detect faces in the image
    #for hands, 1.007 and 20,20 worked. problem is it finds 4 hands in mouthclose up
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # break
    crop_img = image[(y+2):(y-2+h-2),(x+2):(x-1+w-1)]
    #
    imgYCC = cv2.cvtColor(crop_img, cv2.COLOR_BGR2YCR_CB)
    #
    #
    crop_img = cv2.GaussianBlur(crop_img,(5,5),0)
    canned = cv2.Canny(crop_img,50,100)
    #
    # # print "post ycc"
    # # print imgYCC
    #
    minPursed = 10000000000
    maxPursed = 0

    minNonPursed = 10000000000
    maxNonPursed = 0

    shape = canned.shape

    for x in range(shape[0]-2):
        for y in range(shape[1]-2):
            # print canned[x,y]
            if canned[x,y] ==255:
                if y< minNonPursed:
                    minNonPursed = y
                if y > maxNonPursed:
                    maxNonPursed = y
    #
    # print "max and min non pursed"
    # print minNonPursed  # 0
    # print maxNonPursed  # 120
    #         # if crop_img[x,y]
    differenceTopEye = maxNonPursed-minNonPursed

    # cv2.imshow("Faces found", canned)
    # #
    cv2.imshow("faces found", image)
    cv2.waitKey(0)

    return differenceTopEye

#######begin lips  ********************
differenceTopLipToBottom = normalMouth()
pursedDifferenceTopLipToBottom = pursedMouth()
pursedRatio = float(differenceTopLipToBottom)/float(pursedDifferenceTopLipToBottom)
print pursedRatio

if pursedRatio > 1.2:
    print "probable discomfort"

######begin eyes ********************
squintDiff=getSquint()
eyeDiff =eye()

squintRatio = float(eyeDiff)/float(squintDiff)
print "squint ratio is "
print squintRatio
if squintRatio > 1.1:
    print "probable dislike"


#######begin hands  ********************
# hands()
