$clone $(pos_x) $(pos_y) $(pos_z) $(pos_x) $(pos_y) $(pos_z) ~ ~ ~ strict replace

execute if block ~ ~ ~ air run tag @s add color_match_pixel_air
execute unless block ~ ~ ~ air run tag @s remove color_match_pixel_air