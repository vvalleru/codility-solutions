import PassingCars
import unittest

class PassingCarsTest(unittest.TestCase):
  
  def testOneCarEast(self):
    input = [0]
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)

  def testOneCarWest(self):
    input = [1]
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)

  def testAllCarsTravellingEast(self):
    input = [0] * 10
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)

  def testAllCarsTravellingWest(self):
    input = [1] * 10
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)

  def testFirstCarTravellingWest(self):
    input = [0] * 10
    input[0] = 1
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)

  def testFirstCarTravellingEast(self):
    input = [0] * 10
    input[0] = 1
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)

  def testLastCarTravellingWest(self):
    input = [0] * 10
    input[-1] = 1
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(9,passingCars)

  def testLastCarTravellingEast(self):
    input = [1] * 10
    input[-1] = 0
    pc = PassingCars.PassingCars(input)
    passingCars = pc.getPassingCars()
    self.assertEqual(0,passingCars)