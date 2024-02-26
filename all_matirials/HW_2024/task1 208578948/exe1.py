def Task1():
    print("The Age Generator")
    try:
        open("ages1.txt", 'r')
    except FileNotFoundError:
        print(f"FileNotFoundError: the file 'ages1.txt' does not exsits.")
        
        with open("ages.txt" , 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            for line in lines:
                try:
                    Age = int(line)
                    print(f"The age listed is: {Age}",end= "\n\n" )
                except ValueError:
                    print(f"The age listed is: {line}", end="\n")
                    print("ValueError: that is an Invalid age.",end="\n\n")


    except Exception as e:
        print(f"Unexpected error: {e}")
    except EOFError:
        print("End of file.")
if __name__ == '__main__':
    Task1()

