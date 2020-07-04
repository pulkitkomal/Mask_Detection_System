import cv2
import os
import shutil
import time
from config import PATH

def getFrame(sec, video_path, count, filename):
    vidcap = cv2.VideoCapture(video_path)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(PATH+"/static/{}/cache/time:_".format(filename)+str(count)+"_sec.jpg", image)     # save frame as JPG file
    return hasFrames

def extract_frames(video_path, filename):
    try:
        shutil.rmtree(PATH+'/static/'+filename+'/cache')
    except:
        pass
    os.mkdir(PATH+'/static/'+filename+'/cache')
    sec = 0
    frameRate = 1
    count = 1
    success = getFrame(sec, video_path, count, filename)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, video_path, count, filename)

def detect_wihout_mask(video,filename):
    print('start')
    from model import detect_mask
    model_service = detect_mask.init_()
    start_time = time.time()
    filename = filename.replace('.', "-").replace(' ', '-').replace('(','-').replace(')','-')

    try:
        os.mkdir('static')
    except:
        pass
    try:
        os.mkdir(PATH+'/static/'+filename)
    except:
        pass
    extract_frames(video, filename)
    print('Frames Extracted')
    try:
        shutil.rmtree(PATH+'/static/'+filename+'/output')
    except:
        pass
    os.mkdir(PATH+'/static/'+filename+'/output')
    list_dir = os.listdir(PATH+'/static/'+filename+'/cache')
    for image in list_dir:
        detect_mask.results(PATH + '/static/'+filename+'/cache/' + image, image, filename, model_service[0], model_service[1])
    shutil.rmtree(PATH+'/static/{}/zip_images'.format(filename))
    time_ = ((time.time() - start_time)/60)
    return "%.2f mins" % time_
