#!/usr/local/bin/python3

"""
    
    Copyright 2018 @RandyMcMillan | RandyMcMillan.net | Randy McMillan
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    
    
    """


#python3.7 sphere.py

#pip install gmpy2
import gmpy2,math

from gmpy2 import * #global * is completely unneccesary mpz,mpfr only is better for this example

#setup some numbers I like
global_partition = mpz(904625697166532776746648320380374280100293470930272690489102837043110636675);
first_prime = mpz(1623087694307053270266275330414301965675413090185657913);
second_prime = mpz(6119161);
third_prime = mpz(24371);
fourth_prime = mpz(2221);
fifth_prime = mpz(211);
sixth_prime = mpz(29);
seventh_prime = mpz(11);
eigth_prime = mpz(5*5);

#think of radius as units per radian
#one radian equals 180 degrees divided by math.pi

class Sphere:
    def __init__(self,unitsPerRadian):
        self.unitsPerRadian = unitsPerRadian
    #self.unitsPerRadian = unitsPerRadian
    def returnDiameter(self):
        return self.unitsPerRadian * 2 # 2 times the radius
    def returnCircumference(self):
        return self.unitsPerRadian * math.pi * 2 # 2 times pi time radius
    def returnSurfaceArea(self):
        return self.unitsPerRadian * self.unitsPerRadian * 4 * math.pi # 4 times pi times radius squared
    def returnVolume(self):
        return (4/3) * math.pi * self.unitsPerRadian * self.unitsPerRadian * self.unitsPerRadian # four thirds times pi times radius cubed
    def printUnitsPerRadian(self):
        print("self.unitsPerRadian =",self.unitsPerRadian)

#largeInt inherits mpz type from large primes enumerated above
largeInt = first_prime*second_prime*third_prime*fourth_prime*fifth_prime*sixth_prime*seventh_prime*eigth_prime
print("largeInt            =",largeInt)
print("global_partition    =",global_partition)
testSphere = Sphere(largeInt)
testSphere.printUnitsPerRadian()
dia = mpfr(testSphere.returnDiameter())
cir = mpfr(testSphere.returnCircumference())
sa = mpfr(testSphere.returnSurfaceArea())
vol = mpfr(testSphere.returnVolume())

print("diamater =",dia)
print("circumference =",cir)
print("surface area =",sa)
print("volume =",vol)


#formulas to think diffferently about spherical math
threeHundredSixtyDegrees = 360 # as in degrees
radian = mpfr(threeHundredSixtyDegrees / (2*math.pi)) # TODO: calc pi better
halfRadian = mpfr(threeHundredSixtyDegrees / (4*math.pi))
areaOfCircle = mpfr(threeHundredSixtyDegrees * ((1/2)*radian)) # 10313.24031 Area of Circle in radians
print("360          =",threeHundredSixtyDegrees)
print("radian       =",radian,"in degree units")
print("halfRadian   =",halfRadian,"in degree units")
print("areaOfCircle =",areaOfCircle,"in degree units")

#Radian Based Sphere
class RadianSphere:
    def __init__(self):
        return None
    def returnDiameter(self):
        return 2*radian
    def returnCircumference(self):
        return threeHundredSixtyDegrees
    #this is where we change methods of calulating attributes of a sphere
    def returnSurfaceArea(self):
        return threeHundredSixtyDegrees * 4 * (1/2) * radian
    def returnVolume(self):
        return threeHundredSixtyDegrees * 4 * (1/2) * radian * (1/3) * radian
    def printUnitsPerRadian(self):
        return None

testSphere = RadianSphere()
testSphere.printUnitsPerRadian()
dia = mpfr(testSphere.returnDiameter())
cir = mpfr(testSphere.returnCircumference())
sa = mpfr(testSphere.returnSurfaceArea())
vol = mpfr(testSphere.returnVolume())

print("diamater =",dia)
print("circumference =",cir)
print("surface area =",sa)
print("volume =",vol)

