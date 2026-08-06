data merge entity @s {text:" ",transformation:{scale:[8,4,1],translation:[-0.1,-0.5,0.001]}}

function color_match:lookup/palette_index with entity @s data
data modify entity @s data.texture set from storage color_match:temp all.index_texture
function color_match:lookup/texture_color with entity @s data
data modify entity @s background set from storage color_match:temp all.texture_decimal
data modify entity @s data.decimal_color set from storage color_match:temp all.texture_decimal

data modify entity @s data.decimal_color set from entity @s background