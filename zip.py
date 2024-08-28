import cv2 as cv
import os
import sys
import zipfile

def zip_images(inputfile, outputfile):
    os.makedirs(outputfile, exist_ok=True)
    
    zip_filename = os.path.join(outputfile, 'images.zip')
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    
            for filename in os.listdir(inputfile):
                img_path = os.path.join(inputfile, filename)
                img = cv.imread(img_path)
            
                if img is not None:
                    temp_image_path = os.path.join(outputfile, filename)
                    cv.imwrite(temp_image_path, img)
                    zipf.write(temp_image_path, arcname=filename)
                
                    os.remove(temp_image_path)
                else:
                    print(f"Warning: Unable to read {img_path}.")

    print(f"All images have been zipped successfully into {zip_filename}.")

if len(sys.argv) < 3:
    print("Usage: python script_name.py <inputfile> <outputfile>")
    sys.exit(1)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

zip_images(inputfile, outputfile)
