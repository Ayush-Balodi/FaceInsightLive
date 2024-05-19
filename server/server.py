# from flask import Flask, requet, jsonify
# import util

# @app.route("/classfiy_image", methods=['GET','POST'])
# def classify_image():
#     image_data = request.form['image_data']

#     jsonify(util.classfiy_image(image_data))
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# if __name__ == "__main__":
#     print("Staring the server.....")
#     util.load_save_artifacts()
#     return app.run(debug=True)

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/detect', methods=['GET'])
def detect():
    # Run the detect.py script in a new process
    subprocess.Popen(['python', 'detect.py'])
    return 'Detection started. Please check the screen for the video feed.'

if __name__ == '__main__':
    app.run(debug=True)
