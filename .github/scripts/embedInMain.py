import sys, re

filePath = sys.argv[1]


with open(filePath, 'r') as file:
    rawContent = file.read()

with open("Src/Main.tex", 'r') as main:
    append = True
    content = ""
    
    for line in main:
        if ph := re.search(r"\\end{document}", line):
            append = True
        if append:
            content = content + line
        if ph := re.search(r"\\begin{document}", line):
            append = False
            content = content + rawContent

with open(filePath, 'w') as file:
    file.write(content)
