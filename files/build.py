import os
from datetime import date

listedFiles = list(os.listdir())
dict = eval(open("ids","r").read())
folders = []

for id in dict:
    if id in listedFiles:
        print("Adding {id} with tag {tag}".format(id=id,tag=dict[id]))
        folders.append(id)
    else:
        print("Error, can't add {id}".format(id=id))


alldays = []
for folder in folders:
    files = list(os.listdir(folder))
    for file in files:
        new = True
        for d in alldays:
            if d[0]==file:
                new = False
                break
        if new:
            alldays.append([file,folder])
        else:
            for i in range(len(alldays)):
                if alldays[i][0]==file:
                    alldays[i].append(folder)
                    break

alldays.sort()

out = open("result.tex","w")

for day in alldays:
    y = int(day[0][0:4])
    m = int(day[0][4:6])
    d = int(day[0][6:8])
    out.write("\\newpage\n")
    out.write("\section{Le "+date(y,m,d).strftime('%d/%m/%Y')+" :}\n")
    for i in range(len(day)):
        if i==0:
            pass
        else:
            out.write("    \subsection{"+dict[day[i]]+" :}\n")
            out.write("        \input{files/" + day[i] + "/" + day[0] + "}\n")

out.close()


print("\n\n\n\n"+open("result.tex","r").read())
