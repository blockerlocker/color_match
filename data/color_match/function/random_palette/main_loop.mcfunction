data modify storage color_match:temp all.random_palette.current_color set from storage color_match:temp all.random_palette.remaining[0]
data remove storage color_match:temp all.random_palette.remaining[0]

function color_match:random_palette/grab_shade_pool with storage color_match:temp all.random_palette

data modify storage bldp:array_random in set from storage color_match:temp all.random_palette.shade_pool
function bldp:func/array/random/init

data modify storage color_match:temp all.random_palette.current_shade set from storage bldp:array_random out.color

function color_match:random_palette/add_to_palette with storage color_match:temp all.random_palette

execute if data storage color_match:temp all.random_palette.remaining[0] run return run function color_match:random_palette/main_loop

data remove storage color_match:temp all.random_palette