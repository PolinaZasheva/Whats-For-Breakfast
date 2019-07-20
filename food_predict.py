import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model_file = 'best_model_3class.hdf5'
print(model_file)
food_list = ['french toast','omelette','waffle']
# Load model to make predictions
K.clear_session()
model_best = load_model(model_file,compile = False)

# Function for making predictions using the given model
def predict_class(model, images, show = True):
  for img in images:
    image_name = img
    img = image.load_img(img, target_size=(299, 299))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img /= 255.                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    food_list.sort()
    pred_value = food_list[index]
    print(image_name + " " + pred_value + " " + str(pred[0,index]))
    if show:
        plt.imshow(img[0])                           
        plt.axis('off')
        plt.show()

# Initialize a list of images to classify using the model
images = []

# To use locally, images used for predicts are stored in img_folder
img_folder = './img_test/'
for img in os.listdir(img_folder):
    images.append(img_folder+img)

# Calls predict_class on images array
predict_class(model_best, images, False)

