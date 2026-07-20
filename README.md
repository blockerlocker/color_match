Made for 26.3

This is the data pack for my mini-game Color Match. You can use this data pack to recreate the same setup I have in [my videos](https://www.youtube.com/shorts/nATbAgJJMsE), but I consider this to be a work in progress, and it's not necessarily a super simple and polished experience. It's also recommended you play with a mod or [resource pack](https://modrinth.com/resourcepack/unshaded-blocks) that disables block shading to make sure the side of the block in-game matches the brightness of the raw texture file used for averaging the block colors.

Here's an overview of each command you need to play the game yourself:
| Command | Description |
| --- | --- |
| `/function color_match:painting/spawn/set {name:<painting_name>}` | Summon a painting by its name (the file name in the `raw_art` folder). Paintings spawn from the bottom left corner and always face south. They will always have a random color palette when spawned. All commands that have an option for "nearest" search for the nearest painting by its bottom left corner. |
| `/function color_match:painting/spawn/random` | Same as `painting/spawn/set`, but picks a random painting instead. |
| `/function color_match:painting/roll_block/<all\|nearest\|self>` | Several commands for randomizing a painting's palette and displaying its block textures. |
| `/function color_match:painting/roll_color/<all\|nearest\|self>` | Several commands for randomizing a painting's palette and displaying its average colors. |
| `/function color_match:painting/display_block/<all\|nearest\|self>` | Several commands for making a painting display its block textures. |
| `/function color_match:painting/display_color/<all\|nearest\|self>` | Several commands for making a painting display its average colors. |
| `/function color_match:painting/delete/<all\|nearest\|self>` | Several commands for deleting paintings. |
| `/function color_match:check/reveal_incorrect/main` | Check how well you did at guessing, with checkmarks on correct guesses, and small Xs with the correct block texture on incorrect guesses. This is my preferred checking command. |
| `/function color_match:check/yes_no/main` | Check how well you did at guessing, with checkmarks on correct guesses, and just small Xs on incorrect guesses. |
| `/function color_match:check/reveal_block/main` | Spawn the correct block textures on top of every pixel. |
| `/function color_match:check/clear` | Remove all check entities. |
| `/function color_match:debug/kill_all_entities` | Remove all Color Match entities.  |

If you want to add new pieces of art to the game, you must use the color palette from `data_generation/raw_art/palette.png`, place your .png in the `raw_art` folder, and then run the `generate_load_data.py` Python script to re-generate the game's data.