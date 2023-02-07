from flask import Flask, render_template, request
import numpy as np
import joblib



app = Flask(__name__)

model = joblib.load('random_forest_model.joblib')
labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image data from the request
        image_data = request.form['image_data']

        # Split the data into a list of pixels
        pixels = np.array([int(pixel) for pixel in image_data.split(',')])

        # Check that the input data is the correct length
        if len(pixels) != 784:
            return 'Error: Input data must contain 784 pixels (28x28), {} given'.format(len(pixels))

        # Reshape the array to match the model's expected input shape
        pixels = pixels.reshape(1, 784)

        # Use the model to predict the class of the image
        prediction = model.predict(pixels)

        # Get the class label with the highest probability
        class_label_index = prediction[0]
        class_label = labels[class_label_index]

        # Return the result to the user
        return str(class_label)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

