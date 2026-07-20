data modify storage bldp:array_random in set from storage color_match:art_lookup all
function bldp:func/array/random/init

data modify storage color_match:temp all.build set from storage bldp:array_random out

function color_match:build/main