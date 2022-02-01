print("Hello")
print("This is a program for a database where you will have the name and number of a person")
print("Type in 'input' if you want us to input data")
print("Type in 'print' if you want us to output data")
print("Type in 'remove' if you want us to remove data")
print("Type in 'get' if you want to find the data of someone specific")
print("Type in 'change' if you want to change the data of someone in your contacts")
dic={}
lis=[]
while 1:
    A=input()
    A=A.lower()
    if A=='input':
        x=input("Please enter the name of the person: ")
        y=input("Please enter the number of the person: ")
        x=x.lower()
        lis.append(x)
        dic[x]=y
    elif A=='print':
        if len(lis)==0:
            print("Sorry, you haven't inputted anything")
        else:
            print("Here's your current database")
            for i in lis:
                print(i.capitalize(),dic[i])
    elif A=='remove':
        z=input("Please enter the contact you want to remove: ")
        lis.remove(z.lower())
        dic.pop(z.lower())
    elif A=='get':
        z=input("Please enter the name of the person you want the number of: ")
        print(dic[z.lower()])
    elif A=='change':
        z=input("Enter the name of the person whose data you want to change: ")
        d=input("What's their new contact: ")
        dic[z.lower()]=d
    
        
        
