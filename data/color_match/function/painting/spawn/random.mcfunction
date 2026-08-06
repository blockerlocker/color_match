data modify storage bldp:array_random in set from storage color_match:art_lookup all
function bldp:func/array/random/init

data modify storage color_match:temp all.name set from storage bldp:array_random out

function color_match:painting/spawn/set with storage color_match:temp all