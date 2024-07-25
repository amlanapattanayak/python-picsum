#print("Hello World" + " " + "I am a Python Programmer")
from flask import (Flask, render_template, jsonify)
import requests
import random

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/randomimage')
def random_image():
    response = requests.get('https://picsum.photos/v2/list')
    image_list = response.json()

    # Get a random image from the list
    num = random.randint(0, 9)

    random_image = image_list[num]  # You can modify this to get a different random image

    # Construct the URL for the image
    image_url = random_image['download_url']

    # Return a JSON response with the image URL
    #return jsonify({'image_url': image_url})
    return render_template('picsum.html', image_url=image_url, num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)