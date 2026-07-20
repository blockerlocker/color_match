data merge entity @s {text:" ",transformation:{scale:[8,4,1],translation:[-0.1,-0.5,0.001]}}
$data modify entity @s background set from storage color_match:temp all.refresh.$(color)
data modify entity @s data.decimal_color set from entity @s background