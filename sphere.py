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

#setup some large primes I like
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

print("Begin normal sphere with very large radius.")

class Sphere:
    def __init__(self,Radius):
        self.Radius = Radius
    #self.unitsPerRadian = unitsPerRadian
    def returnDiameter(self):
        return self.Radius * 2 # 2 times the radius
    def returnCircumference(self):
        return self.Radius * math.pi * 2 # 2 times pi time radius
    def returnSurfaceArea(self):
        return self.Radius * self.Radius * 4 * math.pi # 4 times pi times radius squared
    def returnVolume(self):
        return (4/3) * math.pi * self.Radius * self.Radius * self.Radius # four thirds times pi times radius cubed
    def returnRadius(self):
        return self.Radius

#largeInt inherits mpz type from large primes enumerated above
print("global_partition    =",global_partition)
largeInt = first_prime*second_prime*third_prime*fourth_prime*fifth_prime*sixth_prime*seventh_prime*eigth_prime
print("largeInt            =",largeInt)
testSphere = Sphere(largeInt)
radius = mpz(testSphere.returnRadius())

print("radius              =",radius)

print("All values above are the same.\n")


dia = mpz(testSphere.returnDiameter())
cir = mpz(testSphere.returnCircumference())
sa  = mpz(testSphere.returnSurfaceArea())
vol = mpz(testSphere.returnVolume())

print("diamater            =",dia)
print("circumference       =",cir)
print("surface area        =",sa)
print("volume              =",vol)
print("\n")


print("Begin radian based sphere")

#formulas to think diffferently about spherical math
threeHundredSixtyDegrees = 360 # This is the circumference of a unit sphere based in degree units.
radian = mpfr(threeHundredSixtyDegrees / (2*math.pi)) # This is the "radius" of the unit sphere based in degree units.
#All spheres share the same "radius" which is one (1) radian.
halfRadian = mpfr(threeHundredSixtyDegrees / (4*math.pi)) # Think about this alittle more and consider how it would be used in the next statement.
#It is unlikely that you have seen the area of a circle calculated this way.
areaOfCircle = mpfr(threeHundredSixtyDegrees * ((1/2)*radian)) # 10313.24031 Area of Circle in degree units! Wuh? Remember "units per radian"...
areaOfCircle2 = mpfr(threeHundredSixtyDegrees * halfRadian)

print("360                 =",threeHundredSixtyDegrees)
print("radian              =",radian,"degree units")
print("halfRadian          =",halfRadian,"degree units")
print("areaOfCircle        =",areaOfCircle,"degree units")
print("areaOfCircle2       =",areaOfCircle2,"using halfRadian")

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
        return threeHundredSixtyDegrees * 4 * (1/2) * radian # or use halfRadian
    def returnVolume(self):
        return threeHundredSixtyDegrees * 4 * (1/2) * radian * (1/3) * radian # or use halfRadian
    def printUnitsPerRadian(self):
        return None

testSphere2 = RadianSphere()
testSphere2.printUnitsPerRadian()
dia2 = mpfr(testSphere2.returnDiameter())
cir2 = mpfr(testSphere2.returnCircumference())
sa2  = mpfr(testSphere2.returnSurfaceArea())
vol2 = mpfr(testSphere2.returnVolume())

print("diamater            =",dia2,"degree units")
print("circumference       =",cir2,"degree units")
print("surface area        =",sa2,"degree units")
print("volume              =",vol2,"degree units")


#Handling unit conversion
print("\nHandling unit conversion.")

newDiameter = mpfr(radius*(dia2/radian))
newCirc = mpfr(radius*(cir2/radian))
#newSA = mpfr(radius*(sa2/radian))
#newVol = mpfr(radius*(vol2/radian))

print("testSphere  diameter       =",dia,"units")
print("testSphere2 diameter       =",mpz(newDiameter),"units")
print("testSphere  circumference  =",cir,"units")
print("testSphere2 circumference  =",mpz(newCirc),"units")
#print("surface area        =",newSA,"units")
#print("volume              =",newVol,"units")




