import cv2 as cv
import os
import sys
def rescaleFrame(inputfile,scale,outputfile):
    os.makedirs(outputfile,exist_ok=True)
    for filename in os.listdir(inputfile):
        img_path=os.path.join(inputfile,filename)
        img=cv.imread(img_path)
        width=int(img.shape[1]*scale/100)
        height=int(img.shape[0]*scale/100)
        dimensions=(width,height)
        resized_img=cv.resize(img,dimensions,interpolation=cv.INTER_AREA)
        output_path=os.path.join(outputfile,filename)
        cv.imwrite(output_path,resized_img)
        print(f"Rescaled image is at {output_path}")

if len(sys.argv)<4:
    print("Usage: python script_name.py <inputfile> <scale(in %)> <outputfile>")
    sys.exit(1)
inputfile=sys.argv[1]
scale=int(sys.argv[2])
outputfile=sys.argv[3]
rescaleFrame(inputfile,scale,outputfile)
cv.destroyAllWindows()