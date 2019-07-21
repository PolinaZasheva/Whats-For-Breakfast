from food_predict import predict_class
from food_predict import model_best
# from ImageResize import resizer
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('file not uploaded')
            return
        file = request.files['file']
        images = []
        images.append(file.read())
        breakfast_name = 'incomplete'
        # breakfast_name = predict_class(model_best, images=image)
        # image = resizer(images=image)
        # predict_class(model_best, images=image)
        # print(resizer(images=image))
        return render_template('result.html', breakfast=breakfast_name)

if __name__ == '__main__':
    app.run(debug=True)
