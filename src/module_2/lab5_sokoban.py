def main():
    history = []

    while True:
        action = input("Enter an action (or 'Undo' or 'Restart'): ")

        if action == "Undo":
            if history:
                last_action = history.pop()
                print(f"Undone: '{last_action}'")
            else:
                print("No actions to undo.")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)

        print(history)

main()