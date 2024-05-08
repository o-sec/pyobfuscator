#!/usr/bin/python3
import sys

#colors
P = "\033[1;35;48m"
R = "\033[1;31;48m"
Res = "\033[1;0;48m"

#charset 
chrdict = {'!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126, ' ':32, '\n': 10}

obfuscated = []

def usage():
    print(f"usage :\n\n{sys.argv[0]} file=<file.py> --> for read from file\n{sys.argv[0]} stdin --> for read from standard input\n{sys.argv[0]} stdin/file=<file.py> ofile=<output_file.py> --> read from stdin or file and write output to a file\n\ne.g :\n {sys.argv[0]} file=my_code.py \n {sys.argv[0]} stdin\n {sys.argv[0]} stdin ofile=obf_file.py\n {sys.argv[0]} file=my_code.py ofile=obf_file.py")

def obfuscate(code):
    for char in code:
        obfuscated_char = f"chr({chrdict[char]})"
        obfuscated.append(obfuscated_char)
    obfuscated_code = "+".join(obfuscated)
    return obfuscated_code


try:
    if len(sys.argv) < 2 :
        usage()
    elif len(sys.argv) == 2 :
        if sys.argv[1].lower() == "stdin":
            code = str(input(f"\n{P}[+] - your code here :{Res}\n"))
            print(f"\n{P}here is an obfuscated virsion of your code :{Res}\n")
            print(f"exec({obfuscate(code)})")
        elif "file=" in sys.argv[1].lower():
            try:
                file_name = sys.argv[1].split("=")[1]
                with open(file_name , 'r') as file:
                    file_content = file.read()
                    file.close()
                    obfuscated_file_content = obfuscate(file_content)
                    print(f"\n{P}read from file :{Res} {file_name}\n{P}here is an obfuscated virsion of your code :{Res}\nexec({obfuscated_file_content})")
            except Exception as e:
                print(str(e))
                exit()
        else:
            usage()
    elif len(sys.argv) == 3 :
        if sys.argv[1].lower() == "stdin" and "ofile=" in sys.argv[2].lower():
            try:
                output_file = sys.argv[2].split("=")[1]
                code = str(input(f"\n{P}[+] - your code here :{Res}\n"))
                with open( output_file , 'w' ) as ofile:
                    ofile.write(f"exec({obfuscate(code)})")
                    ofile.close()
                    print(f"\n{P}obfuscated virsion of your code sucessfully saved in file : {Res}{output_file}\n")
            except Exception as e:
                print(str(e))
                exit()
        elif "file=" in sys.argv[1].lower() and "ofile=" in sys.argv[2].lower():
            try:
                file_name = sys.argv[1].split("=")[1]
                with open(file_name , 'r') as file:
                    file_content = file.read()
                    file.close() 
                    output_file = sys.argv[2].split("=")[1]
                    with open( output_file , 'w' ) as ofile:
                        ofile.write(f"exec({obfuscate(file_content)})")
                        ofile.close()
                        print(f"\n{P}read from file :{Res} {file_name}\n{P}obfuscated virsion of your code sucessfully saved in file : {Res}{output_file}\n")
            except Exception as e:
                print(str(e))
        else:
            usage()
    else:
        usage()    

except KeyboardInterrupt as KI:
    print(f"{R}Keyboard Interrupt !{Res}")
    exit()
except Exception as e:
    print(str(e))
    exit()
