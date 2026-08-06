data modify storage color_match:temp all.random_palette.remaining set from storage color_match:temp all.build.palette
function color_match:build/random_palette_loop
data modify storage color_match:temp all.build.palette_map set from storage color_match:temp all.random_palette_out

function color_match:build/start with storage color_match:temp all.build

data remove storage color_match:temp all