import cv2
import time
import random
import dropbox

starttime=time.time()
def snap():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):

        ret,frame =videoCaptureObject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False

    return imagename
    print("snapshot taken")


    videoCaptureObject.release()
    cv2.destroyAllWindows()


snap()