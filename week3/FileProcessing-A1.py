class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def open_file(self): #opening a file here
        with open(self.filepath, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
            file.close()

    def read_first_char_of_each_line(self): # Reading the first char of each line
        with open(self.filepath, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line[0:1])
            file.close()

    def write_file(self, text="\n"): #writing to the file
        with open(self.filepath, "w") as file:
            file.write(text)
        file.close()

    def append_file(self, text): 
        with open(self.filepath, "a") as file:
            file.write(text)
        file.close()

manager = FileManager("./week3/junk.txt")
#manager.open_file()
manager.append_file("End of file\n")
manager.open_file()
