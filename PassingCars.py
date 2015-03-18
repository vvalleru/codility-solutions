class PassingCars:
  def __init__(self, A):
    self.A = A
    self.passingCars = 0
    self.carsTravellingEast = 0

  def getPassingCars(self):
    for car in self.A:
      if car == 1:
        self.passingCars += self.carsTravellingEast
        if self.passingCars > 1000000000:
          return -1
      else:
          self.carsTravellingEast += 1

    return self.passingCars