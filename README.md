# BasicCityPlanningGame

Part of the Deicide D&amp;D 5e campaign

Install and run with

    pip3 install -r requirements.txt
    python3 game.py

Use RIGHT_MOUSE_CLICK to switch between city view and menu view.

Rules:
- Goal is to maximize happiness
- River and Road tiles have no fixed amount, you can have as much as you want of each
- Other tiles have a fixed amount that must exist in map

Rules to enforce by hand:
- River tiles need to be linked to the water on the left by other river tiles
- Palace tiles need to be a single palace
- Road tiles need to be connected to the road tiles on the top, right and bottom of the map

How to increase happiness:
- Residential tiles want to be near Rivers, Markets, Guilds, and Clinics
- Residential tiles do not want to be near Industry and Road
- Trade tiles want to be near Roads, Markets, the Palace, and Military
- Trade tiles do not want to be near Clinics
- Industrial tiles want to be near Rivers, Roads, Military, and Clinics
- Industrial tiles do not want to be near Guilds or the Palace

This is the area of influence (where something is considered near):
X

- An R/T/I tile just needs to be near a single desired tile (for example, having ten clinics near the same residential tile is equivalent to having a single one)

These two are equivalent:
X
