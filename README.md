<img src="https://static.wikia.nocookie.net/minecraft_gamepedia/images/7/7f/Fishing_Rod_JE2_BE2.png/revision/latest?cb=20200201063839" alt="Fishing Rod Icon" width="50" height="50">

# PyFisher
*Script for automated Minecraft fishing, based on visual bobber state detection.*

Ever since the [1.16](https://minecraft.fandom.com/wiki/Java_Edition_1.16) update, autofishing in Minecraft has gotten more difficult. 
This Python script eases the pain by automating fishing, detecting the current state of the catch and reeling in when required.

Features:
- Automatic detection of the active fishing bobber  
- Customizable parameters
- Dashboard display for current tick state and the amount of catches 
  
   
 ## Area scanned
 To increase effectivity, the script does not scan the entire screen, rather just a portion of it, within which the bobber should be visually kept. By default, the area is roughly equal to the one displayed on the screenshot. <br>
 
<img src="/screenshots/area.png" alt="Overlay" width=640 height=340>

To change the area scanned, update the following line in the code, but be aware that the bigger the analyzed screen region is, the slower the program will run. In testing, too big of a region resulted in a noticable delay that threw off the timings required.

```py
self.coordinates = (750, 150, 1110, 500)
```

## Dashboard

The script offers a dashboard that showcases the current state of the script, as well as a log for how many catches were reeled and the current tick of the script.

<img src="/screenshots/dashboard.png" alt="Overlay">



