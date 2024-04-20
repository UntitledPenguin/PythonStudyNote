
class Building:
    withGarden=None

    def __init__(self, groundarea, floornums, floorheight=4):
        self.g_area = groundarea
        self.f = floornums
        self.h = floornums * floorheight

    def GFA(self):
        return self.g_area * self.f

    def FAR(self):
        return self.GFA() / self.g_area  # Corrected the call to GFA()

class Villa(Building):
    withGarden=True
    
    def AddGarden(self,GardenArea):
        self.g_area=self.g_area-GardenArea

class Plot:

    def __init__(self,area):
        self.area=area
        self.b=[]
    def constructbuilding(self,buildings:Building):
        self.b.append(buildings)
    def PlotGFA(self):
        PlotGFA=0
        for building in self.b:
            PlotGFA=PlotGFA+int(building.GFA())
        return PlotGFA
    def PlotFAR(self):
        return(self.PlotGFA()/self.area)


obj_R1 = Building(1000, 10)
obj_V1 = Villa(300,2)
obj_P1 = Plot(3000)
print (obj_P1.area)
obj_V1.AddGarden(40)
print(obj_V1.g_area)
print(obj_V1.FAR())
print(obj_V1.GFA())

obj_P1.constructbuilding(obj_R1)
obj_P1.constructbuilding(obj_V1)
print(obj_P1.b)
print (obj_P1.PlotGFA())
obj_P1.constructbuilding(obj_V1)
print(obj_P1.b)
print (obj_P1.PlotGFA())
print (obj_P1.PlotFAR())

print (obj_R1.withGarden)
print (obj_V1.withGarden)


        