import sys
sys.path.append("..")

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

from fetch_images import fetch_images
from palette import extract_palette
from layout import create_moodboard

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    theme = data.get("theme")

    if not theme:
        return jsonify({"error": "Theme is required"}), 400

    image_paths = fetch_images(theme, count=9)

    if not image_paths:
        return jsonify({"error": "No images found"}), 404

    palette = extract_palette(image_paths, num_colors=5)

    output_path = "../output/moodboard.png"

    create_moodboard(
        image_paths=image_paths,
        palette=palette,
        title_text=theme.title(),
        output_path=output_path
    )

    return send_file(output_path, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
