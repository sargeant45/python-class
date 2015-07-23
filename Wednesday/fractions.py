class Fraction:
  def __init__(self, num, den):
    self.num = num
    self.den = den
  
  def toFloat(self):
    return float(self.num) / float(self.den)
  
  def __float__(self):
    return float(self.num) / float(self.den)

  def __str__(self):
    return str(self.num) + " / " + str(self.den)
  
frac1 = Fraction(3, 2)
print(float(frac1) * 1)