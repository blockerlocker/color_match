data remove storage bldp:array_random out

execute store result score #bldp_array_random operator if data storage bldp:array_random in[]

data modify storage bldp:temp all.random.x set value 0
execute store result storage bldp:temp all.random.y int 1 run scoreboard players remove #bldp_array_random operator 1

function bldp:func/random/value with storage bldp:temp all.random

function bldp:func/array/random/commit with storage bldp:temp all.random

data remove storage bldp:array_random in
data remove storage bldp:temp all