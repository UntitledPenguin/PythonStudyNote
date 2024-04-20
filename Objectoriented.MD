# 面向对象 or 十分抽象——调包侠入门指南

不知道这个世界上还有没有比“面向对象的程序设计”这几个字更加废话的汉字。所以想针对这个很重要但是总是被讲的很复杂的概念说说自己的理解。

## 对象和类 Object，Class ，Instance

“对象是类的实例”。我感觉没有人在不理解对象和理解到底是什么的时候能把这句话看懂，但是感觉大部分网上的资料的写作方式就像以英文撰写英语课本一样让对程序设计一无所知的人看了还是一无所知。所以，我还是想写写我自己的一些浅显的小理解：

如果把程序看成设计一条流水线，那么object就是要被大卡车拉去工厂送上流水线的东西。因为这些东西能够被放在一条生产线上进行加工，那么他们肯定是共有一些特性的，因此就构成了一个特定的类别（class）。
	-把某个果汁生产工厂的流水线想象成你现在要调用的一段代码，这段代码需要的“水果”这个类的对象：苹果（水果001）、梨子（水果002）、椰子（水果003）。但是如果你调用了一个动物对象（猴子007），这条流水线自然会出现一些故障。
	-在学校里，把点名这个过程看成一个函数，它操作的类就是学生，操作的对象可以是每个具体的学生：比如小王、小张、小李，那么换句话说，小王、小李、小张就是“学生”这个类的实例（instance）。
	
一般情况下，似乎object和instance是可以混用的，但是对象更像是一个特指，而实例是一个基于语境的一个代词：比如说，王小明是一个特定的对象，但是他可以分属于很多的类，因此可以是很多类别的实例，比如说在工地王小明是“搬砖工”的实例，在家庭生活是“爸爸”实例，在赌场是“倒霉蛋”实例。也就是说，“对象”可以脱离某个具体的class依旧存在，但如果没有规定是什么class，instance就无从谈起。

#### 属性和方法 Property， Method

已经知道了对象和实例的区别之后，我们来说说类的建立和使用。

假如我们编写一个3D建模的程序，里面要建立一些3维空间的几何图形，那么我们可以先创建一个大的类：Geometry，对于这个geometry class里的所有实例，我们可以规定一些他们共享的固有属性来描述他们（property），比如说：几何中心点的位置，体积，表面积，等等。那么对于这些几何体，我们还可以进行一些操作，比如：旋转一定的角度，放大一定的倍数……这些就可以被看作是几何体这个class中的instance所共享的Method。

当然，在这个Geometry大类里，还可以包含其他的子类，比如说球体，正方体，圆锥等等。它们共享从属的大类的属性（体积、表面积之类）和方法（都可以被旋转、平移），但每个类也有自己特有的属性和方法，比如球体可以有属性“半径”，也可以定义其特有的方法，“求过特定点的切面”，正方体可以有属性“棱长”，圆锥可以有固定的方法：求扇形展开面 之类的。

特别要注意的是，在诸多method中，有一个特别的constructor method。这个method是建立某个实例所需的初始化环节，一般在python中以 def__init__(self, .....)的形式出现。这是建立某个实例中首先被运行的部分，大多数时候包含了建立这个实例的必要信息：比如说我们要在三维坐标里建立一个点，那么在这个constructor里我们就可以包含（x,y,z）三个坐标，从而定义这个点所在的位置，这样之后的其他method才成为可能，比如平移，复制 等等。如果把整个class的property和method看成一个工具箱，那constructor文件就是打开工具箱首先要阅读的使用说明书，里面往往包含了产品的必要信息和其他初始化的步骤。

在调用property和method时，我们都以 X.property，X.method() 号进行调用，这里的X就是实例的变量名。
####  Function vs Method

在python里，function和method都以 def... 的形式出现，它们二者看起来有很多共同之处，但是也有一些区别。按照我的理解，method总是出现在class里，调用时候也包含了（self,...)，说明它总是在对某一类里的实例进行操作。而function可以独立于某个class存在，在调用时，不必包含self，使用时候更加灵活，可以处理、建立某几类class之间的关系，或者一些更为通用的过程。举个例子，假如我们要对上述的几何图形进行打印，我们就可以建立一个独立于class之外的function，这个function可以打印画布上现在所存在的所有几何对象，也可以假如别的对象比如：比例尺、网格、坐标系，以及关联其他的样式变量。

#### 实例1：疲惫的工人阶级

