import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# from ImageResize import resizer
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

model_file = 'best_model_3class.hdf5'
print(model_file)
food_list = ['french toast','omelette','waffle']

# Load model to make predictions
K.clear_session()
model_best = load_model(model_file,compile = False)

# Function for making predictions using the given model
def predict_class(model, img):
    img = image.load_img(img, target_size=(299, 299))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img /= 255.     

    preds = model.predict(img)
    return preds

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        if 'file' not in request.files:
            print('file not uploaded')
            return
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        image = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(image)

        # Make prediction
        preds = predict_class(model_best, image)

        index = np.argmax(preds)
        food_list.sort()
        pred_value = food_list[index]
        print(image + " " + pred_value + " " + str(preds[0,index]))

        breakfast_name = pred_value
        # image = resizer(images=image)
        # print(resizer(images=image))
        return render_template('result.html', breakfast=breakfast_name)

if __name__ == '__main__':
    # app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
