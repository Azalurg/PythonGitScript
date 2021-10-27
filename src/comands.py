import gitFunctions
import actions

path = "paths.txt"


def print_all_paths():
    try:
        with open(path) as file:
            for line in file:
                print(line, end="")
    except Exception as e:
        print(e)


def close_app():
    pass


def print_help():
    for key, val in actions.actions.items():
        print(str(key) + ": " + val["description"])


def add_path():
    with open(path, "a") as file:
        val = input("enter the path: ")
        file.write(val + "\n")


def delete_path():
    print("Select number of line you want to delete")
    print("To delete all enter '000'")
    dir_list = []
    with open(path, "r") as file:
        counter = 1
        for line in file:
            dir_list.append(line)
            print(str(counter) + ". " + line, end="")
            counter += 1
    decision = input("Enter your choice: ")
    if decision == "000":
        print("!!! YOU ARE ABOUT TO DELETE ALL PATHS !!!")
    else:
        try:
            decision = int(decision)
            if int(decision) <= len(dir_list):
                print("You are about to delete: " + dir_list[int(decision) - 1], end="")
            else:
                print("Wrong input")
                pass

        except ValueError:
            print("Wrong input")

    agreement = input("(Y/n) ")
    if agreement in ["Y", "y", "yes", "Yes", "YES"]:
        if decision == "000":
            file = open(path, "w")
            file.close()
        else:
            dir_list.pop(int(decision - 1))
            file = open(path, "w")
            for line in dir_list:
                file.write(line)
            file.close()


def projects_pull():
    counter = 0
    counter_errors = 0
    with open(path, "r") as file:
        for line in file:
            success, error = gitFunctions.pull_project(line[:-1])
            counter += 1
            if success:
                print("Pull - {}".format(line), end="")
            else:
                print("ERROR - {}".format(line), end="")
                counter_errors += 1
    print("You are up to date!")
    print("Pull operations done: {}/{}".format(counter - counter_errors, counter))


def projects_status():
    counter = 0
    counter_errors = 0
    with open(path, "r") as file:
        for line in file:
            success, error = gitFunctions.show_status(line[:-1])
            counter += 1
            if success:
                pass
            else:
                print("ERROR - {}".format(line), end="")
                counter_errors += 1
    print("Status checked!")
    print("Correct operations: {}/{}".format(counter - counter_errors, counter))


def projects_push():
    counter = 0
    counter_errors = 0
    with open(path, "r") as file:
        for line in file:
            success, error = gitFunctions.push_all(line[:-1])
            counter += 1
            if success:
                print("Push - {}".format(line), end="")
            else:
                print("ERROR - {}".format(line), end="")
                counter_errors += 1
    print("Status checked!")
    print("Correct operations: {}/{}".format(counter - counter_errors, counter))


def projects_commit():
    counter = 0
    counter_errors = 0
    with open(path, "r") as file:
        for line in file:
            success, error = gitFunctions.commit_all_git(line[:-1])
            counter += 1
            if success:
                print("Commit - {}".format(line), end="")
            else:
                print("ERROR - {}".format(line), end="")
                counter_errors += 1
    print("Status checked!")
    print("Correct operations: {}/{}".format(counter - counter_errors, counter))
