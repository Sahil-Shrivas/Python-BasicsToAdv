class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips 
    

class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color
    
class Punefactory(BhopalFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets