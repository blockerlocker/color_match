data modify entity @n[type=marker,tag=color_match_painting] data.palette_map set from storage color_match:clipboard all.palette_map
data modify storage color_match:temp all.palette_map set from storage color_match:clipboard all.palette_map

function color_match:pixel/refresh/main with entity @n[type=marker,tag=color_match_painting]

data remove storage color_match:temp all