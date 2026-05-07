# Progress Journal

> Use this journal to track progress, decisions, problems, and next steps.
> Update it after each work session.
> 
---

# 1. Project Overview

## Project Title
[scoring tournament app]

## Project Description
[We have to create an app for a tournament, where the app can be able to track points and allow the school to create teams etc. and it has to be easy to use for anyone.]

## Start Date
[31.3.2026 i started coding]

## Target End Date
[Unknown]

## File list.

## (Dependencies) API / library / module list.
---


# 2. Progress Log

> Add a new session at the top each time you work.

---
## Session [01]
**Date:** [31.3.2026]  
**Time spent:** [50min]  
**Focus:** [Designing the layout of the website]

### Problems / Challenges
- no problems yet
- 

### Solutions / Actions Taken
- actions taken were making the design
- 

### Evidence
- I added the code of the mainmenu and the buttons as we can see from line  1 to 27.


### Reflection
- What went well? the whole process went well
- What needs improvement? now to make the buttons work and make their functions work
- What did I learn? i learned about that i have to loop my code at the end to make it work

---

## Session [02]
**Date:** [1.4.2026]  
**Time spent:** [30 min]  
**Focus:** [Building the competitor setup screen and linking it to the main menu]

### Problems / Challenges
- Used column= inside .pack() which caused an error
- Wasn't sure how to link buttons to different screens, because i had to expeirence with it yet.

### Solutions / Actions Taken
- Removed column= since it only works with .grid(), not .pack()
- Used command=show_competitor_setup to connect the button to the new screen

### Evidence
- Added code from line 10 - 20

### Reflection
- What went well? The screen navigation works and I understand how functions clear and how to go back to the main window
- What needs improvement? Need to get more familiar with which options work with .pack() vs .grid()
- What did I learn? Screens in Tkinter are just functions, not separate files

---
# Session [03]
**Date:** [7.4.2026]  
**Time spent:** [60 min]  
**Focus:** Adding a team name input field to the competitor setup screen

### Problems / Challenges
- Wasn't sure how to read what the user typed into the input box
- The window was too small and some elements were getting cut off

### Solutions / Actions Taken
- Used .get() to retrieve the text from the tk.Entry widget
- Changed the window height from 300 to 400 so everything fits

### Evidence
- Added code

### Reflection
- What went well? The input field works and the error popup shows correctly when the name is left blank
- What needs improvement? Need to learn how to store the saved name so it can be used later in the program
- What did I learn? tk.Entry creates a text box, .get() reads it, and .strip() removes accidental spaces so a blank space doesn't count as a valid name

---
# Session [04]
**Date:** [14.4.2026]  
**Time spent:** [120 min]  
Reflection
- What went well? the input field worked first try which was nice, and the error popup shows up correctly when you leave the name blank which is what i wanted

- What needs improvement? i still need to figure out how to actually store the name somewhere so i can use it later in the program, right now it just shows the popup but doesnt really save anything properly

- What did I learn? i learned that tk.Entry makes the text box and you use .get() to read whatever the user typed, also that .strip() is useful because it stops someone just pressing space and it counting as a valid name



---
# Session [05]
**Date:** [21.4.2026]  
**Time spent:** [300 min]  
Reflection
- What went well? i managed to complete it at the end.

- What needs improvement? i still need to figure out how to actually store the name somewhere so i can use it later in the program, right now it just shows the popup but doesnt really save anything properly

- What did I learn? i learned that tk.Entry makes the text box and you use .get() to read whatever the user typed, also that .strip() is useful because it stops someone just pressing space and it counting as a valid name


# Session [06]
**Date:** [25.4.2026]  
**Time spent:** [200 min]  

Problems / Challenges

Wasn't sure how to store members for each team separately, since all teams share the same dictionary
The members listbox wasn't refreshing when I switched to a different team in the dropdown
Didn't know how to bind the dropdown so it reacts when the user changes the selection

Solutions / Actions Taken

Used a dictionary of lists (team_members) where each key is a team name and the value is a list of member names, so each team has its own separate list


