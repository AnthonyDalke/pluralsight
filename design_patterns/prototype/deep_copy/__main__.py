from laptop import Laptop
from tower import Tower, MainBoard

l1 = Laptop("L1", "Intel", "32GB", "2TB SSD", "Onboard", "1920x1080")
l1.display()
l2 = l1.clone()
l2.model = "L2"
l2.processor = "AMD"
l2.display()

t1 = Tower(
    "T1", MainBoard("Asus", "Game"), "AMD", "32GB", "2TB SSD", "Onboard", "1920 x 1080"
)
t1.display()
t2 = t1.clone()
t2.mainboard.model = "Business"
t2.display()
t1.display()
