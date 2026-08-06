execute unless entity @s[type=marker,tag=color_match_painting,tag=color_match_init] run return fail


data modify storage color_match:temp all.roll_color set from entity @s data

data modify storage color_match:temp all.random_palette.remaining set from entity @s data.palette
function color_match:build/random_palette_loop
data modify entity @s data.palette_map set from storage color_match:temp all.random_palette_out
data modify storage color_match:temp all.palette_map set from entity @s data.palette_map

function color_match:pixel/roll_color/main with entity @s

data remove storage color_match:temp all