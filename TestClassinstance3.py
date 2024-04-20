class Human:
    disposable_time = 24  # Define as class attribute

    def __init__(self, name):
        self.name = name
    def Sleep(self):
        self.disposable_time-=8

class Parent(Human):
    def __init__(self, name, parentinghour):
        self.name=name
        self.ph = parentinghour

class Worker(Human):
    def __init__(self, name, workinghour):
        self.name=name
        self.wh = workinghour 

    def overwork(self):
        self.wh += 3

class ParentWorker(Parent, Worker):
    def __init__(self, name, parentinghour, workinghour):
        self.name=name
        self.wh=workinghour
        self.ph=parentinghour
        self.ec = 0

    def extracommuting(self, x):
        self.ec = x

def Freetime(Someone):
    
    if isinstance(Someone,Human):   
       print(Someone.name,"is an instance of Human")
       fh = Someone.disposable_time  # Initialize fh with disposable_time
    if isinstance(Someone, Worker):
       print(Someone.name,"is an instance of Worker")
       fh -= Someone.wh
    if isinstance(Someone, Parent):
       print(Someone.name,"is an instance of Parent")
       fh -= Someone.ph
    if isinstance(Someone, ParentWorker):
       print(Someone.name,"is also an instance of ParentWorker")
       fh -= Someone.ec
    return fh

name_list = [
    ('Alice', True, False),
    ('Bob', True, True),
    ('Charlie', False, True),
    ('David', False, False)
]

for name, IsWorker, IsParent in name_list:
    if IsWorker and IsParent:
        X = ParentWorker(name, 3, 7)
        X.Sleep()
        X.extracommuting(1)
        X.overwork()
    elif IsWorker:
        X = Worker(name, 8)
        X.Sleep()
        X.overwork()
    elif IsParent:
        X = Parent(name, 8)
        X.Sleep()
    else: 
        X=Human(name)
        X.Sleep()
    print('{} has {} hours of free time'.format(X.name, Freetime(X)))