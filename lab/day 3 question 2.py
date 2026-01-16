numbers_package/
    __init__.py
    writer.py
    reader.py
    numbers.txt
main.py

# writer.py
def write_numbers_to_file(filename):
    try:
        with open(filename, 'w') as file:
            for i in range(1, 101):
                file.write(str(i) + '\n')
        print(f"Numbers written to {filename} successfully.")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except PermissionError:
        print(f"Error: Permission denied to write to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# reader.py
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except PermissionError:
        print(f"Error: Permission denied to read {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# main.py
from numbers_package.writer import write_numbers_to_file
from numbers_package.reader import read_file_content

def main():
    filename = 'numbers_package/numbers.txt'
    write_numbers_to_file(filename)
    print("\nFile Content:")
    read_file_content(filename)

if __name__ == "__main__":
    main()