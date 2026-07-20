execute positioned ~ ~ ~1 run kill @e[type=block_display,tag=color_match_check,distance=..0.2]

data modify storage color_match:temp all.block_reveal_color set from entity @s background

execute positioned ~ ~ ~1 summon text_display run function color_match:check/reveal_block/text_display with storage color_match:temp all

data remove storage color_match:temp all