```
class Human: #首先我们建立一个 human 大类

    disposable_time = 24   # 然后我们给这个人类加入一个属性：所有的人都拥有24小时的可支配时间

    def __init__(self, name): # 初始化人类，传入的变量是每个人的名字
        self.name = name
        
    def Sleep(self): #对于每个人我们先定睡觉这个方法，可支配时间减少8小时因为每个人都要睡觉
        self.disposable_time-=8
  

class Parent(Human): #接下来，我们建立了一个 父母 类

    def __init__(self, name, parentinghour): #这个父母类我们传入的属性有不仅有名字，还有养孩子要花的时间
        self.name=name
        self.ph = parentinghour

class Worker(Human):#接下来，我们建立一个新的 类： 工人

    def __init__(self, name, workinghour): #每一个工人有名字，还有工作时长
        self.name=name
        self.wh = workinghour

    def overwork(self): #对于工人这个类，我们建立一个method，加班，每次运行加班都会加3小时工作时长
        self.wh += 3

class ParentWorker(Parent, Worker): #然后，我们建立一个既是工人又是父母的类，这个类继承了父母和工人所有的属性和方法
    def __init__(self, name, parentinghour, workinghour):
        self.name=name
        self.wh=workinghour
        self.ph=parentinghour
        self.ec = 0
        
    def extracommuting(self, x): #这一类人因为接送小孩还可能会有额外的x小时的通勤消耗 

        self.ec = x

  

def Freetime(Someone): #接下来我们定义一个外部的function，这个function计算的是某个人的自由时间

    if isinstance(Someone,Human):  #首先，如果这个人属于人类，那么先有24小时的可支配时间

       print(Someone.name,"is an instance of Human")

       fh = Someone.disposable_time  # Initialize fh with disposable_time

    if isinstance(Someone, Worker): #判断这个人是不是worker这个类的实例，如果是的话可支配时间就要减去上班的时间了。

       print(Someone.name,"is an instance of Worker")

       fh -= Someone.wh

    if isinstance(Someone, Parent):#判断这个人是不是parent这个类的实例，如果是的话，减去养孩子的时间

       print(Someone.name,"is an instance of Parent")

       fh -= Someone.ph

    if isinstance(Someone, ParentWorker):#最后，如果这个人又是工人又是父母，我们还要减去额外的通勤消耗

       print(Someone.name,"is also an instance of ParentWorker")

       fh -= Someone.ec

    return fh
    #在这个函数里，我们特意打印出每个object所属的instance，来说明object和instance之间的关系。

  

# 在这里我们存放了一些数据，里面有名字，是不是工人，是不是父母：
name_list = [

    ('Alice', True, False),

    ('Bob', True, True),

    ('Charlie', False, True),

    ('David', False, False)

]

#开始对列表里的所有对象进行一个循环，在循环里，我们根据其身份类别先建立一个实例，然后再调用一系列的相关的方法：


for name, IsWorker, IsParent in name_list:

    if IsWorker and IsParent:

        X = ParentWorker(name, 3, 7)

        X.Sleep() #对于每一个Human我们都可以调用Sleep这个方法

        X.extracommuting(1)

        X.overwork() #因为ParentWorker也是Worker，所以我们可以调用加班这个方法

    elif IsWorker:

        X = Worker(name, 8)

        X.Sleep() #对于每一个Human我们都可以调用Sleep这个方法

        X.overwork()

    elif IsParent:

        X = Parent(name, 8)

        X.Sleep() #对于每一个Human我们都可以调用Sleep这个方法

    else:

        X=Human(name)

        X.Sleep()

    print('{} has {} hours of free time'.format(X.name, Freetime(X)))

	#最终我们打印每个人所拥有的自由时间

```

程序的运行输出结果如下：
```
Alice is an instance of Human
Alice is an instance of Worker
Alice has 5 hours of free time
Bob is an instance of Human
Bob is an instance of Worker
Bob is an instance of Parent
Bob is also an instance of ParentWorker
Bob has 2 hours of free time
Charlie is an instance of Human
Charlie is an instance of Parent
Charlie has 8 hours of free time
David is an instance of Human
David has 16 hours of free time
```

可见不上班又不养小孩，就可以拥有最多的可支配时间…（？

### Namespace，Global Variable，Local Variable 命名空间，全局变量和局部变量

