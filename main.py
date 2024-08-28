import os

os.system("python download.py bike 20 outputfolder1")
os.system("python greyscale.py outputfolder1 outputfolder2")
os.system("python rescale.py outputfolder2 25 outputfolder3")
os.system("python zip.py outputfolder3 outputfolder3.zip")
os.system("python sendToEmail.py outputfolder3.zip bansallovely179@gmail.com")