Reflection
- What went well? What went well? Once I understood the dictionary of lists structure it made sense, and the refresh logic worked after I added the bind. The individual scores screen was quicker to build because I could follow the same pattern as teams.
What needs improvement? The results screen is getting long and a bit crowded now that it shows both teams and individuals — might need to think about layout or scrolling
What did I learn? You can bind a Combobox to an event using <<ComboboxSelected>> so a function runs automatically when the user changes the dropdown, and dict.get(key, []) is a safe way to read from a dictionary without crashing if the key doesn't exist yet


# Session [07]
**Date:** [07.05.2026]  
**Time spent:** [100 min]  

Problems / Challenges

The app was showing "Could not load saved data. Error: Expecting value: line 1 column 1 (char 0)" which meant the json file existed but was completely empty
Even after creating the tournament_data.json file manually it still wasnt working
Wasnt sure if the problem was the code or the file itself

Solutions / Actions Taken

Created the tournament_data.json file manually in the same folder as main.py and put the correct starting structure inside it with empty lists and dictionaries
The file had a U next to it in VS Code meaning it wasnt actually saved yet — pressed Cmd+S to save it properly
After saving the file the app loaded correctly with no errors

Evidence

tournament_data.json now exists in the same folder as main.py in the OneDrive coding folder
App runs without any warning popup on startup
Data now persists between sessions

Reflection

What went well? Once I figured out the file just wasnt saved in VS Code it was a quick fix, the actual code was correct the whole time which was good
What needs improvement? I should check if files are properly saved in VS Code before assuming the code is broken, wasted time debugging something that wasnt actually a code problem
What did I learn? VS Code shows a U next to files that havent been saved yet and a dot for unsaved changes — if i see that i need to press Cmd+S before running anything. Also that a json file cant be empty, it needs valid content inside it even if its just empty brackets




# 7. Problems and Fixes

| Problem | Cause | Fix | Status |
|---|---|---|---|
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |

---

11. Final Reflection
What I achieved

Built a fully working tournament scoring app in Python using tkinter that lets you set up teams, add members to teams, set up individual competitors and track scores for both
Added data saving and loading using a JSON file so all the tournament data stays saved even after the app is closed and reopened
Managed to fix multiple bugs and errors throughout the project and kept a progress journal documenting every session

What worked well

The screen navigation system worked really well, using functions to clear and rebuild the window made it easy to add new screens without things breaking
The dropdown menus with ttk.Combobox were good for selecting teams and individuals, much better than typing names in manually every time
Saving data after every single action (not just on close) meant even if the app crashed nothing would be lost

What did not work well

The JSON saving took way longer to fix than it should have, most of the time was wasted not realising the file just wasnt saved in VS Code
The results screen gets quite cramped when there are a lot of teams and individuals shown at the same time, theres no scrolling so things can get cut off
Some of my earlier sessions i didnt write detailed enough notes so i had to try remember what i actually did

What I would improve next time

Add a reset or clear data button inside the app so you can wipe the tournament and start again without having to manually edit the json file
Add a scrollable frame to the results screen so it doesnt get cut off when theres a lot of data
Plan the data structure at the very start before writing any code, i had to add the team_members dictionary and individual stuff later which meant going back and changing a lot of things

Final outcome
The final result is a working tournament scoring application built in Python with tkinter. It allows the user to create up to 4 teams with members, up to 10 individual competitors, enter points for both teams and individuals across events, and view a ranked leaderboard at the end. All data is saved automatically to a JSON file so nothing is lost between sessions. The app runs fully from the main.py file and is easy enough for anyone to use without any technical knowledge.
Did I meet the success criteria (design specifications)?

 The app can create and store teams with up to 4 teams allowed
 Individual competitors can be added and scored separately from teams
 Scores are tracked and displayed in ranked order on the results screen
 Data is saved to a file and reloaded when the app is reopened
 Input validation is in place so blank names and negative scores are rejected

Final evaluation
Overall i think the project went well considering i hadnt done much tkinter before starting. The app does everything the college asked for — it handles both teams and individuals, tracks points across events and shows a final leaderboard. The biggest struggle was the JSON saving which took a few sessions to properly fix but i did eventually get it working. If i had more time i would make the interface look better and add more features like being able to edit or delete teams after creating them. But for what was required i think it meets the brief and the code is commented clearly enough that someone else could read and understand it.