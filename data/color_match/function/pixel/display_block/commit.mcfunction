data modify entity @s data.decimal_color set from entity @s background
data merge entity @s {background:0,transformation:{scale:[5,5,0],translation:[-0.125,-0.75,0]}}
$data modify entity @s text set value {atlas:blocks,sprite:"$(sprite)"}