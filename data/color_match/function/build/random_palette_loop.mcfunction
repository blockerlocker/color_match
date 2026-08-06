data modify storage bldp:array_random in set from storage color_match:temp all.random_palette.remaining[0].blocks
function bldp:func/array/random/init

data modify storage color_match:temp all.random_palette_out append from storage bldp:array_random out

data remove storage color_match:temp all.random_palette.remaining[0]

execute if data storage color_match:temp all.random_palette.remaining[0] run return run function color_match:build/random_palette_loop

data remove storage color_match:temp all.random_palette