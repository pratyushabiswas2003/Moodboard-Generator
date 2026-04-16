import os
import requests

UNSPLASH_ACCESS_KEY = "ENUQXz_tWPtY27BHUn6ympyR1rOvr1tI8KC8Koaf5lQ"


def fetch_images(theme, count=9, save_folder="output"):
    os.makedirs(save_folder, exist_ok=True)

    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": theme,
        "per_page": count,
        "orientation": "squarish",
        "client_id": UNSPLASH_ACCESS_KEY
    }

    print(f"\n🔍 Searching for images matching: {theme}...")

    response = requests.get(url, params=params)
    data = response.json()
    print(data)

    if "results" not in data or len(data["results"]) == 0:
        print("❌ No images found. Try another theme.")
        return []

    saved_files = []

    for i, img in enumerate(data["results"]):
        img_url = img["urls"]["regular"]
        img_data = requests.get(img_url).content
        file_path = os.path.join(save_folder, f"{theme}_{i+1}.jpg")

        with open(file_path, "wb") as f:
            f.write(img_data)

        saved_files.append(file_path)
        print(f"✔ Downloaded: {file_path}")

    print("\n🎉 All images downloaded successfully!\n")
    return saved_files
