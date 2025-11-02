class File_demo:
    def write_data_to_file(self):
        data = "It is data sciences batch"
        ptr = open("d:\\trick\\myfile.txt", "w")  # use same file name
        ptr.write(data)
        ptr.close()
        print("Data saved successfully!")

    def read_data_from_file(self):
        ptr = open("d:\\trick\\file.text", "r")  # same file name
        print(2 + 3)
        print(ptr.read())
        ptr.close()

        

# Create object and test
obj = File_demo()
obj.write_data_to_file()
obj.read_data_from_file()
