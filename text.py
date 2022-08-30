from gtts import gTTS
import os
def write():
    name=str(input("enter the name"))
    amount=input("Enter the amount")
    outfile=open("Text.txt","a")
    file = open("Text.txt", "r")
    a=[]
    data=file.readlines()
    for i in data:
        a.append(i.split("="))

    count=0
    for j in range(len(a)):
       
        
        if a[j][0].replace(" ", "")==name.lower().replace(" ", ""):
            print("--------------------------------------------\n")
            print("Name Alredy Exist.. \n Enter Another Name \n")
            print("--------------------------------------------")
            count+=1
            break
    if count==0:
        if name!="" and amount!="":
            outfile.write(name.lower()+" "+"="+" "+amount+"\n")
            outfile.close()
            return 1
        else:
            print("Give Name And Amount")
        return 0

def convert():
    file = open("Text.txt", "r")
    a=[]
    data=file.readlines()
    for i in data:
        a.append(i.split("="))
    for j in a:
        output=gTTS(j[0]+"గారు స్వామి వారికి"+j[1]+"రూపాయలు సమర్పించారు గావున వారిని, వారి కుటుంబాన్ని శ్రీ విఘ్నేశ్వరుడు ఎల్లవేళలా కాపాడి రక్షించు గాక అని ప్రార్ధన.",lang="te",slow=False)
        output.save(j[0]+".mp3")

# def read():
#     file = open("Text.txt", "r")
#     a=[]
#     data=file.readlines()
#     for i in data:
#         a.append(i.split("="))
#     for j in a:

#         os.system("start "+j[0].replace(" ", "")+".mp3")
    
# పోపూరి సాంబశివరావు గారు స్వామి వారికి 1000/- రూపాయలు సమర్పించారు గావున వారిని, వారి కుటుంబాన్ని శ్రీ విఘ్నేశ్వరుడు ఎల్లవేళలా కాపాడి రక్షించు గాక అని ప్రార్ధన.


a=int(input("Entery 1"))
b=100
while b>0:
    if a==1:
        a=write()
        if a==1:
            convert()
        print("------------------------------------------------------\n")
        print("continue cilck --- 1 \n Or \n Break the Event Click ---2\n")
        print("------------------------------------------------------")

        l=int(input())
        if l==1:
            pass
        elif l==2:
            break
        else:
            break

        