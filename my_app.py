from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load_model('fashion_mnist_model.h5')
labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image data from the request
        image_data = request.form['image_data']

        # Split the data into a list of pixels
        pixels = image_data.split(',')

        # Check that the input data is the correct length
        if len(pixels) != 784:
            return 'Error: Input data must contain 784 pixels (28x28), {} given'.format(len(pixels))

        # Convert the list of pixels to a numpy array
        pixels = np.array(pixels, dtype=np.float32)

        # Reshape the array to match the model's expected input shape
        image = pixels.reshape(1, 28, 28, 1)

        # Use the model to predict the class of the image
        prediction = model.predict(image)

        # Get the class label with the highest probability
        class_label_index = np.argmax(prediction)
        class_label = labels[class_label_index]

        # Return the result to the user
        return str(class_label)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
