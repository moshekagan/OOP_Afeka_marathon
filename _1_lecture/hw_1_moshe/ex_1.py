def ex_1():
    read_lines_from_file("Ages_1.txt")
    read_lines_from_file("Ages.txt")


def read_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                print(line.strip())

                try:
                    age = int(line.strip())
                except ValueError as e:
                    print(f"{type(e).__name__}: file contains invalid age: {line.strip()}")
            raise EOFError
    except FileNotFoundError:
        print(f'File {file_name} not found.')
    except EOFError as e:
        print(f"{type(e).__name__}: end of file")


if __name__ == '__main__':
    ex_1()
