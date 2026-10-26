# TermProject.py
# Nightly routine tracker for my kid (meds, teeth, chores).
# It saves everything in a file so it remembers between runs.

import json
from datetime import date
from pathlib import Path

# the file where we save stuff
DATA_FILE = Path("routine_data.json")

# tasks that show up the first time you run it
DEFAULT_TASKS = ["Take nightly medicine", "Brush teeth", "Clean up the bedroom"]


def load_data():
    # if there is a save file, use it
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Couldn't read the save file, starting over.")

    # otherwise start new
    name = input("Child's name? ").strip()
    if name == "":
        name = "Kiddo"
    return {"child": name, "tasks": list(DEFAULT_TASKS), "log": {}}


def save_data(data):
    # write everything to the file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def done_on(data, day, task):
    # True if this task was checked off on that day
    return task in data["log"].get(day, [])


def show_today(data):
    today = date.today().isoformat()
    print(f"\n--- {data['child']}'s list for {today} ---")

    if len(data["tasks"]) == 0:
        print("No tasks yet. Add one from the menu.")
        return

    # print each task with a box, [x] means done
    for number, task in enumerate(data["tasks"], start=1):
        if done_on(data, today, task):
            box = "[x]"
        else:
            box = "[ ]"
        print(f"{number}. {box} {task}")

    # count what's left
    left = 0
    for task in data["tasks"]:
        if not done_on(data, today, task):
            left += 1

    if left > 0:
        print(f"\n{left} left to do today.")
    else:
        print("\nAll done for today. Good job!")


def mark_done(data):
    show_today(data)
    if len(data["tasks"]) == 0:
        return

    choice = input("\nWhich number did they finish? (Enter to cancel): ").strip()
    if choice == "":
        return

    # make sure they typed a real number from the list
    try:
        task = data["tasks"][int(choice) - 1]
    except (ValueError, IndexError):
        print("That's not a number on the list.")
        return

    # save it under today's date
    today = date.today().isoformat()
    finished = data["log"].setdefault(today, [])
    if task in finished:
        print(f"'{task}' was already checked off today.")
    else:
        finished.append(task)
        save_data(data)
        print(f"Checked off '{task}'!")


def add_task(data):
    task = input("New task: ").strip()
    if task == "":
        print("You have to type something.")
    elif task in data["tasks"]:
        print("That one is already on the list.")
    else:
        data["tasks"].append(task)
        save_data(data)
        print(f"Added '{task}'.")


def remove_task(data):
    # show the list first so they can pick
    for number, task in enumerate(data["tasks"], start=1):
        print(f"{number}. {task}")

    choice = input("Which number to remove? (Enter to cancel): ").strip()
    if choice == "":
        return

    try:
        removed = data["tasks"].pop(int(choice) - 1)
    except (ValueError, IndexError):
        print("That's not a number on the list.")
        return

    save_data(data)
    print(f"Removed '{removed}'.")


def main():
    data = load_data()
    save_data(data)
    print(f"\nWelcome to the routine tracker for {data['child']}!")

    menu = (
        "\nMenu:\n"
        "  1. Show today's list\n"
        "  2. Check off a task\n"
        "  3. Add a task\n"
        "  4. Remove a task\n"
        "  5. Quit"
    )

    # keep showing the menu until they pick quit
    while True:
        print(menu)
        choice = input("Pick 1-5: ").strip()

        if choice == "1":
            show_today(data)
        elif choice == "2":
            mark_done(data)
        elif choice == "3":
            add_task(data)
        elif choice == "4":
            remove_task(data)
        elif choice == "5":
            print("Goodnight!")
            break
        else:
            print("Please pick a number from 1 to 5.")


if __name__ == "__main__":
    main()