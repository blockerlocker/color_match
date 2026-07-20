kill @e[tag=color_match_check]

execute as @e[type=text_display,tag=color_match_pixel] at @s run function color_match:check/yes_no/pixel_check with entity @s

execute if entity @e[type=text_display,tag=color_match_incorrect] as @a at @s run playsound block.note_block.bass ui @s

execute unless entity @e[type=text_display,tag=color_match_incorrect] if entity @e[type=text_display,tag=color_match_correct] as @a at @s run playsound block.note_block.bell ui @s