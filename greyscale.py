import cv2 as cv
import os
import sys
def greyscale(inputfile,outputfile):
    os.makedirs(outputfile,exist_ok=True)
    for filename in os.listdir(inputfile):
        img_path=os.path.join(inputfile,filename)
        img=cv.imread(img_path)
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        output_path=os.path.join(outputfile,filename)
        cv.imwrite(output_path,gray)
        print(f"Saved grayscale image to {output_path}")
        
if len(sys.argv)<3:
    print("Usage: python script_name.py <inputfile> <outputfile>")
    sys.exit(1)        
inputfile=sys.argv[1]
outputfile=sys.argv[2]
greyscale(inputfile,outputfile)
cv.destroyAllWindows()





    