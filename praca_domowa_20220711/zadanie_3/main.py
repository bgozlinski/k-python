class Asystent:
    def __init__(self, filename):
        with open(filename, "r") as input_file:
            self.file = input_file.read()

    def read_file(self):
        return self.file




def main():
    a = Asystent("config_file.txt")
    content = a.read_file()
    print(content.split(' '))

main()
