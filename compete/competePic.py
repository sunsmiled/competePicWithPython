# from os import walk

# f = []
# for (dirpath, dirnames, filepath) in walk("D:/111test/picpic"):
#    f.extend(filepath)
#    print(f)
#    break

# import os
# for root, dirs, files in os.walk("D:/111test/picpic"):
#    for filename in files:
#       print (filepath)
#    for dirname in dirs:
#        print (dirs)


import os
import numpy as np
import cv2

from skimage.measure import compare_ssim
import argparse
import imutils


def VisitDir(path):
    f = []
    for root, dirs, files in os.walk(path):
        for filespath in files:
            # print(os.path.join(root, filespath))
            f.append(os.path.join(root, filespath))
            
    # print(f)

    return(f)
      

if __name__=="__main__":

# path="D:/111test/picpic"

    thefilepathlist = VisitDir("D:/0727com/0616_pic")
    print(thefilepathlist)
    print((thefilepathlist)[0])
    # img = cv2.imread((thefilepathlist)[0],0)
    # cv2.imshow("image",img)

    thenewfilepathlist = VisitDir("D:/0727com/0727_pic")
    print(thenewfilepathlist)
    print((thenewfilepathlist)[0])
    # img = cv2.imread((thefilepathlist)[0],0)
    # cv2.imshow("image",img)

    for i in range(0,153):
        print(i)
        print((thefilepathlist)[i])
        print((thenewfilepathlist)[i])

        imageA = cv2.imread((thefilepathlist)[i])
        imageB = cv2.imread((thenewfilepathlist)[i])

        grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)


        # compute the Structural Similarity Index(SSIM) between the teo images,
        # eusuring that the difference iamge is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM:{}".format(score))

        # threshold the difference image ,followed by inding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]


        # loop over the contours
        for c in cnts:
            # compute the bounding box of the countour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # show the ouput images
        # cv2.imshow("Original",imageA)
        # cv2.imshow("Modified",imageB)
        # cv2.imshow("Diff",diff)
        # cv2.imshow("Thresh",thresh)

        # path = "haha"+"i"+".png"
        # path = sub('haha{i}.png')
        path = ("haha%s.png" % i)
        print(path)
        # cv2.imwrite("haha1.png",imageA)
        cv2.imwrite(path, imageB)
        cv2.waitKey(0)
    else:
        print('for循环结束')

    


    
    

