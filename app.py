import os
from flask import Flask, render_template, request, redirect
from downloader import download

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        link = request.form["link"]
        print(link)
        download(link)
        return redirect("/")
    return render_template("index.html")


@app.route("/viewer/")
def viewer():
    vids = []
    for x in os.listdir("./static/vids"):
        if x.endswith(".mp4"):
            vids.append("/vids/" + x)
    print(vids)
    return render_template("viewer.html", videos=vids)


app.run(host="127.0.0.1", port=8000, debug=True)
