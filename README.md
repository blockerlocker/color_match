<p align="center">
  <img alt="header" src="https://shieldcn.dev/header/gradient.svg?title=Color+Match&amp;subtitle=This+data+pack+adds+a+custom+mini-game+called+%22Color+Match%22&amp;mode=dark&amp;image=https%3A%2F%2Fimgur.com%2FSdfYjei.png" />
</p>

<p align="center">
  <a href="https://youtube.com/@BlockerLockerYT"><img alt="subscribers" src="https://shieldcn.dev/youtube/subscribers/UCsBjURrPoezykLs9EqgamOA.svg?label=Subs" /></a>
  <img alt="Custom badge" src="https://shieldcn.dev/badge/26.3.svg?variant=outline&amp;theme=emerald&amp;label=Minecraft" />
</p>

## Overview

Color Match was made for Minecraft 26.3 by the popular YouTuber **BlockerLocker**.

This data pack allows you to recreate the exact mini-game setup seen in [my videos](https://www.youtube.com/shorts/nATbAgJJMsE). 

> [!NOTE]
> This project is a work in progress and is not necessarily a super simple or polished experience. Be sure to read this guide carefully if you are setting it up for yourself.

### Recommendations

It is highly recommended to play with a mod or [resource pack](https://modrinth.com/resourcepack/unshaded-blocks) that disables block shading. This ensures the side of the block in-game matches the brightness of the raw texture file used for averaging block colors.

### Compatibility

| Minecraft Version | Supported? |
| --- | --- |
| 26.3-snapshot-7 | ✅ |
| 26.3-snapshot-6 | ❌ |
| 26.3-snapshot-5 and earlier | ❌ |
| 26.2.x | ❌ |
| 26.1.x | ❌ |
| 1.21.x and older | ❌ |

> [!WARNING]  
> Running this data pack on unlisted or older versions may work, but it is completely untested and not officially supported.

---

## Commands

Here is an overview of each command you need to play the game:

| Command | Description |
| --- | --- |
| `/function color_match:painting/spawn/set {name:<painting_name>}` | Summon a painting by its name (the file name in the `raw_art` folder). Paintings spawn from the bottom left corner and always face south. They will always have a random color palette when spawned. All commands that have an option for "nearest" search for the nearest painting by its bottom left corner. |
| `/function color_match:painting/spawn/random` | Same as `painting/spawn/set`, but picks a random painting instead. |
| `/function color_match:painting/roll_block/<all\|nearest\|self>` | Several commands for randomizing a painting's palette and displaying its block textures. |
| `/function color_match:painting/roll_color/<all\|nearest\|self>` | Several commands for randomizing a painting's palette and displaying its average colors. |
| `/function color_match:painting/display_block/<all\|nearest\|self>` | Several commands for making a painting display its block textures. |
| `/function color_match:painting/display_color/<all\|nearest\|self>` | Several commands for making a painting display its average colors. |
| `/function color_match:painting/delete/<all\|nearest\|self>` | Several commands for deleting paintings. |
| `/function color_match:painting/resummon/<all\|nearest\|self>` | Resummon the same painting from scratch. Mostly used for debugging. |
| `/function color_match:painting/clone` | Make an exact copy of the nearest painting at the player's current position. |
| `/function color_match:painting/copy_palette` | Copy the color palette of the nearest painting to a clipboard. |
| `/function color_match:painting/paste_palette` | Paste the color palette from the clipboard to the nearest painting. Note that if you paste the colors onto a different type of painting, the colors will probably be messed up. |
| `/function color_match:check/reveal_incorrect/main` | Check how well you did at guessing, with checkmarks on correct guesses, and small Xs with the correct block texture on incorrect guesses. This is my preferred checking command. |
| `/function color_match:check/yes_no/main` | Check how well you did at guessing, with checkmarks on correct guesses, and just small Xs on incorrect guesses. |
| `/function color_match:check/reveal_block/main` | Spawn the correct block textures on top of every pixel. |
| `/function color_match:check/clear` | Remove all check entities. |
| `/function color_match:debug/kill_all_entities` | Remove all Color Match entities. |

---

## Adding Custom Artwork

If you want to add new pieces of art to the game:
1. Place a `.png` file in the `raw_art` folder.
2. Run the `generate_load_data.py` Python script to re-generate the game's data.

> [!WARNING]
> Avoid using **VERY large** pieces of art, as they will likely cause in-game lag.

---

<p align="center">
  <a href="https://github.com/blockerlocker/color_match/graphs/contributors"><img alt="contributors" src="https://shieldcn.dev/contributors/blockerlocker/color_match.svg?names=true&amp;bots=true&amp;mode=dark&amp;watermark=true" /></a>
</p>
