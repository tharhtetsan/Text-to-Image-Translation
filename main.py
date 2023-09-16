from flask import Flask
import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from rinna_modelWork import rinna_modelWork
from global_modelWork import global_modelWork

model_lists = ["Rinna","Global"]
result_path = "static/result_images"

rinna_model = rinna_modelWork()
global_model = global_modelWork()


app = Flask(__name__)


@app.route('/<filename>')
def display_image(filename):
    print('display_image filename: ' + str(filename))
    return redirect(url_for('static', filename='result_images/' + filename), code=301)


@app.route("/", methods=['POST'])
def submit():

   
    request_text = request.form['prompt_text'].lower().strip()
    request_model = request.form.get('selected_model').lower().strip()
    if request_model == "rinna":
        rinna_model.generate_imgs(request_text,num_imgs=1)
    else:
        global_model.generate_imgs(request_text,num_imgs=1)

    IMG_LIST = os.listdir(result_path)
    IMG_LIST = [result_path+'/' + i for i in IMG_LIST]
    return render_template("index.html", imagelist=IMG_LIST,model_list = model_lists)


@app.get("/")
def home():
    IMG_LIST = os.listdir(result_path)
    IMG_LIST = [result_path+'/' + i for i in IMG_LIST]
    return render_template("index.html", imagelist=IMG_LIST,model_list = model_lists)




@app.get("/delete")
def delete_img():
    IMG_LIST = os.listdir(result_path)
    IMG_LIST = [result_path+'/' + i for i in IMG_LIST]
    for cur_img in IMG_LIST:
        os.remove(cur_img)
    return render_template("index.html", imagelist=[],model_list = model_lists)




if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))




