execute unless entity @s[type=marker,tag=color_match_painting,tag=color_match_init] run return fail


data modify storage color_match:temp all.roll_block set from entity @s data


data modify storage color_match:temp all.random_palette.remaining set from storage color_match:temp all.roll_block.palette
function color_match:random_palette/main_loop

data modify storage color_match:temp all.roll_block.palette_map set from storage color_match:temp all.random_palette_out

data modify entity @s data.palette_map set from storage color_match:temp all.random_palette_out

function color_match:pixel/roll_color/main with entity @s


data remove storage color_match:temp all