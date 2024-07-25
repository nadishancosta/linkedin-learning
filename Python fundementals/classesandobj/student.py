class Student:
    
    def __init__(self,name,major,gpa,is_on_prob):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_prob = is_on_prob
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False