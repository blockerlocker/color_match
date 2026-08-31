execute if block ~ ~ ~ air run tag @s add color_match_pixel_air
execute unless block ~ ~ ~ air run tag @s remove color_match_pixel_air

execute unless entity @a[predicate=color_match:player/sprint_held] run return fail

execute store result storage color_match:temp all.pos_x int 1 run data get entity @s Pos[0]
execute store result storage color_match:temp all.pos_y int 1 run data get entity @s Pos[1]
execute store result storage color_match:temp all.pos_z int 1 run data get entity @s Pos[2]

data modify storage color_match:temp all.decimal_color set from entity @s data.decimal_color

function color_match:pixel/auto_fill/find_identical with storage color_match:temp all

data remove storage color_match:temp all