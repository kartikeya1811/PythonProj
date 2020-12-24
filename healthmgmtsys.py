# 3 clients - Harry, Rohan, and Hammad
cli_name = {"1": "Harry", "2": "Rohan", "3": "Hammad"}
log_list = {"1": "exercise", "2": "diet"}
act_list = {"1": "log", "2": "retrieve"}


# function that when executed takes as input client name
def getname():
    nam = input("Enter the name:")
    cli_name[str(len(cli_name) + 1)] = nam


def getdata():
    import datetime
    return datetime.datetime.now()


def inputname():
    for i, j in cli_name.items():
        print("Press", i, "for", j)
    cli_key = input()
    print("You have selected", cli_name[cli_key], "\n")
    return cli_key


try:

    for i1, j1 in act_list.items():
        print("press", i1, "for", j1)
    op1 = input()

    op = inputname()

    if op1 == "1":
        for i1, j1 in log_list.items():
            print("press", i1, "for", j1)
        op2 = input()

        if op2 == "1" or op2 == "2":
            data1 = input("Enter info of " + cli_name[op] + " to be logged")
            f = open(cli_name[op] + "_" + log_list[op2] + ".txt", "a")
            f.write("[" + str(getdata()) + "] :" + " " + data1 + "\n")
            f.close()
        else:
            print('Invalid key input')
    elif op1 == "2":
        for i1, j1 in log_list.items():
            print("press", i1, "for", j1)
        op3 = input()
        f = open(cli_name[op] + "_" + log_list[op3] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
except Exception as e:
    print("wrong key input!!")
