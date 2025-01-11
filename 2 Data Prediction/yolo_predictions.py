import cv2
import numpy as np
import os
import yaml
from yaml.loader import SafeLoader

class YOLO_Predictions():
    def __init__(self, onnx_model, data_yaml):
        
        # load yaml
        with open(data_yaml, mode='r') as f:
            data_yaml = yaml.load(f, Loader=SafeLoader)
        self.labels = data_yaml['names']
        self.nc     = data_yaml['nc']
        
        #load YOLO Model
        self.yolo = cv2.dnn.readNetFromONNX('Model/weights/best.onnx')
        self.yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        
    def generate_colors(self, ID):
        np.random.seed(10)
        colors = np.random.randint(100, 255, size=(self.nc, 3)).tolist()
        return tuple(colors[ID])
    
    def prediction(self,image):
        row, col, d = image.shape
        
        #create blank square black matrix
        max_rc = max(row, col) 
        input_image = np.zeros((max_rc, max_rc, 3), dtype=np.uint8) 
        input_image[0:row, 0:col] = image #overlay image
        
        # get YOLO predictions
        
        # returns a 4-dimensional NumPy array ("blob") 
        # represents the preprocessed input image for passing to a dnn model 
        INPUT_WH = 640
        blob = cv2.dnn.blobFromImage(input_image, 1/255, (INPUT_WH, INPUT_WH), swapRB=True, crop=False)
        self.yolo.setInput(blob)
        preds = self.yolo.forward() # get predictions
        
        # remove duplicates of 25200
        
        # 1. filter detections based on confidence(0.4) and probablity score(0.25)
        detections = preds[0]
        boxes = []
        confidences = []
        classes = []
        
        image_w, image_h = input_image.shape[:2]
        
        # since square, both r same
        x_factor = image_w / INPUT_WH
        y_factor = image_h / INPUT_WH
        
        # 2. column names: center_x, center_y, w, h, confidence, prob-scores of classes
        for i in range(len(detections)):
            row = detections[i]
            confidence = row[4] #4th columnn of ith row
            
            if confidence > 0.1:
                class_score = row[5:].max() # maximum probability of class detected
                class_id = row[5:].argmax() # index at which max prob occurs
        
                if class_score > 0.25:
                    cx, cy, w, h = row[0:4]
        
                    #construct bound box from these values
                    left = int((cx - 0.5*w) * x_factor)
                    top  = int((cy - 0.5*h) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)
                    box = np.array([left, top, width, height])
        
                    confidences.append(confidence)
                    boxes.append(box)
                    classes.append(class_id)
        
        # 3. clean
        boxes_np = np.array(boxes).tolist()
        confidences_np = np.array(confidences).tolist()
        
        # 4. Non Maximum Suppression
        index = cv2.dnn.NMSBoxes(boxes_np, confidences_np, 0.1, 0.3)
        index.flatten()
        
        
        # extracy bounding box info
        for ind in index:
            x, y, w, h = boxes_np[ind]
            bb_conf = int(confidences_np[ind]*100)
            class_id = classes[ind]
            class_name = self.labels[class_id]
            colors = self.generate_colors(class_id)
        
            text = f'{class_name}: {bb_conf}%'
            
            cv2.rectangle(image, (x,y), (x+w, y+h), colors, 2)
            cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_PLAIN, 0.7, colors, 1)
    
        return image



        
            