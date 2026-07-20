kill @e[tag=color_match_check]

execute as @e[type=text_display,tag=color_match_pixel] at @s run function color_match:check/reveal_block/pixel_check with entity @s

execute as @a at @s run playsound block.note_block.bell ui @s