# Define the Brainf*ck commands and their C equivalents
commands = {
    ">": "++ptr;\n",
    "<": "--ptr;\n",
    "+": "tape[ptr] = (tape[ptr] + 1) % 256;\n",
    "-": "tape[ptr] = (tape[ptr] - 1) % 256;\n",
    ".": 'printf("%c",tape[ptr]);\n',
    ",": 'tape[ptr] = getch();\n',
    "[": "while (tape[ptr] != 0){\n",
    "]": "}\n"
}

# Import the sys module for input and output
import sys

# Get the name of the BF file from the command line argument
bf_file = sys.argv[1]

# Open the BF file and read its contents
with open(bf_file, "r") as f:
    bf_code = f.read()

# Initialize the tape, the pointer, and the indentation level
tape = [0] * 30000
ptr = 0
indent = 1

# Open a new C file with the same name as the BF file
c_file = bf_file.replace(".bf", ".c")
with open(c_file, "w") as f:
    # Write the initial code to set up the tape and the pointer
    f.write("#include <stdio.h>\n#include <conio.h>\n")
    f.write("char tape[30000];\n")
    f.write("int ptr = 0;\n")

    f.write("int main()\n{\n")
    # Loop through each character in the BF code
    for c in bf_code:
        # If the character is a valid Brainf*ck command
        if c in commands:
            # Write the corresponding C code with the proper indentation
            f.write("    " * indent + commands[c])
            # If the command is a loop start, increase the indentation level
            if c == "[":
                indent += 1
            # If the command is a loop end, decrease the indentation level
            elif c == "]":
                indent -= 1
    f.write("}")