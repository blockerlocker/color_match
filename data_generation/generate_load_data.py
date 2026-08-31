import os, json, colorsys, math
from PIL import Image

abspath = os.path.abspath(__file__)
directory = os.path.dirname(abspath)
os.chdir(directory)

block_textures = os.listdir("whole_block_textures")
art_textures = os.listdir("raw_art")

DEBUG = True

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


print("--Creating Block Lookup")

block_lookup = []

for file_name in block_textures:
    if file_name.endswith(".png"):
        stripped_file_name = file_name[:-4]

        average = average_color(file_name)

        if not average == None:
            decimal = decimal_color(*average)

            with open(f"../data/color_match/predicate/{stripped_file_name}.json") as json_file:
                block_predicate = json.load(json_file)

            block_states = []

            for block_state in block_predicate["terms"]:
                block_state_data = {"id":block_state["predicate"]["block"]["blocks"]}
                if block_state["predicate"]["block"].get("state"):
                    block_state_data["properties"] = block_state["predicate"]["block"]["state"]
                block_states.append(block_state_data)
            
            block_lookup.append({"texture":stripped_file_name,"decimal":decimal,"rgb":average,"block_states":block_states})

print("--Creating Art Lookup")
art_data = []
art_lookup = []
for file_name in art_textures:
    if file_name.endswith(".png"):
        stripped_file_name = file_name[:-4]

        raw_texture = Image.open("raw_art/" + file_name)
        rgb_texture = raw_texture.convert("RGBA")
        width, height = rgb_texture.size

        palette = []
        pixels = []
        palette_index = 0

        for x in range(0, width):
            for y in range(0, height):
                r, g, b, a = rgb_texture.getpixel((x,y))

                rgb = (r,g,b)
                if a == 255:
                    texel = {"color":decimal_color(*rgb),"rgb":rgb}
                else:
                    texel = {"color":"none","rgb":"none"}

                if not texel in palette:
                    if texel == "none":
                        palette.append(texel)
                    else:
                        palette.append(texel)
                    palette_index += 1

                pixels.append(palette.index(texel))

        unclaimed_colors = []

        for block in block_lookup:
            unclaimed_colors.append(block)

        for color in palette:
            if color["rgb"] != "none":
                palette[palette.index(color)]["blocks"] = []

        def weighted_hsv_distance(a,b,weights):
            hsv_a = hsv_color(*a)
            hsv_b = hsv_color(*b)
            
            a_weighted = (hsv_a[0] * weights[0], hsv_a[1] * weights[1], hsv_a[2] * weights[2])
            b_weighted = (hsv_b[0] * weights[0], hsv_b[1] * weights[1], hsv_b[2] * weights[2])
            
            return min(math.dist(a_weighted,b_weighted),math.dist(a_weighted,tuple(x - y for x, y in zip(hsv_b, (255 * weights[0], 0, 0)))),math.dist(a_weighted,tuple(x + y for x, y in zip(hsv_b, (255 * weights[0], 0, 0)))))

        def hsv_distance(a,b):
            hsv_a = hsv_color(*a)
            hsv_b = hsv_color(*b)

            return min(math.dist(hsv_a,hsv_b),math.dist(hsv_a,tuple(x - y for x, y in zip(hsv_b, (255, 0, 0)))),math.dist(hsv_a,tuple(x + y for x, y in zip(hsv_b, (255, 0, 0)))))

        for color in palette:
            if color["color"] != "none":
                for unclaimed in unclaimed_colors:
                    if weighted_hsv_distance(color["rgb"],unclaimed["rgb"],(2,1,3)) < 100:
                        color["blocks"].append(unclaimed["texture"])

                color.pop("rgb",None)

        art_data.append({"name":stripped_file_name,"pixels":pixels,"palette":palette,"width":width,"height":height})
        art_lookup.append(stripped_file_name)

if DEBUG == True:
    for art in art_data:
        print(f"----{art["name"]}: Lowest assignment {min(len(color["blocks"]) for color in art["palette"])}, highest assignment {max(len(color["blocks"]) for color in art["palette"])}")

for block in block_lookup:
    block.pop("rgb",None)

print("--Writing data to lookup_tables.mcfunction")
block_lookup_command = f"data modify storage color_match:block_lookup all set value {block_lookup}"
art_lookup_command = f"data modify storage color_match:art_lookup all set value {art_lookup}"
art_data_command = f"data modify storage color_match:art_data all set value {art_data}"

with open("../data/color_match/function/load/lookup_tables.mcfunction", "w") as file:
    file.write(f"{block_lookup_command}\n{art_data_command}\n{art_lookup_command}")