$dialog show @s {\
    "type": "minecraft:multi_action",\
    "title": "Manual Recolor",\
    "inputs": [\
        {\
            "type": "minecraft:text",\
            "key": "palette_map",\
            "width": 300,\
            "label": "palette_map",\
            "initial": '$(palette_map)',\
            "max_length": 999999999\
        }\
    ],\
    "actions": [\
        {\
            "label": "Save",\
            "action": {\
                "type": "minecraft:dynamic/run_command",\
                "template": 'function color_match:zzz/manual_recolor_commit {palette_map:\'\u0024(palette_map)\'}'\
            }\
        }\
    ]\
}