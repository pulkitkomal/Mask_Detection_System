from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from config import PATH
import os
import shutil
import time

def detect_and_predict_mask(frame, faceNet, maskNet):
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
		(104.0, 177.0, 123.0))
	faceNet.setInput(blob)
	detections = faceNet.forward()
	faces = []
	locs = []
	preds = []

	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		if confidence > 0.5:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			face = np.expand_dims(face, axis=0)
			faces.append(face)
			locs.append((startX, startY, endX, endY))
	if len(faces) > 0:
		preds = maskNet.predict(faces)
	return (locs, preds)

def init_():
	prototxtPath = PATH + '/model_services/deploy.prototxt'
	weightsPath = PATH + '/model_services/res10_300x300_ssd_iter_140000.caffemodel'
	net = cv2.dnn.readNet(prototxtPath, weightsPath)
	model = load_model(PATH + '/model_services/mask_detector.model')
	return (net,model)


def results(image, file_name, filename, net, model):
	image = cv2.imread(image)
	image = cv2.resize(image, (160,120), interpolation=cv2.INTER_AREA)
	(locs, preds) = detect_and_predict_mask(image, net, model)
	for (box, pred) in zip(locs, preds):
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred
		label = "Mask" if mask > withoutMask else "No Mask"
		temp_var = label
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
		cv2.putText(image, label, (startX, startY - 10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
		temp_list = []
		try:
			os.mkdir(PATH+'/static/{}/zip_images'.format(filename))
		except:
			pass
		if temp_var == 'No Mask':
			cv2.imwrite(PATH+'/static/{}/output/{}'.format(filename,file_name), image)
			temp_list.append(file_name)
			print(file_name)
		else:
			print('Mask_Detected')
		for x in temp_list:
			shutil.copyfile(PATH+'/static/{}/cache/{}'.format(filename, x),
							PATH+'/static/{}/zip_images/{}'.format(filename, x))
		try:
			os.mkdir(PATH+'/static/zips'.format(filename))
		except:
			pass
		shutil.make_archive(PATH+'/static/zips/{}'.format(filename), 'zip', PATH+'/static/{}/zip_images'.format(filename))

