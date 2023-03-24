import sys, os, re, subprocess

title = sys.argv[1]
filePath = sys.argv[2]

content = ""
with open(filePath, 'r') as file:
    i = 0
    for line in file:
        newline = line
        if not os.path.exists("Src/Slike"):
            os.makedirs("Src/Slike")
        if ph := re.search(r"(\\Placeholder\[.*\]{.*})", line):
            i = i+1
            print(ph.group(1))
            slikaName = title + '-slika' + str(i)
            with open("Src/Slike/{}.tex".format(slikaName), 'w') as tikz:
                tikz.write(ph.group(1))
                newline = "\\input{{ Slike/{} }}".format(slikaName)
            subprocess.Popen(['.github/scripts/createTikzIssue.sh {} {}'.format(title, slikaName)]
                             , shell = True
                             , env = os.environ)
        content += newline
        content += "\n"
with open(filePath, 'w') as file:
    file.write(content)
