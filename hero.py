class Hero():
    """Class to create Hero for our game"""
    def __init__(self, name, level, race):
        """Initiate our Hero"""
        self.name=name
        self.level=level
        self.race=race
        self.health=100

    def show_hero(self):
        """Print all atributes of our hero"""
        discription=(self.name+" "+"Level is: "+str(self.level)+" Race is: "+self.race+" Health is "+str(self.health)).title()
        print(discription)

    def level_up(self):
        """Update Level of Hero"""
        self.level+=1
            
    def move(self):
        """Start moving hero"""
        print("Hero "+self.name+" start moving...")

    def set_health(self, new_health):
        """Chanching health of hero"""
        self.health=new_health
