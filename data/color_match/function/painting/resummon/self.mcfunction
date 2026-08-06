execute unless entity @s[type=marker,tag=color_match_painting,tag=color_match_init] run return fail

data modify storage color_match:temp all.name set from entity @s data.name

function color_match:painting/delete/self

execute at @s run function color_match:painting/spawn/set with storage color_match:temp all

data remove storage color_match:temp all