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
from vecmat.matrix import Matrix
from vecmat.vector import Vector

class MatrixUnitTest(unittest.TestCase) :
	'''
	matrix module testing
	'''
	def setUp(self):
		'''
		crete some basic matrix to test with 
		'''
		self.mat1 = Matrix()
		self.mat2 = Matrix([[2,2,1,1],[1,2,3,1],[1,2,1,3],[7,1,3,4]])
		
	def test_create(self):
		'''
		create and compare a simple matrix
		'''
		mat=Matrix()
		matCompare= Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
		self.assertEqual(mat,matCompare)
			
	def test_matMult(self):
		'''
		multiply 2 matrixes
		'''
		result = self.mat1*self.mat2
		self.assertEqual(result,self.mat2)
		
	def test_matMultVec(self):
		'''
		multiply a matrix and a vector
		'''
		vec=Vector([1,2,3])
		result = self.mat1*vec
		self.assertEqual(result,Vector([1.0, 2.0, 3.0]))	
			
	def test_matFromMaya(self):
		'''
		convert a maya matrix to a matrix Object
		'''
		MMatrix=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]
		result = Matrix().fromMaya(MMatrix)
		self.assertEqual(result,self.mat1)
		
	def test_matToMaya(self):
		'''
		convert a matrixObject to Maya
		'''
		MMatrix=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]
		result = Matrix().toMaya()
		self.assertEqual(result,MMatrix)	
		
	def test_matInvese(self):
		'''
		inverse matrix
		'''
		result = self.mat2.inverse()
		compare = Matrix([[0.27777777777777779, -0.1388888888888889, -0.19444444444444442, 0.1111111111111111],\
						 [0.58333333333333326, -0.041666666666666664, 0.041666666666666664, -0.16666666666666666],\
						 [-0.3611111111111111, 0.43055555555555552, -0.09722222222222221, 0.055555555555555552],\
						 [-0.3611111111111111, -0.069444444444444448, 0.40277777777777773, 0.055555555555555552]])
		self.assertEqual(result,compare)	
			
	def test_matTranspose(self):
		'''
		transpose matrix
		'''
		result = self.mat2.transpose()
		compare = Matrix([[2.0, 1.0, 1.0, 7.0],\
						 [2.0, 2.0, 2.0, 1.0],\
						 [1.0, 3.0, 1.0, 3.0],\
						 [1.0, 1.0, 3.0, 4.0]])
		self.assertEqual(result,compare)	
		
	def test_extractRot(self):
		'''
		extractRotation from a matrix
		'''
		MMatrix = [0.81379768134937369, 0.46984631039295416, -0.34202014332566871, 0.0, -0.44096961052988237, 0.8825641192593856, 0.16317591116653482, 0.0, 0.37852230636979245, 0.018028311236297279, 0.92541657839832336, 0.0, 0.28584183121589524, 1.6245631663788398, 0.29900230020311369, 1.0] 
		M=Matrix()
		M.fromMaya(MMatrix)
		rotations= M.getRotation()
		result = [rotations[0].toDeg(),rotations[1].toDeg(),rotations[2].toDeg()]
		compare = [10.0,20.0,30.0]
		result = [float("%.1f"%result[0]),float("%.1f"%result[1]),float("%.1f"%result[2])]
		self.assertEqual(result,compare)
		
	def test_setRot(self):
		'''
		rotation set for matrix
		'''
		M=Matrix()
		rot=[10.0,20.0,-65.0]
		newM = M.setRotation(rot)
		rotations= newM.getRotation()
		#print('rotation',rotations)
		result = [rotations[0].toDeg(),rotations[1].toDeg(),rotations[2].toDeg()]
		result = [float("%.1f"%result[0]),float("%.1f"%result[1]),float("%.1f"%result[2])]
		self.assertEqual(result,rot)
		
	def test_setScale(self):
		'''
		scale set for matrix
		'''
		M=Matrix()
		scale=[10.0,20.0,65.0]
		newM = M.setScale(scale)
		sc = newM.getScale()
		#result = [float("%.1f"%sc[0]),float("%.1f"%sc[1]),float("%.1f"%sc[2])]
		self.assertEqual(sc,scale)
		
	def test_directAssigment(self):
		'''
		direct assignment of matrix element
		'''
		M=Matrix()
		chkValue = [[10, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
		M[0][0]=10
		self.assertEqual(M,chkValue)
		
		
		