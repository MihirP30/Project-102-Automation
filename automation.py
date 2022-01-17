import cv2
import random
import dropbox

def take_snapshot():
    image_number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(image_number) + ".png"
        cv2.imwrite(img_name, frame)
        result = False
    
    print("Snapshot taken.")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name

def upload_file(img_name):
    access_token = "sl.BASaRtRM7BUasAN2G1brDJKKgX9cc1K0l5nkQ2vSCFzmeycuazpz6PYoYokuYXz1f2yIMPa4sXxR2h43F4iYxjFOH_-Esg8NcI-qRgtPQTnfDNXi5i7bctzSz6oteTDEctiDCVc"
    file = img_name
    file_from = file
    file_to = "/P-102-Automation/" + file
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded.")

def main():
    while(True):
        name = take_snapshot()
        upload_file(name)


take_snapshot()