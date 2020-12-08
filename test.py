from Mines import CoalMine
from Mines import IronMine
from Factories import SteelFactory            
        
t1 = IronMine("Iron Mine")
t2 = CoalMine("Coal Mine")
c = 10
while c > 0:
    t1.tick()
    t2.tick()
    print(t1.output)
    print(t2.output)
    c -= 1
