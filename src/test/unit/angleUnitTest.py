# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version.
# 
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA


import unittest
from vecmat.angle import Angle

class AngleUnitTest(unittest.TestCase):
	'''
	angle module testing
	'''
	
	def setUp(self):
		'''
		crete some basic vectors to test with 
		'''
		self.ang1 = Angle(90).setAsDeg()
		self.ang2 = Angle(1.5707963267948966)
		
	def test_chkDegType(self):
		'''
		check if the fist angle is a degree
		'''
		self.assertTrue(self.ang1.isDeg())
		
	def test_chkRadType(self):
		'''
		check if the fist angle is grade
		'''
		self.assertTrue(self.ang2.isRad())		
	
	def test_toRad(self):
		'''
		deg to rad
		'''
		result = self.ang1.toRad()
		self.assertEqual(result,Angle(1.5707963267948966))
	
	def test_toDeg(self):
		'''
		rad to deg
		'''
		result = self.ang2.toDeg()
		self.assertEqual(result,Angle(90).setAsDeg())

	def test_toRadAndBack(self):
		'''
		deg to rad to deg
		'''
		result = self.ang1.toRad()
		self.assertEqual(result.toDeg(),self.ang1)		

	def test_toDegAndBack(self):
		'''
		rad to deg to rad
		'''
		result = self.ang2.toDeg()
		self.assertEqual(result.toRad(),self.ang2)
		
	def test_doubleRad(self):
		'''
		deg to deg
		'''
		result = self.ang2.toRad()
		self.assertEqual(result,self.ang2)
		
	def test_doubleDeg(self):
		'''
		rad to rad
		'''
		result = self.ang1.toDeg()
		self.assertEqual(result,self.ang1)		
		
	def test_eq_1(self):
		'''
		compare 2 deg
		'''
		result = (self.ang1 == Angle(90).setAsDeg())
		self.assertTrue(result)

	def test_eq_2(self):
		'''
		compare a deg and a rad
		'''
		result = (self.ang1 == self.ang2)
		self.assertTrue(result)
				
	def test_eq_3(self):
		'''
		compare a deg and a float
		'''
		result = (self.ang1 == 90.0)
		self.assertTrue(result)

	def test_eq_4(self):
		'''
		compare a deg and a int
		'''
		result = (self.ang1 == 90)
		self.assertTrue(result)

	def test_ne_1(self):
		'''
		compare 2 deg
		'''
		result = (self.ang1 != Angle(90).setAsDeg())
		self.assertFalse(result)

	def test_ne_2(self):
		'''
		compare a deg and a rad
		'''
		result = (self.ang1 != self.ang2)
		self.assertFalse(result)
				
	def test_ne_3(self):
		'''
		compare a deg and a float
		'''
		result = (self.ang1 != 90.0)
		self.assertFalse(result)

	def test_ne_4(self):
		'''
		compare a deg and a int
		'''
		result = (self.ang1 != 90)
		self.assertFalse(result)

	def test_add_1(self):
		'''
		sum 2 deg and check the result
		'''
		result = self.ang1 + self.ang1
		self.assertEqual(result,180.0)
		
	def test_add_2(self):
		'''
		sum 2 deg , check if the result is a deg
		'''
		result = (self.ang1 + self.ang1)
		self.assertTrue(result.isDeg())
				
	def test_add_3(self):
		'''
		sum a rad and a deg and check the result in deg
		'''
		result = (self.ang1 + self.ang2).toDeg()
		self.assertEqual(result,180.0)		
		
	def test_add_4(self):
		'''
		sum a degree and a float and check the return type
		'''
		result = self.ang1 + 10.0
		self.assertTrue(result.isDeg())
		
	def test_add_5(self):
		'''
		sum a degree and a float and check the return type
		'''
		result = self.ang1 + 10.0
		self.assertTrue(result.isDeg())
		
	def test_add_6(self):
		'''
		sum a degree and a rad
		'''
		result = self.ang1 + self.ang2
		self.assertEqual(result,3.1415926535897931)		

		
	def test_add_7(self):
		'''
		sum a degree and a rad
		'''
		result = self.ang2 + self.ang2
		self.assertTrue(result.isRad())		


	def test_add_8(self):
		'''
		sum a degree and a int
		'''
		result = self.ang1 + 90
		self.assertEqual(result,180)		
						
	def test_sub_1(self):
		'''
		subtract degs , check the result type
		'''
		result = self.ang1 + Angle(45.0).setAsDeg()
		self.assertTrue(result.isDeg())	
		
	
	def test_sub_2(self):
		'''
		subtract rads , check the result type
		'''
		result = (self.ang2 - Angle(1.0))
		self.assertTrue(result.isRad())	
		
	def test_sub_3(self):
		'''
		subtract rads and float, check the result type
		'''
		result = (self.ang2 - 1.0)
		self.assertTrue(result.isRad())			
		
	def test_sub_4(self):
		'''
		subtract deg and float , check the result type
		'''
		result = (self.ang1 - 1.0)
		self.assertTrue(result.isDeg())		
				
	def test_sub_5(self):
		'''
		subtract deg , check the result
		'''
		result = (self.ang1 - Angle(45.0).setAsDeg())
		self.assertEqual(result,45.0)	

	def test_sub_6(self):
		'''
		subtract rad and deg , check the result
		'''
		result = (self.ang2 - Angle(90).setAsDeg())
		self.assertEqual(result,0.0)			
		
	def test_sub_7(self):
		'''
		subtract rad and deg , check the result
		'''
		result = (self.ang2 - Angle(90).setAsDeg())
		self.assertTrue(result.isRad())			

	def test_sub_8(self):
		'''
		subtract deg and float , check the result type
		'''
		result = (self.ang1 - 90)
		self.assertEqual(result,0.0)			
			
	def test_mul_1(self):
		'''
		subtract degs , check the result type
		'''
		result = self.ang1 * Angle(45.0).setAsDeg()
		self.assertTrue(result.isDeg())	
		
	
	def test_mul_2(self):
		'''
		subtract rads , check the result type
		'''
		result = (self.ang2 * Angle(1.0))
		self.assertTrue(result.isRad())	
		
	def test_mul_3(self):
		'''
		subtract rads and float, check the result type
		'''
		result = (self.ang2 * 1.0)
		self.assertTrue(result.isRad())			
		
	def test_mul_4(self):
		'''
		subtract deg and float , check the result type
		'''
		result = (self.ang1 * 1.0)
		self.assertTrue(result.isDeg())		
				
	def test_mul_5(self):
		'''
		subtract deg , check the result
		'''
		result = (self.ang1 * Angle(45.0).setAsDeg())
		self.assertEqual(result,4050.0)	

	def test_mul_6(self):
		'''
		subtract rad and deg , check the result
		'''
		result = (self.ang2 * Angle(90).setAsDeg())
		self.assertEqual(result,2.4674011002723395)			
		
	def test_mul_7(self):
		'''
		subtract rad and deg , check the result
		'''
		result = (self.ang2 * Angle(90).setAsDeg())
		self.assertTrue(result.isRad())					

	def test_mul_8(self):
		'''
		subtract rad and int , check the result
		'''
		result = (self.ang2 * 90)
		self.assertEqual(result,141.37166941154069)		
		
	def test_div_1(self):
		'''
		subtract degs , check the result type
		'''
		result = self.ang1 / Angle(45.0).setAsDeg()
		self.assertTrue(result.isDeg())	
		
	
	def test_div_2(self):
		'''
		subtract rads , check the result type
		'''
		result = (self.ang2 / Angle(1.0))
		self.assertTrue(result.isRad())	
		
	def test_div_3(self):
		'''
		subtract rads and float, check the result type
		'''
		result = (self.ang2 / 1.0)
		self.assertTrue(result.isRad())			
		
	def test_div_4(self):
		'''
		subtract deg and float , check the result type
		'''
		result = (self.ang1 / 1.0)
		self.assertTrue(result.isDeg())		
				
	def test_div_5(self):
		'''
		subtract deg , check the result
		'''
		result = (self.ang1 / Angle(45.0).setAsDeg())
		self.assertEqual(result,2.0)	

	def test_div_6(self):
		'''
		subtract rad and deg , check the result
		'''
		result = (self.ang2 / Angle(90).setAsDeg())
		self.assertEqual(result,1.0)			
		
	def test_div_7(self):
		'''
		subtract rad and deg , check the result
		'''
		result = (self.ang2 / Angle(90).setAsDeg())
		self.assertTrue(result.isRad())		
		
	def test_div_8(self):
		'''
		subtract rad and int , check the result
		'''
		result = (self.ang1 / 90)
		self.assertEqual(result,1.0)		
						
if __name__ == '__main__':
	unittest.main()