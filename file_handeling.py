import os

filename = "data.txt"

# Function to create or write data to the file
def create_data(data):
    with open(filename, "w") as file:
        file.write(data)
    print(f"Data written to {filename}")

# Function to read data from the file
def read_data():
    try:
        with open(filename, "r") as file:
            data = file.read()
            print(f"Data in {filename}:")
            print(data)
            return data
    except FileNotFoundError:
        print(f"{filename} does not exist.")

# Function to update data in the file
def update_data(new_data):
    try:
        with open(filename, "a") as file:  # Append mode
            file.write("\n" + new_data)
        print(f"Data appended to {filename}")
    except FileNotFoundError:
        print(f"{filename} does not exist. Creating file.")
        create_data(new_data)

# Function to delete specific content from the file
def delete_data(delete_text):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                if delete_text not in line:
                    file.write(line)

        print(f"Data containing '{delete_text}' deleted from {filename}")
    except FileNotFoundError:
        print(f"{filename} does not exist.")

# Function to rename the file
def rename_file(new_filename):
    try:
        os.rename(filename, new_filename)
        print(f"File renamed to {new_filename}")
        global filename
        filename = new_filename  # Update filename to the new name
    except FileNotFoundError:
        print(f"{filename} does not exist.")
    except FileExistsError:
        print(f"{new_filename} already exists.")

# Testing the CRUD operations
if __name__ == "__main__":
    # Create data in the file
    create_data("Hello, this is a sample text.")

    # Read data from the file
    read_data()

    # Update data in the file
    update_data("This is additional text for the file.")

    # Read data after update
    read_data()

    # Delete specific data from the file
    delete_data("sample")

    # Read data after delete
    read_data()

    # Rename the file
    rename_file("new_data.txt")

    # Try reading from the new file
    read_data()
