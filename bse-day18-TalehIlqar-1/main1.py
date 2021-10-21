class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def perimetr(self):
    return 2 * (self.width + self.height)

  def area(self):
    return self.width * self.height

  def res(self):
    netice = f'''
        En = {self.width}
        Uzunluq = {self.height}
        Perimetr = {self.perimetr()}
        Sahe = {self.area()}
      '''
    
    return netice

a = int(input("type width: "))
b = int(input("type height: "))


x = Rectangle(a,b)
y = x.res()
print(y)


class Parallelepipede(Rectangle):
    def __init__(self, lenght, width, hight):
        super().__init__(lenght,width)
        self.hundurluk = hight

class Parallelepipede(Rectangle):
  def __init__(self, width, height, lin):
    super().__init__(width, height)
    self.lin = lin

  def perim(self):
    p = (self.width + self.height + self.lin) * 4
    return p

  def hecm(self):
    h = self.width * self.height * self.lin
    return h

  def netic(self):
    n = f'''
    en = {self.width}
    uzunluq = {self.height}
    hundurluk = {self.lin}
    perimetr = {self.perim()}
    hecm = {self.hecm()}
    '''
    return n

n = int(input("en daxil et: "))
m = int(input("uzunluq daxil et: "))
l = int(input("hundurluk daxil edin: "))


c = Parallelepipede(n,m,l)
s = c.netic()
print(s)



