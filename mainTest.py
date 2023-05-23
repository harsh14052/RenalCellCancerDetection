import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model = load_model("KidneyTumor10Epochs.h5")

image = cv2.imread("E:\\KidneyTumorDetection\\Pred\\Normal- (5005).jpg")
# image = cv2.imread("E:\\KidneyTumorDetection\\Pred\\Tumor- (2249).jpg")

img = Image.fromarray(image)

img = img.resize((64, 64))

img = np.array(img)

input_img = np.expand_dims(img, axis=0)

result = (model.predict(input_img) > 0.5).astype("int32")
print(result)
