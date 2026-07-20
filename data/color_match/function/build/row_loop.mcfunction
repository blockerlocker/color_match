execute if score #remaining_rows operator matches ..0 run return run data remove storage color_match:temp all.build

scoreboard players remove #remaining_rows operator 1

execute store result score #remaining_columns operator run data get storage color_match:temp all.build.height

execute positioned ~1 ~ ~ summon marker run function color_match:build/set_next_column_pos

function color_match:build/column_loop