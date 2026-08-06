data merge entity @s {text:" ",transformation:{scale:[8,4,1],translation:[-0.1,-0.5,0.001]}}
$data modify storage color_match:temp all.texture set from storage color_match:temp all.palette_map[$(pixel_index)]
function color_match:lookup/texture_color with storage color_match:temp all
data modify entity @s background set from storage color_match:temp all.texture_decimal
data modify entity @s data.decimal_color set from entity @s background
data modify entity @s data.texture set from storage color_match:temp all.texture