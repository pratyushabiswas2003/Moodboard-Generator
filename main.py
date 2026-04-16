from fetch_images import fetch_images
from palette import extract_palette
from layout import create_moodboard

def main():
    print("\n Welcome to the Mood Board Generator!\n")
    theme = input("Enter a theme(e.g. 'Japan aesthetic', 'F1 vibes', 'healing era'): ")
    image_paths=fetch_images(theme, count=9)
    if not image_paths:
        print("No images fetched. Exiting program.")
        return
    palette= extract_palette(image_paths, num_colors=5)
    title=theme.title()

    create_moodboard(
        image_paths=image_paths,
        palette=palette,
        title_text=title,
        output_path="output/moodboard.png"
    )
    print("\n Mood board generation complete")
if __name__ == "__main__":
    main()