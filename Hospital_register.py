class MedCare:
    def __init__(self):
        self.D1={}
        self.D={}
        self.total=0
        self.bill=0
        self.Y=None
    def patient_Reg(self,name,age,id_no):
        self.name=name
        self.age=age
        self.id_no=id_no
        self.D[self.id_no]=[self.age,self.name]
        
    def consult_Doctor(self,i):
        self.i=i
        L=list(self.D.values())
        K=list(self.D.keys())
        for id_s in K:
            if (id_s==self.i):
                j=self.D[self.i][0]
                if j<17:
                    self.bill=200
                elif j>18 and i<40:
                    self.bill=400
                elif j<40:
                    self.bill=300
        self.D1[self.i]=self.bill
        self.total+=self.bill
        print(self.bill)
        
    def Display_Bill(self,id_sr,Y):
        self.id_sr=id_sr
        self.Y=Y
        if self.Y==1:
            if id_sr in list(self.D.keys()):
                print(self.D1[id_sr])
            else:
                print("INVALID")
        else:
            print(self.total)

def PR():
    global i
    if i<=20:
        name=input("Enter name:")
        age=int(input("Enter age"))
        if (age>0 and age<120):
            print("Your id:",i)
            Obj.patient_Reg(name,age,i)
    else:
        print("Reached limit!")
    
def CD():
    i=int(input("Enter id:"))
    if i in Obj.D:
        presc=input("Enter prescription")
    Obj.consult_Doctor(i)

def DB():
    Y=int(input("Total amount or Patient Bill (0/1):"))
    if Y==1:
        id_no=int(input("Enter patient id:"))
        Obj.Display_Bill(id_no,Y)
    else:
        Obj.Display_Bill(0,Y)
    
    
    
Obj=MedCare()
r=1
i=0
while(r==1):
    print("1.Patient Registration\n2.Consult Doctor\n3.Display Bill\n4.Exit")
    ch=int(input("Enter choice:"))
    i+=1
    if ch==1:
        PR()
        
    elif ch==2:
        CD()

    elif ch==3:
        DB()

    elif ch==4:
        r=0
        print("Thank You")
        
