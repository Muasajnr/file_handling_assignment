# File Creation
def create_file():
    try:
        # Open the file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some numbers: 98765\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied. Unable to create the file.")
    except Exception as e:
        print("An error occurred:", e)

# File Reading and Display
def read_file():
    try:
        # Open the file in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please create the file first.")
    except Exception as e:
        print("An error occurred:", e)

# File Appending
def append_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the file
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Data appended successfully.")
    except PermissionError:
        print("Permission denied. Unable to append to the file.")
    except Exception as e:
        print("An error occurred:", e)

# Error Handling
def main():
    create_file()  # Create the file
    read_file()    # Read and display the contents of the file
    append_file()  # Append additional data to the file

if __name__ == "__main__":
    main()
