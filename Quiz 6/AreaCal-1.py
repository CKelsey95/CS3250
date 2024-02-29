class Calculator():   
  def __init__(self, p1, p2):  
    self.s1 = p1
    self.s2 = p2
    self.area = 0
    self.circ = 0

  def set_area(self):
    self.area = self.s1 * self.s2
     #return self.p1 * self.p2

  def set_circumference(self):
    self.circ = 2*(self.s1 + self.s2)
    #return 2*(self.p1+self.p2)