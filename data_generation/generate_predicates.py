import os
import json
from PIL import Image
from pathlib import Path

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


### Grab predicate lookup table
block_textures = os.listdir("whole_block_textures")
with open("predicate_lookup.json", "r", encoding="utf-8") as json_file:
    predicate_lookup = json.load(json_file)


### Clear predicate folder
color_predicate_folder = "../data/color_match/predicate/color"
for file in os.scandir(color_predicate_folder):
    filePath = color_predicate_folder + "/" + file.name
    os.remove(filePath)

for file_name in block_textures:
    if file_name.endswith(".png"):
        stripped_file_name = file_name[:-4]
        
        total_red = 0
        total_blue = 0
        total_green = 0
        counted_pixels = 0


        ### Process image
        raw_texture = Image.open('whole_block_textures/' + file_name)
        rgb_texture = raw_texture.convert('RGBA')
        width, height = rgb_texture.size

        for x in range(0, width):
            for y in range(0, height):
                r, g, b, a = rgb_texture.getpixel((x,y))

                if a == 255:
                    total_red += r
                    total_green += g
                    total_blue += b
                    counted_pixels += 1
        
        if counted_pixels == width * height:


            ### Determine Average Color
            avg_red = round(total_red / (counted_pixels))
            avg_green = round(total_green / (counted_pixels))
            avg_blue = round(total_blue / (counted_pixels))
            
            avg_argb_decimal = avg_red * 65536 + avg_green * 256 + avg_blue - 16777216
            
            
            ### Save Predicate
            predicate_file_path_string = "../data/color_match/predicate/color/" + str(avg_argb_decimal) + ".json"
            predicate_file_path = Path(predicate_file_path_string)

            if not predicate_file_path.is_file():
                with open(predicate_file_path_string, "w") as json_file:
                    json.dump({ "type": "minecraft:any_of", "terms": [] }, json_file)

            with open(predicate_file_path_string, "r") as json_file:
                updated_predicate = json.load(json_file)
                for term in predicate_lookup[stripped_file_name]:
                    updated_predicate["terms"].append(term)
                
                with open(predicate_file_path_string, "w") as json_file:
                    json.dump(updated_predicate, json_file)