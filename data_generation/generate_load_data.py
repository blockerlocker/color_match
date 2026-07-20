import os
import json
import shutil
import colorsys
from PIL import Image
from pathlib import Path

def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    art_command = "data modify storage color_match:art_lookup all set value " + gen_art_lookup()
    block_command = "data modify storage color_match:block_lookup all set value " + gen_block_lookup()
    texture_command = "data modify storage color_match:texture_lookup all set value " + gen_texture_lookup()
    palette_command = "data modify storage color_match:palette_lookup all set value " + gen_palette_lookup()
    loaded_command = "data modify storage color_match:state all.lookups_loaded set value true"
    
    with open("../data/color_match/function/load/lookup_tables.mcfunction", "w") as file:
        file.write(art_command+"\n"+block_command+"\n"+texture_command+"\n"+palette_command+"\n"+loaded_command)



def gen_art_lookup():
    art_textures = os.listdir("raw_art")
    art_data = {"all":[]}

    for file_name in art_textures:
        if file_name.endswith(".png"):
            stripped_file_name = file_name[:-4]
            
            ### Process image
            raw_texture = Image.open('raw_art/' + file_name)
            rgb_texture = raw_texture.convert('RGBA')
            width, height = rgb_texture.size

            art_entry = {"name":stripped_file_name,"width":width,"height":height,"pixels":[],"palette":[]}


            for x in range(0, width):
                for y in range(0, height):
                    r, g, b, a = rgb_texture.getpixel((x,y))

                    color = "random"

                    if a != 255:
                        color = "none"
                    else:
                        if r==255 and g==0 and b==0:
                            color = "red"
                        if r==255 and g==128 and b==0:
                            color = "orange"
                        if r==255 and g==255 and b==0:
                            color = "yellow"
                        if r==0 and g==255 and b==0:
                            color = "green"
                        if r==0 and g==255 and b==255:
                            color = "aqua"
                        if r==0 and g==0 and b==255:
                            color = "blue"
                        if r==128 and g==0 and b==255:
                            color = "purple"
                        if r==255 and g==0 and b==255:
                            color = "magenta"
                        if r==255 and g==192 and b==255:
                            color = "pink"
                        if r==255 and g==255 and b==255:
                            color = "white"
                        if r==192 and g==192 and b==192:
                            color = "light_gray"
                        if r==64 and g==64 and b==64:
                            color = "dark_gray"
                        if r==0 and g==0 and b==0:
                            color = "black"
                        if r==128 and g==64 and b==0:
                            color = "brown"
                        if r==255 and g==192 and b==128:
                            color = "tan"

                    if not color in art_entry["palette"]:
                        art_entry["palette"].append(color)

                    art_entry["pixels"].append(color)
                    
            
            art_data["all"].append(art_entry)
    
    return str(art_data["all"])

def gen_block_lookup():
    block_lookup = {}

    ### Grab block lookup table json
    block_textures = os.listdir("whole_block_textures")
    with open("predicate_lookup.json", "r", encoding="utf-8") as json_file:
        predicate_lookup = json.load(json_file)

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
                
                
                ### Save Color Block Lookup
                if block_lookup.get(avg_argb_decimal) == None:
                    block_lookup[avg_argb_decimal] = {}
                block_lookup[avg_argb_decimal]["Name"] = predicate_lookup[stripped_file_name][0]["predicate"]["block"]["blocks"]
                if predicate_lookup[stripped_file_name][0]["predicate"]["block"].get("state"):
                    block_lookup[avg_argb_decimal]["Properties"] = predicate_lookup[stripped_file_name][0]["predicate"]["block"]["state"]

    return str(block_lookup)

def gen_texture_lookup():
    texture_lookup = {}

    ### Grab block lookup table json
    block_textures = os.listdir("whole_block_textures")

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
                
                
                ### Save Color Texture Lookup if doesn't exist
                if texture_lookup.get(avg_argb_decimal) == None:
                    texture_lookup[avg_argb_decimal] = {"sprite":"block/"+stripped_file_name}

    return str(texture_lookup)


def gen_palette_lookup():
    block_textures = os.listdir("whole_block_textures")
    palette = {"red":[],"orange":[],"yellow":[],"green":[],"aqua":[],"blue":[],"purple":[],"magenta":[],"pink":[],"white":[],"light_gray":[],"dark_gray":[],"black":[],"brown":[],"tan":[]}

    if Path("palette").is_dir():
        shutil.rmtree("palette")

    for file_name in block_textures:
        if file_name.endswith(".png"):
            stripped_file_name = file_name[:-4]
            
            total_red = 0
            total_blue = 0
            total_green = 0
            counted_pixels = 0

            # Process image
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

                # Save Average Color Lookup Table
                avg_red = round(total_red / (counted_pixels))
                avg_green = round(total_green / (counted_pixels))
                avg_blue = round(total_blue / (counted_pixels))
                
                avg_argb_decimal = avg_red * 65536 + avg_green * 256 + avg_blue - 16777216
                
                rgb_255 = (avg_red, avg_green, avg_blue)
                rgb_scaled = tuple(p / 255.0 for p in rgb_255)
                h_scaled, s_scaled, v_scaled = colorsys.rgb_to_hsv(*rgb_scaled)

                hue = round(h_scaled * 360)
                sat = round(s_scaled * 100)
                val = round(v_scaled * 100)
                
                in_palette = []

                if (hue <= 12 or hue >= 342) and sat >= 48 and val >= 25:
                    in_palette.append("red")

                if 13 <= hue <= 36 and sat >= 55 and val >= 55:
                    in_palette.append("orange")
                
                if 37 <= hue <= 66 and sat >= 15 and val >= 55:
                    in_palette.append("yellow")
                
                if 67 <= hue <= 155 and sat >= 15 and val >= 32:
                    in_palette.append("green")

                if 156 <= hue <= 185 and sat >= 32 and val >= 32:
                    in_palette.append("aqua")

                if 186 <= hue <= 253 and sat >= 16 and val >= 32:
                    in_palette.append("blue")

                if 254 <= hue <= 290 and 32 <= sat and 20 <= val <= 100:
                    in_palette.append("purple")

                if 291 <= hue <= 315 and sat >= 10 and val >= 48:
                    in_palette.append("magenta")

                if (316 <= hue <= 360 or hue <= 8) and 10 <= sat <= 60 and val >= 40:
                    in_palette.append("pink")
                
                if sat <= 16 and val >= 65:
                    in_palette.append("white")

                if sat <= 17 and 35 <= val <= 64:
                    in_palette.append("light_gray")
                
                if sat <= 40 and 0 <= val <= 45:
                    in_palette.append("dark_gray")
                
                if sat <= 64 and val <= 19:
                    in_palette.append("black")
                
                if 12 <= hue <= 48 and sat >= 30 and val <= 60:
                    in_palette.append("brown")
                
                if 13 <= hue <= 50 and 20 <= sat <= 52 and 47 <= val:
                    in_palette.append("tan")
            

                for color in in_palette:
                    palette[color].append({"color":avg_argb_decimal})
                    #palette_vis('whole_block_textures/' + file_name, "palette/" + str(color) + "_" + file_name)

    return str(palette)

def palette_vis(source,destination):
    Path("palette").mkdir(parents=True, exist_ok=True)
    shutil.copy(source,destination)

if __name__ == "__main__":
    main()