execute positioned ~ ~ ~1 run kill @e[type=text_display,tag=color_match_check,distance=..0.2]

execute if block ~ ~ ~ air run return fail

$execute if predicate color_match:color/$(background) positioned ~ ~ ~1 run return run function color_match:check/yes_no/correct

execute positioned ~ ~ ~1 run function color_match:check/yes_no/incorrect