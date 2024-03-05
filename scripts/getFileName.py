def run():
    file_path = 'outputs/count.txt'
    with open(file_path, 'r+') as file:
        # Read the entire contents of the file
        file_contents = file.read()
        plus = int(file_contents) + 1
        file.seek(0)  # Move the file pointer to the beginning of the file
        file.write(str(plus))
        file.truncate() 
        return file_contents


