from flask import Flask, request, send_file
import io
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return 'Hello World!'

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    print("Content-Type:", request.content_type)
    print("Incoming files:", request.files)
    print("Incoming form keys:", request.form)
    if "image" not in request.files:
        return {"error": "No image uploaded"}, 400

    image_file = request.files["image"]
    img = Image.open(image_file.stream)

    output = remove(img)

    img_io = io.BytesIO()
    output.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
