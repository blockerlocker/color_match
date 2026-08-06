data modify storage color_match:temp all.build.pixel_data set value {text:" ",transformation:{scale:[8,4,1],translation:[-0.1,-0.5,0.001]},brightness:{sky:15,block:15},Tags:[color_match_entity,color_match_pixel]}
data modify storage color_match:temp all.build.pixel_data.data.owner set from entity @n[type=marker,tag=color_match_painting,tag=!color_match_init] UUID
data modify storage color_match:temp all.build.pixel_data.background set from storage color_match:temp all.texture_decimal
data modify storage color_match:temp all.build.pixel_data.data.decimal_color set from storage color_match:temp all.texture_decimal
data modify storage color_match:temp all.build.pixel_data.data.texture set from storage color_match:temp all.build.texture
data modify storage color_match:temp all.build.pixel_data.data.pixel_index set from storage color_match:temp all.build.pixel_index

execute unless data storage color_match:temp all.build{current_pixel_color:"none"} summon text_display run data modify entity @s {} merge from storage color_match:temp all.build.pixel_data