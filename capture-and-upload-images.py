import cv2
import dropbox
import time 
import random

startTime = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame= videoCaptureObject.read()
        imageName="img" + str(number) + ".png"
        cv2.imwrite(imageName,frame)
        startTime = time.time
        result = False
    return imageName
    print("Snapshot Taken.")
    videoCaptureObject.release()
    cv2.destroyallWindows()

def uploadFile(img_name):
    access_token = "VF9FHe56WkAAAAAAAAAAGsmjJnXpm-C1IqkUJMuhG9iU2MLcfOevWZYn_KWjVhta"
    file = img_name
    file_from = file
    file_to = "/newFolder1/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite) 
        print("Files Succesfully Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=3):
            name = take_snapshot()
            uploadFile(name)

main()