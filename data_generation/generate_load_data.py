import os
import json
import shutil
import colorsys
from PIL import Image
from pathlib import Path

abspath = os.path.abspath(__file__)
directory = os.path.dirname(abspath)
os.chdir(directory)

block_textures = os.listdir("whole_block_textures")
art_textures = os.listdir("raw_art")

def average_color(file_name):
    total_red = 0
    total_blue = 0
    total_green = 0
    counted_pixels = 0

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

        avg_red = round(total_red / (counted_pixels))
        avg_green = round(total_green / (counted_pixels))
        avg_blue = round(total_blue / (counted_pixels))

        return((avg_red,avg_green,avg_blue))
    else:
        return(None)

def decimal_color(r,g,b):
    return(r * 65536 + g * 256 + b - 16777216)

def hsv_color(r,g,b):
    rgb = (r,g,b)
    rgb_scaled = tuple(p / 255.0 for p in rgb)
    h_scaled, s_scaled, v_scaled = colorsys.rgb_to_hsv(*rgb_scaled)

    h = round(h_scaled * 360)
    s = round(s_scaled * 100)
    v = round(v_scaled * 100)
    return(h,s,v)

print("--Creating Block Map")

block_map = []

for file_name in block_textures:
    if file_name.endswith(".png"):
        stripped_file_name = file_name[:-4]

        average = average_color(file_name)

        if not average == None:
            decimal = decimal_color(*average)

            hsv = hsv_color(*average)

            hue = hsv[0]
            saturation = hsv[1]
            value = hsv[2]

            with open(f"../data/color_match/predicate/{stripped_file_name}.json") as json_file:
                block_predicate = json.load(json_file)

            block_states = []

            for block_state in block_predicate["terms"]:
                block_state_data = {"id":block_state["predicate"]["block"]["blocks"]}
                if block_state["predicate"]["block"].get("state"):
                    block_state_data["properties"] = block_state["predicate"]["block"]["state"]
                block_states.append(block_state_data)
            
            block_map.append({"texture":stripped_file_name,"decimal":decimal,"hue":hue,"saturation":saturation,"value":value,"block_states":block_states})

print("--Creating Art Map")

for file_name in art_textures:
    if file_name.endswith(".png"):
        raw_texture = Image.open("raw_art/" + file_name)
        rgb_texture = raw_texture.convert("RGBA")
        width, height = rgb_texture.size

        palette = []
        pixels = []
        palette_index = 0

        for x in range(0, width):
            for y in range(0, height):
                r, g, b, a = rgb_texture.getpixel((x,y))

                hsv = hsv_color(r,g,b)
                if a == 255:
                    pixel_color = hsv
                else:
                    pixel_color = "none"

                if not {"color":pixel_color} in palette:
                    palette.append({"color":pixel_color})
                    palette_index += 1

                pixels.append(palette.index({"color":pixel_color}))

        unclaimed_colors = []

        for h in range(0,360):
            for s in range(0,100):
                for v in range(0,100):
                    unclaimed_colors.append((h,s,v))
                    print((h,s,v))

        for color in palette:
            if color["color"] != "none":
                palette[palette.index(color)]["unscanned"] = [color["color"]]
                palette[palette.index(color)]["claimed"] = []
                
                if color["color"] in unclaimed_colors:
                    unclaimed_colors.remove(color["color"])
            
        while len(unclaimed_colors) > 0:
            print(len(unclaimed_colors))
            for color in palette:
                if color["color"] != "none":
                    for unscanned in color["unscanned"]:
                        new_claims = []
                        new_claims.append((unscanned[0] + 1, unscanned[1], unscanned[2]))
                        new_claims.append((unscanned[0], unscanned[1] + 1, unscanned[2]))
                        new_claims.append((unscanned[0], unscanned[1], unscanned[2] + 1))
                        new_claims.append((unscanned[0] - 1, unscanned[1], unscanned[2]))
                        new_claims.append((unscanned[0], unscanned[1] - 1, unscanned[2]))
                        new_claims.append((unscanned[0], unscanned[1], unscanned[2] - 1))

                        print(new_claims)

                        palette[palette.index(color)]["claimed"].append(unscanned)
                        palette[palette.index(color)]["unscanned"].remove(unscanned)

                        print(palette[palette.index(color)])

                        for new_claim in new_claims:
                            if new_claim in unclaimed_colors:
                                palette[palette.index(color)]["unscanned"].append(new_claim)
                                unclaimed_colors.remove(new_claim)
                                

                    
            
        print("\n\n\n"+str(palette))

print("--Writing data to lookup_tables.mcfunction")

block_map_command = f"data modify storage color_match:art_lookup all set value {block_map}"

with open("../data/color_match/function/load/lookup_tables.mcfunction", "w") as file:
    file.write(block_map_command)