建立了这么多类、方法和函数之后，难免会有重名的情况。那么Namespace是理解变量传递的一个重要的概念。在我的理解里，我一直想象把Namespace想象成一栋大楼里各个不同的空间，每个房间都有自己的命名系统，这其中可能有重名的情况，但是具体的所指要根据你目前所在的房间来判断。比方说，主程序就好像一个大楼的大堂，大堂里有几个变量“招待员”“保洁”“搬运工”“大堂经理”等等，那么当前的命名空间就是大堂，但当我们提着行李入住房间了之后，房间里可能又遇到了”保洁“和”招待员“，虽然这些变量名和刚刚大堂里的一样，但此时的命名空间变成了酒店房间，那么显然保洁和招待员所指的也不是同一个人。看一个例子：

### 例：小费给谁了
````
def Go_upstairs(): #上楼，侍者并未跟随

    tip=20 #在楼上你又给了二楼的侍者20块钱
    print("Upstairs_waiter:",tip) #我们查询二楼出现的侍者收到多少钱
    
def Go_upstairs_with_waiter(): #上楼，大堂的侍者跟随了
    global tip #此时我们需要定义tip成为一个全局变量，因为我们知道这里的小费都给了同一个人
    tip+=20 #冤种的我们又在楼上给了20块钱
    print("Upstairs_waiter:",tip) #我们查询现在二楼出现的侍者（其实就是一楼的侍者）收到多少钱

# 酒店大堂，
tip=10 #在酒店大堂里，你打赏了10块钱小费
Go_upstairs() #然后你执行上楼程序
print("Downstairs_waiter:",tip) #此时我们查看大堂里的侍者有多少钱，尽管tip共享同一个变量名，返回值仍然是10，因为所处的命名空间不同。
Go_upstairs_with_waiter() #下面第二次，我们又上楼，此时我们假设大堂里的侍者跟随我们
print("Downstairs_waiter:",tip) #当我们下楼时，再次查询大堂里的侍者有多少钱，当然，它现在有了30块钱，因为上下楼，也就是切换命名空间的过程中，他一直作为全局变量跟随着我们……

````
程序运行结果：````
````
Upstairs_waiter: 20
Downstairs_waiter: 10
Upstairs_waiter: 30
Downstairs_waiter: 30
````
### Package，Module，Library

很多人对于调包（调用现成的包裹）嗤之以鼻，认为从头开始搭建自己的程序才是合格程序员。但其实我自己认为调包和建包是相辅相成的，一个工程师学徒先要弄懂别人的包在干什么->然后把别人的包拿来用->创造自己的包，然后才能一步步变成一个真正的工程师。这就好像学会造自行车，先去外面买一堆轮子、踏板、刹车，他们每一个就像一个小小的包裹，如果能够把这每一个包裹的内容和期间的相互关系弄清楚，再以自己的方式把这些包裹再拼成一辆车还能让它运转起来，已经算一个不错的自行车工程师了。倘若还能对每个模块进行优化、修理，甚至把它改装成电动自行车，那就慢慢成长变成生成高级的自行车的工程师。

当然，这个调包过程也得有个限度，如果自己去买了一辆自行车就说自己是自行车工程师，显然不合适。但是有一些内容对于一个自行车工程师就显然是可以直接调用的，比如，我们大可不必跑去制作橡胶、发明轮子，或者锻造钢铁。因为这些都是前人早就研究制作好的，也就相当于程序设计中已经存在的“package”"module""library"。比如python自带的math，机器学习和数据分析所经常被调用的numpy、pandas、scikit-learn，他们都提供了一系列可以直接调用的方法、类和函数，供大家直接使用。

不严谨的情况下，package，module，library这几个概念可以混用，但是他们之间还是有细微差别。一般认为，module只包含一个.py文件，比如math就是一个单独的python文件，里面包含了一系列代码，而package则包含多个.py文件，一般以文件夹的形式存在，这其中还一般会包含一个__init__.py来阐明其中所有的模块之间的关系和进行初始化。至于library则更加宽泛，可能包含了多个package和modules，是一个更宽泛的工具包。

### 结语

终于磕磕碰碰把这篇文章写完了。因为最近在学ghpythonlib和rhino common几个library的缘故，对library和module以及整个面向对象的程序设计有了点新认识，所以决定写下来。或许还有很多理解不够深刻的地方，在后续的学习中应当继续完善自己的认识。感激chatgpt对我学习的帮助，一些理论的部分也参考了Guido van Rossum的python教程。也希望自己的笔记或许能够帮到更多的人。
