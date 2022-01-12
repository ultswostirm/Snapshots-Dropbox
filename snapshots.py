import cv2
import time
import random
import dropbox

StartTime=time.time()

def snapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    
    while result:
        ret, frame=VideoCaptureObject.read()
        imgName="Snapshot"+str(number)+".png"
        cv2.imwrite(imgName,frame)
        StartTime=time.time()
        result=False
        
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
    print("Snapshots have been saved")
    return imgName

def uploadFile(imgName):
    access_token = 'sl.A_4NCSh6xHo2Mzte3eP8YIpE0CE7FIQWJEEh3kfh5__tTgf1dfAiI_-f57cB6V9ajuapVv4GkfsxAy-U2nX9EV3o1Kh6Hev3xMBgFQmGVvAuHUIKbqIoEE_-Zywfw3OVurrsmUY'


    file_from = imgName
    file_to = "/demondbx/"+(imgName)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
            
    # API v2
            print("The file has been backed up succesfully")

def main():
    while(True):
        if((time.time()-StartTime)>=5 ):
            name=snapshot()
            uploadFile(name)
            
main()
    