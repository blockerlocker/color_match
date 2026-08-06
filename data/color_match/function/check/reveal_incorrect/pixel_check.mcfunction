execute positioned ~ ~ ~1 run kill @e[type=text_display,tag=color_match_check,distance=..0.2]

execute if block ~ ~ ~ air run return fail

$execute if predicate color_match:$(texture) positioned ~ ~ ~1 run return run function color_match:check/yes_no/correct

data modify storage color_match:temp all.texture set from entity @s data.texture

execute positioned ~ ~ ~1 summon text_display run function color_match:check/reveal_block/text_display with storage color_match:temp all
execute positioned ~ ~ ~1 summon text_display run function color_match:check/reveal_incorrect/incorrect with storage color_match:temp all

data remove storage color_match:temp all