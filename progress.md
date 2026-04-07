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
[31.1.2026 i started coding]

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


# 7. Problems and Fixes

| Problem | Cause | Fix | Status |
|---|---|---|---|
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |

---

# 11. Final Reflection

> Complete this section at the end of the project.

## What I achieved
- 
- 
- 

## What worked well
- 
- 
- 

## What did not work well
- 
- 
- 

## What I would improve next time
- 
- 
- 

## Final outcome
[Describe the final result]

## Did I meet the success criteria (designspecifications)?
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Final evaluation
[Write a short final judgment of the project]

---
- 
