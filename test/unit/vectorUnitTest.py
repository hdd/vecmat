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
from vecmat.vector import Vector

class VectorUnitTest(unittest.TestCase) :
	'''
	vector module testing
	'''
	
	def setUp(self):
		'''
		crete some basic vectors to test with 
		'''
		self.vec1 = Vector([3,2,1])
		self.vec2 = Vector([1,2,3])
		
	def test_create(self):
		'''
		create an empty vector
		'''
		testVector = Vector()
		self.assertEqual(testVector,Vector([0,0,0]))
	
	def test_sum(self):
		'''
		sum 2 vectors
		'''	
		result = self.vec1 + self.vec2
		self.assertEqual(result,Vector([4,4,4]))
		
	def test_sub(self):
		'''
		subtract 2 vectors
		'''	
		result = self.vec2-self.vec2
		self.assertEqual(result,Vector([0,0,0]))
		
	def test_multFloat(self):
		'''
		multiply vector and float
		'''
		result = self.vec2*10.0
		self.assertEqual(result,Vector([10.0, 20.0, 30.0]))
		
	def test_mulInt(self):
		'''
		multiply vector and int
		'''
		result = self.vec2*10
		self.assertEqual(result,Vector([10.0, 20.0, 30.0]))		
				
	def test_divFloat(self):
		'''
		divide with float
		'''
		result = self.vec2/2.0
		self.assertEqual(result,Vector([0.5, 1.0, 1.5]))		

	def test_divInt(self):
		'''
		divide with int
		'''
		result = self.vec2/2
		self.assertEqual(result,Vector([0.5, 1.0, 1.5]))	
		
	def test_mag(self):
		'''
		calc the magnitude of a vector
		'''
		result =self.vec2.mag()
		self.assertEqual(result,3.7416573867739413)		
		
	def test_dot(self):
		'''
		calculate the dot product of 2 vectors
		'''
		result = self.vec1.dot(self.vec2)
		self.assertEqual(result,10.0)
		
	def test_cross(self):
		'''
		calculate the cross product of 2 vectors
		'''
		result = self.vec2.cross(self.vec1)
		self.assertEqual(result,Vector([-4.0, 8.0, -4.0]))	
		
	def test_angleBetween(self):
		'''
		calculate the angle between 2 vectors
		the result angle is checked in degree
		'''		
		result = self.vec2.angleBetween(self.vec1).toDeg()
		self.assertEqual(result,44.415308597192976)
		
	def test_wPos(self):
		'''
		calculate the weighted position based on two vector
		'''
		result = self.vec2.wPos(self.vec1, 0.75)
		self.assertEqual(result,Vector([2.5,2.0,1.5]))
	
	def test_eq(self):
		'''
		compare 2 vectors
		'''
		self.assertTrue(self.vec1 == self.vec1)

	def test_eq_1(self):
		'''
		compare vector and list4
		'''
		self.assertTrue(self.vec1 == [3,2,1,1])
		
	def test_eq_2(self):
		'''
		compare vector and list3
		'''
		self.assertTrue(self.vec1 == [3,2,1])
		
	def test_eq_3(self):
		'''
		compare vector and list4
		'''
		self.assertFalse(self.vec1 == [3,2,1,0])	

	def test_eq_4(self):
		'''
		compare vector and list3
		'''
		self.assertFalse(self.vec1 == [3,2,0])


	def test_eq_5(self):
		'''
		compare vector and touple4
		'''
		self.assertFalse(self.vec1 == (3,2,1,0))	

	def test_eq_6(self):
		'''
		compare vector and touple3
		'''
		self.assertFalse(self.vec1 == (3,2,0))
					
	def test_ne(self):
		'''
		compare 2 different vectors
		'''
		self.assertTrue(self.vec1 != self.vec2)
		
	def test_normalize(self):
		'''
		normallize vector
		'''
		result = self.vec1.normalize()
		self.assertEqual(result,Vector([0.80178372573727319, 0.53452248382484879, 0.2672612419124244]))
						
	def test_mixMath_1(self):
		'''
		V.normalize()*V.mag()
		'''
		result = self.vec1.normalize()*self.vec2.mag()
		self.assertEqual(result,Vector([3.0, 2.0, 1.0]))
		
	def test_directAssigment(self):
		'''
		direct assigment for vector element
		'''
		V=Vector()
		V[0]=1
		V[1]=2
		V[2]=3
		self.assertEqual(V,Vector([1,2,3]))
						
		
if __name__ == '__main__':
	unittest.main()