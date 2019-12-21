import os
import urllib.request

from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(["png"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def upload_form():
    return render_template("upload.html")

@app.route("/", methods=["POST"])
def upload_file():
    if(request.method == "POST"):
        if("files[]" not in request.files):
            flash("No file part")
            return redirect(request.url)
        files = request.files.getlist("files[]")
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        flash("File successfully uploaded")
        return redirect("/")

if __name__ == "__main__":
    app.run()