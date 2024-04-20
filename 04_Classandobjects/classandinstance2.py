name_list = [
    ('Alice', True, False),
    ('Bob', True, True),
    ('Charlie', False, True),
    ('David', False, False)
]
# Name, Is_Worker, Is_Parent

class Human:
    disposable_time=24
    def __init__(self,name):
        self.name=name #定义父母育儿时长这个property
        print(self.name,"is Human")    

class Parent(Human):

    def __init__(self,name,parentinghour):
        Human().__init__(self,name)
        self.ph=parentinghour #定义父母育儿时长这个property
        print(self.name,"is Parent")      

class Worker(Human):

    def __init__(self,name,workinghour):
        Human().__init__(self,name)
        self.wh=workinghour #定义工人工作时长这个property
        print(self.name,"is Worker")      

    def overwork(self):
        self.wh=+3 #工人拥有加班这个Method    

class ParentWorker(Parent,Worker):
    
    def __init__(self, name, parentinghour, workinghour):
        Parent.__init__(self, name, parentinghour)
        Worker.__init__(self, name, workinghour)
        self.ec = 0

    def extracommuting(self,x): #作为父母的工人或许拥有额外的通勤时长 作为一个方法存入
        self.ec=x

def Freetime(Someone):
    if isinstance(Someone,Human):
        fh=Someone.disposable_time
    if isinstance(Someone,Worker):
       fh=fh-Someone.wh
    if isinstance(Someone,Parent):
        fh=-Someone.ph
    if isinstance(Someone,ParentWorker):
        fh=-Someone.ec
    return fh

for name, IsWorker,IsParent in name_list:
    if IsWorker and IsParent:
        X=ParentWorker(name,2,7)
        X.extracommuting(1)
    elif IsWorker:
        X=Worker(name,8)
        X.overwork()
    elif IsParent:
        X=Parent(name,5)
    print(X.name, Freetime(X))
