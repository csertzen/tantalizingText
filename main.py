nameList = ["Jason", "Kristian", "Esme", "Keigo", "Sean", "Stella", "Peter", "Spencer", "Leo"]

def names1():
    for item in nameList:
        print(item)
#names1()
def names2():
    for item in nameList:
        print(item[0])
#names2()
def names3():
    for i in nameList[0]:
        print(i)
#names3()
def names4():
    print(len(nameList))
    for i in range(3):
        #print(i)
        for name in nameList:
            print(i, end='')
        print('')
            
names4()
