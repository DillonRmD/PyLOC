import argparse
from prettytable import PrettyTable 

class File:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc

def main():
    parser = argparse.ArgumentParser(prog="./pyloc.py",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # here is the CLI input files to count the lines of code
    parser.add_argument("--files", "-f", nargs="*", type=str, default=[])    

    args=parser.parse_args()

    # this will hold a list of Files class object which will later hold all files information
    fileDetails = []

    # iterate over the files in the CLI file list
    for fileName in args.files:
        # Open the current file
        readFile = open(fileName, "r")

        # readlines() returns a list of lines -> ["mon\n", "tues\n", ...] so we can just find the length of this array and that is the number of lines
        numLines = len(readFile.readlines())
        currentFile = File(fileName, numLines)
        fileDetails.append(currentFile)
    print("PyLOC -- A python tool to count the number of lines in multiple files robustly and quickly!")
    print("By: Dillon Williams -- Programmer, Software Developer, Epic Dude")
    
    table = PrettyTable(["File Name", "Lines of Code"])
    for detail in fileDetails:
        table.add_row([detail.name, detail.loc])

    print(table)
        
    


if __name__ == "__main__":
    main()