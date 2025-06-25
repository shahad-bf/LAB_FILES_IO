while True:
    ans = input("do u want to add new task? y/n: ").lower()

    if ans == "exit":
        print("program exit")
        break

    if ans == "y":
        t = input("type your task: ")
        file = open("to_do.txt", "a")
        file.write(t + "\n")
        file.close()
       

    elif ans == "n":
        ask = input("see your list? y/n: ").lower()
        if ask == "y":
            try:
                f = open("to_do.txt", "r")
                lines = f.readlines()
                f.close()

                if lines == []:
                    print("not found task")

                else:


                    print("your tasks:")
                    for i in lines:
                        print(" " + i.strip())

            except:
                print("file not found")

