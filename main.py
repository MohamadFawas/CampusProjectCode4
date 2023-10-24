import tensorflow as tf
import numpy as np
import cv2
import sys
import urllib.request

#print(sys.argv[1])
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="model (1).tflite")
interpreter.allocate_tensors()


# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


# Load test image
#req = urllib.request.urlopen("https://res.cloudinary.com/dnjzv3tpx/image/upload/v1690352776/notes/jmft1fmrn0xyrru6o5qv.jpg")
urllib.request.urlretrieve(sys.argv[1], "00000001.jpg")
#req = urllib.request.urlopen(sys.argv[1])
img = cv2.imread("00000001.jpg")
img = cv2.resize(img, (180,180))

##img = np.expand_dims(img, axis=0).astype(np.float32)
img = np.expand_dims(img, axis=0).astype(np.float32)

# Test the model on input data.
interpreter.set_tensor(input_details[0]['index'], img)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])



# Print predicted class
class_names = ['Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot', 'Corn(maize)__Common_rust',
               'Corn_(maize)__Northern_Leaf_Blight', 'Corn(maize)__healthy', 'Grape_Black_rot',
               'Grape_Esca(Black_Measles)', 'Grape_Leaf_blight(Isariopsis_Leaf_Spot)', 'Grape_healthy',
               'Potato_Early_blight', 'Potato_Late_blight', 'Potato_healthy', 'Strawberry_Leaf_scorch',
               'Strawberry_healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
               'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus',
               'Tomato_Tomato_mosaic_virus', 'Tomato__healthy']
predicted_class = class_names[np.argmax(output_data)]

#print(f"Predicted class: {predicted_class}")
# print(output_data)
print(f"{predicted_class}")


#print(class_names)
# print(np.argmax(output_data))