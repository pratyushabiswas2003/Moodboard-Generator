from PIL import Image, ImageDraw, ImageFont
import os
import math

def create_moodboard(
        image_paths,
        palette,
        board_size=(1200,1200),
        grid_size = 3,
        output_path="output/moodboard.png",
        title_text="My Mood Board"
):
    
    print("Creating mood board layout...")
    board=Image.new("RGB", board_size, color=(245,245,245))
    draw= ImageDraw.Draw(board)

    margin=40
    spacing=20

    usable_width=board_size[0] - 2 * margin
    usable_height=board_size[1] - 2 * margin -80
    cell_size=min(
        (usable_width-spacing*(grid_size-1))//grid_size,
        (usable_height-spacing*(grid_size-1))//grid_size
    )
    x_start=margin
    y_start=margin+60

    idx=0
    for row in range(grid_size):
        for col in range(grid_size):
            if idx >= len(image_paths):
                break
            img=Image.open(image_paths[idx]).convert("RGB")
            img=img.resize((cell_size, cell_size))

            x=x_start+col*(cell_size+spacing)
            y=y_start+row*(cell_size+spacing)

            board.paste(img, (x,y))
            idx +=1

    try:
        font=ImageFont.truetype("assets/fonts/PlayfairDisplay-Regular.ttf",42)
    except:
        font=ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), title_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (board_size[0]-text_width)//2
    text_y=15

    draw.text((text_x, text_y), title_text, fill=(40,40,40), font=font)
    board.save(output_path)
    print(f"Mood board saved at {output_path}")