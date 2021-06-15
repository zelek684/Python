

litery ={
    "A":"• —",
    "B":"— • • •",
    "C":"— • — •",
    "D":"— • •",
    "E":"•",
    "F":"• • — •",
    "G":"— — •",
    "I":"• • • •",
    "J":"• •",
    "K":"• — — —",
    "L":"— • —",
    "M":"• — • •",
    "N":"— —",
    "O":"— — —",
    "P":"• — — •",
    "R":"— — • —",
    "S":"• — •",
    "T":"• • •",
    "U":"—",
    "W":"• • —",
    "Y":"— • — —",
    "Z":"— — • •",
    "Ź":"— — • • — •",
    "Ż":"— — • • —",


}

slowo = str(input("podaj slowo "))
slowo= slowo.upper()
print(slowo)
for litera in slowo:
    print(litery[litera])


slowo = "KoT Tom"
