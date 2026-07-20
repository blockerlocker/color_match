execute store result score #remaining_rows operator run data get storage color_match:temp all.build.width

execute align xyz run summon marker ~ ~ ~ {Tags:[color_match_painting,color_match_entity]}

data modify entity @n[type=marker,tag=color_match_painting,tag=!color_match_init] data set from storage color_match:temp all.build

$execute align xyz positioned ~ ~$(height) ~ run function color_match:build/row_loop

tag @n[type=marker,tag=color_match_painting,tag=!color_match_init] add color_match_init