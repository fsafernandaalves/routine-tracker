# Nightly Routine Tracker

#### Video Demo: <URL [here](https://youtu.be/dvTkwlZnwhw)>

#### Description:

This project is a small command-line program written in Python that helps me keep track of my child's nightly routine. The main reason I made it is that my kid takes medicine every night, and it is easy to forget whether it was already taken, especially when the evening gets busy. I also wanted a simple place to keep track of other daily jobs like brushing teeth and cleaning up the bedroom. Instead of using a sticky note or trying to remember, I can open the program, look at tonight's list, and check things off as they get done.

When the program starts for the first time, it asks for the child's name and creates a starting list with three tasks: "Take nightly medicine", "Brush teeth", and "Clean up the bedroom". After that it shows a menu with five options:

1. **Show today's list.** This prints every task with a box next to it. `[x]` means the task was done today and `[ ]` means it still needs to be done. At the bottom it tells me how many tasks are left, or says "All done for today" when everything is checked off.
2. **Check off a task.** This shows the list, asks for the number of the task that was finished, and saves it under today's date. If the task was already checked off today, it just tells me so instead of saving it twice.
3. **Add a task.** I can type in a new task, like "Pack school bag". It will not accept an empty task or one that is already on the list.
4. **Remove a task.** This shows the numbered list and lets me remove one, in case a chore is not needed anymore.
5. **Quit.** This ends the program.

Everything is saved to a file, so when I close the program and open it again the next night, my tasks and my history are still there. Each new day starts with a fresh, empty checklist because the program checks off tasks by today's date.

## Files in this project

**TermProject.py** is the whole program. It has a `main` function that shows the menu in a loop, plus these other functions, which are all defined at the top level of the file:

- `load_data()` reads the save file if it exists, or asks for the child's name and builds a new starting list if it does not. If the save file is broken, it prints a message and starts over instead of crashing.
- `save_data(data)` writes the current information to the save file.
- `done_on(data, day, task)` answers one simple question: was this task checked off on this day? I made it its own function because both the list display and the "left to do" count need the same check, and I did not want to repeat it.
- `show_today(data)` prints today's checklist and the number of tasks left.
- `mark_done(data)` handles checking off a task.
- `add_task(data)` handles adding a new task.
- `remove_task(data)` handles removing a task.

**requirements.txt** lists the libraries the project needs. This project only uses things that come with Python (`json`, `datetime`, and `pathlib`), so nothing needs to be installed. The file only contains a comment saying so.

**routine_data.json** is not something I wrote by hand. The program creates it the first time it runs and updates it every time something changes. It holds the child's name, the list of tasks, and a log of which tasks were done on which dates.

**README.md** is this file.

## Design decisions

**Why a command-line program?** I wanted to finish something that works and that I fully understand, rather than something fancy that I could not explain. A text menu is easy to use and easy to test, and it let me spend my time on the logic instead of on a graphical interface.

**Why JSON for saving?** I could have used a plain text file or a database, but JSON stores lists and dictionaries almost exactly the way Python uses them, so reading and writing is only a couple of lines. It is also human-readable, so if something goes wrong I can open the file and see what happened.

**Why store the log by date?** The log is a dictionary where each key is a date like `2026-10-20` and each value is the list of tasks finished that day. This makes "was it done today?" very easy to answer, and it means old days are kept in the file. I kept the history on purpose, even though the program does not display it right now, because it would be easy to add a history view later. I originally had a weekly summary and streak counter, but I took them out to keep the project simple and focused on the nightly check.

**Why check for mistakes?** Anything the user types can be wrong, so I used `try` and `except` when turning a typed number into a list position, and I check for empty input. That way a typo like "abc" or a number that is too big just prints a message and returns to the menu instead of crashing the program.

**Why small functions?** I split the program into short functions that each do one job. This made it easier to find bugs, and it keeps `main` short and readable.

## How to run it

Make sure Python 3 is installed, put `TermProject.py` in a folder, open a terminal in that folder, and run:

```
python TermProject.py
```

In the future, I would like to add support for more than one child, a reminder if the medicine has not been checked off by bedtime, and a way to look back at past days.
