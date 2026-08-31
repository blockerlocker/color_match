$data modify entity @n[type=marker,tag=color_match_painting,tag=color_match_init] data.palette_map set value $(palette_map)

$data modify storage color_match:temp all.palette_map set value $(palette_map)

function color_match:pixel/refresh/main with entity @n[type=marker,tag=color_match_painting]

function color_match:painting/display_block/nearest

data remove storage color_match:temp all