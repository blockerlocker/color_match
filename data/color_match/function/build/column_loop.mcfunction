execute if score #remaining_columns operator matches ..0 run return run function color_match:build/next_column with storage color_match:temp all.build

scoreboard players remove #remaining_columns operator 1

data modify storage color_match:temp all.build.pixel_index set from storage color_match:temp all.build.pixels[0]
data remove storage color_match:temp all.build.pixels[0]

function color_match:build/get_pixel_texture_name with storage color_match:temp all.build
function color_match:lookup/texture_color with storage color_match:temp all.build

execute positioned ~0.5 ~0.5 ~ run function color_match:build/spawn_pixel with storage color_match:temp all.build

execute positioned ~ ~-1 ~ run function color_match:build/column_loop