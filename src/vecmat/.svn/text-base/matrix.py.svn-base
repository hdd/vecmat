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

from __init__ import * #@UnusedWildImport
from vector import Vector as Vector
from angle import Angle as Angle

__author__ = '$Author$'
__version__ = '$Revision$'
__date__ = '$Date$'
__id__= '$Id$'

#	MATRIX EXCEPTIONS 
class MatrixError(Exception):
	'''
	exception handler for matrixes
	'''
	def __init__(self,value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)

#	MATRIX CLASS
class Matrix(Vector):
	"""
	Matrix class
	"""
	def __init__(self, vec=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]):
		newdata = []
		append=newdata.append
		if len(vec)==4:
			for v in vec:
				append(Vector(v))
			self.vec = newdata
		else:
			raise MatrixError("Matrix must be 4X4")
			
		return
	
	def __mul__(self,other):		
		if (isinstance(other, Matrix)):
			"""
			M*M
			"""
			tmpM=Matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
			
			T0=tmpM[0].vec
			T1=tmpM[1].vec
			T2=tmpM[2].vec
			T3=tmpM[3].vec
			
			T0[0]=self[0][0]* other[0][0] + self[0][1]* other[1][0] + self[0][2]* other[2][0] +self[0][3]* other[3][0] 
			T0[1]=self[0][0]* other[0][1] + self[0][1]* other[1][1] + self[0][2]* other[2][1] +self[0][3]* other[3][1] 
			T0[2]=self[0][0]* other[0][2] + self[0][1]* other[1][2] + self[0][2]* other[2][2] +self[0][3]* other[3][2] 
			T0[3]=self[0][0]* other[0][3] + self[0][1]* other[1][3] + self[0][2]* other[2][3] +self[0][3]* other[3][3] 
			
			T1[0]=self[1][0]* other[0][0] + self[1][1]* other[1][0] + self[1][2]* other[2][0] +self[1][3]* other[3][0] 
			T1[1]=self[1][0]* other[0][1] + self[1][1]* other[1][1] + self[1][2]* other[2][1] +self[1][3]* other[3][1] 
			T1[2]=self[1][0]* other[0][2] + self[1][1]* other[1][2] + self[1][2]* other[2][2] +self[1][3]* other[3][2] 
			T1[3]=self[1][0]* other[0][3] + self[1][1]* other[1][3] + self[1][2]* other[2][3] +self[1][3]* other[3][3] 
	
			T2[0]=self[2][0]* other[0][0] + self[2][1]* other[1][0] + self[2][2]* other[2][0] +self[2][3]* other[3][0] 
			T2[1]=self[2][0]* other[0][1] + self[2][1]* other[1][1] + self[2][2]* other[2][1] +self[2][3]* other[3][1] 
			T2[2]=self[2][0]* other[0][2] + self[2][1]* other[1][2] + self[2][2]* other[2][2] +self[2][3]* other[3][2] 
			T2[3]=self[2][0]* other[0][3] + self[2][1]* other[1][3] + self[2][2]* other[2][3] +self[2][3]* other[3][3] 
	
			T3[0]=self[3][0]* other[0][0] + self[3][1]* other[1][0] + self[3][2]* other[2][0] +self[3][3]* other[3][0] 
			T3[1]=self[3][0]* other[0][1] + self[3][1]* other[1][1] + self[3][2]* other[2][1] +self[3][3]* other[3][1] 
			T3[2]=self[3][0]* other[0][2] + self[3][1]* other[1][2] + self[3][2]* other[2][2] +self[3][3]* other[3][2] 
			T3[3]=self[3][0]* other[0][3] + self[3][1]* other[1][3] + self[3][2]* other[2][3] +self[3][3]* other[3][3] 
			return Matrix(tmpM)
		
		elif (isinstance(other, Vector)):
			"""
			M*V
			"""
			Mt=self.transpose()
			newX=0
			newY=0
			newZ=0
			
			if len(other.vec)==3:
				transVal=1
			else:
				transVal=other.vec[3]
				
			newX = (( other[0] * Mt[0][0]) +  ( other[1] * Mt[0][1]) + ( other[2] * Mt[0][2]) + ( transVal * Mt[0][3]))
			newY = (( other[0] * Mt[1][0]) +  ( other[1] * Mt[1][1]) + ( other[2] * Mt[1][2]) + ( transVal * Mt[1][3]))
			newZ = (( other[0] * Mt[2][0]) +  ( other[1] * Mt[2][1]) + ( other[2] * Mt[2][2]) + ( transVal * Mt[2][3]))
			w	= (( other[0] * Mt[3][0]) +  ( other[1] * Mt[3][1]) + ( other[2] * Mt[3][2]) + ( 1 * Mt[3][3]))
			
			if w != 0.0:
				newX = newX/w
				newY = newY/w  
				newZ = newZ/w
			
			newPoint = [newX, newY, newZ]
			return Vector(newPoint)	
			
	def getTranslation(self):
		"""
		get translate part of matrix
		"""
		return Vector(self.vec[-1][-4:-1])
	
	def getRotation(self):
		'''
		extract the rotation from the matrix
		'''
		scale = self.getScale()
		
		rotY = -math.asin(self[0][2]/scale[0])
		rotZ = math.atan2(self[0][1]/scale[0],self[0][0]/scale[0])
		rotX = math.atan2(self[1][2]/scale[1],self[2][2]/scale[2])
		
		return [Angle(rotX),Angle(rotY),Angle(rotZ)]
		
	def getScale(self):
		sx = math.sqrt(self[0][0]*self[0][0]+self[0][1]*self[0][1]+self[0][2]*self[0][2])
		sy = math.sqrt(self[1][0]*self[1][0]+self[1][1]*self[1][1]+self[1][2]*self[1][2])
		sz = math.sqrt(self[2][0]*self[2][0]+self[2][1]*self[2][1]+self[2][2]*self[2][2])
		
		return [sx,sy,sz]
		
	def setRotation(self,rot=[0.0,0.0,0.0],rotOrder="xyz"):
		outMatrix = Matrix() 
		s = self.getScale()
		trans = self.getTranslation()
		
		sx = math.sin(Angle(rot[0]).setAsDeg().toRad())
		sy = math.sin(Angle(rot[1]).setAsDeg().toRad())
		sz = math.sin(Angle(rot[2]).setAsDeg().toRad())
		cx = math.cos(Angle(rot[0]).setAsDeg().toRad())
		cy = math.cos(Angle(rot[1]).setAsDeg().toRad())
		cz = math.cos(Angle(rot[2]).setAsDeg().toRad())
		
		#rotation X
		RX = Matrix()
		RX[1][1] = cx
		RX[1][2] = sx
		RX[2][1] = -sx
		RX[2][2] = cx
		
		#rotation Y
		RY = Matrix()
		RY[0][0] = cy
		RY[0][2] = -sy
		RY[2][0] = sy
		RY[2][2] = cy
		
		#rotation Z
		RZ = Matrix()
		RZ[0][0] = cz
		RZ[0][1] = sz
		RZ[1][0] = -sz
		RZ[1][1] = cz
	
		#print('RZ',RZ)
		
		#Rotation matrix
		Rot = Matrix()
		rotMtx = {"x":RX, "y":RY, "z":RZ }
		Rot = rotMtx[rotOrder[0]]*rotMtx[rotOrder[1]]*rotMtx[rotOrder[2]]
		
		#Scale matrix
		Scale = Matrix()
		Scale[0][0] = s[0]
		Scale[1][1] = s[1]
		Scale[2][2] = s[2]
		
		
		if(s==[1.0,1.0,1.0]):
			outMatrix = Rot
		else:
			outMatrix = Scale*Rot

		outMatrix[3][0] = trans[0]
		outMatrix[3][1] = trans[1]
		outMatrix[3][2] = trans[2]
		
		self.vec = outMatrix
		return self
		
	def setTranslation(self,t=[0.0,0.0,0.0]):
		self[3].vec[0] = t[0]
		self[3].vec[1] = t[1]
		self[3].vec[2] = t[2]
		return
		
	def setScale(self,s=[1.0,1.0,1.0]):
		currScale = self.getScale()
		for j in range(0,3):
			for i in range(0,3):
				self[j].vec[i] = self[j][i]/currScale[j]
		
		Scale = Matrix()
		Scale[0].vec[0] = s[0]
		Scale[1].vec[1] = s[1]
		Scale[2].vec[2] = s[2]
		self = Scale*self
		return self
		

		
	def toMaya(self):
		"""
		convert Matrix to a valid maya matrix
		"""
		new=[]
		for n in self.vec:
			new+=n	
		return new	
	
	def fromMaya(self,MMatrix):
		"""
		convert a maya matrix to Matrix
		"""
		newdata = []
		append=newdata.append
		if len(MMatrix) == 16:
			for i in xrange(0,len(MMatrix),4):
				V=Vector([MMatrix[i],MMatrix[i+1],MMatrix[i+2],MMatrix[i+3]])
				append(V)
		self.vec=newdata
		return self
	
	def transpose(self):
		"""
		transpose matrix
		"""
		tmpM=Matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
		T0=tmpM[0].vec
		T1=tmpM[1].vec
		T2=tmpM[2].vec
		T3=tmpM[3].vec
		
		T0[0]=self[0][0]
		T0[1]=self[1][0]
		T0[2]=self[2][0]
		T0[3]=self[3][0]
		
		T1[0]=self[0][1]
		T1[1]=self[1][1]
		T1[2]=self[2][1]
		T1[3]=self[3][1]
		
		T2[0]=self[0][2]
		T2[1]=self[1][2]
		T2[2]=self[2][2]
		T2[3]=self[3][2]	
		
		T3[0]=self[0][3]
		T3[1]=self[1][3]
		T3[2]=self[2][3]
		T3[3]=self[3][3]
					
		return tmpM
		
		
	
	def inverse(self):
		"""
		inverse matrix
		"""
		m00 = self[0][0]
		m01 = self[0][1]
		m02 = self[0][2]
		m03 = self[0][3]
		m10 = self[1][0]
		m11 = self[1][1]
		m12 = self[1][2]
		m13 = self[1][3]
		m20 = self[2][0]
		m21 = self[2][1]
		m22 = self[2][2]
		m23 = self[2][3]
		m30 = self[3][0]
		m31 = self[3][1]
		m32 = self[3][2]
		m33 = self[3][3]

		v0 = m20 * m31 - m21 * m30;
		v1 = m20 * m32 - m22 * m30;
		v2 = m20 * m33 - m23 * m30;
		v3 = m21 * m32 - m22 * m31;
		v4 = m21 * m33 - m23 * m31;
		v5 = m22 * m33 - m23 * m32;

		t00 = + (v5 * m11 - v4 * m12 + v3 * m13);
		t10 = - (v5 * m10 - v2 * m12 + v1 * m13);
		t20 = + (v4 * m10 - v2 * m11 + v0 * m13);
		t30 = - (v3 * m10 - v1 * m11 + v0 * m12);

		invDet = 1 / (t00 * m00 + t10 * m01 + t20 * m02 + t30 * m03);

		d00 = t00 * invDet;
		d10 = t10 * invDet;
		d20 = t20 * invDet;
		d30 = t30 * invDet;

		d01 = - (v5 * m01 - v4 * m02 + v3 * m03) * invDet;
		d11 = + (v5 * m00 - v2 * m02 + v1 * m03) * invDet;
		d21 = - (v4 * m00 - v2 * m01 + v0 * m03) * invDet;
		d31 = + (v3 * m00 - v1 * m01 + v0 * m02) * invDet;

		v0 = m10 * m31 - m11 * m30;
		v1 = m10 * m32 - m12 * m30;
		v2 = m10 * m33 - m13 * m30;
		v3 = m11 * m32 - m12 * m31;
		v4 = m11 * m33 - m13 * m31;
		v5 = m12 * m33 - m13 * m32;

		d02 = + (v5 * m01 - v4 * m02 + v3 * m03) * invDet;
		d12 = - (v5 * m00 - v2 * m02 + v1 * m03) * invDet;
		d22 = + (v4 * m00 - v2 * m01 + v0 * m03) * invDet;
		d32 = - (v3 * m00 - v1 * m01 + v0 * m02) * invDet;

		v0 = m21 * m10 - m20 * m11;
		v1 = m22 * m10 - m20 * m12;
		v2 = m23 * m10 - m20 * m13;
		v3 = m22 * m11 - m21 * m12;
		v4 = m23 * m11 - m21 * m13;
		v5 = m23 * m12 - m22 * m13;
		
		d03 = - (v5 * m01 - v4 * m02 + v3 * m03) * invDet;
		d13 = + (v5 * m00 - v2 * m02 + v1 * m03) * invDet;
		d23 = - (v4 * m00 - v2 * m01 + v0 * m03) * invDet;
		d33 = + (v3 * m00 - v1 * m01 + v0 * m02) * invDet;
		
		return Matrix([[d00, d01, d02, d03],[d10, d11, d12, d13],[d20, d21, d22, d23],[d30, d31, d32, d33]])
	
	def mirror(self,axis=None,offset=Vector([0,0,0])):
		"""
		Mirror matrix on an axis , and offset 
		"""
		if axis != None:
			if axis == "x":
				axis=Vector([-1.0,1.0,1.0])
				offset=Vector([1.0,0.0,0.0])*offset
			elif axis == "y":
				axis=Vector([1.0,-1.0,1.0])
				offset=Vector([0.0,1.0,0.0])*offset
			elif axis == "z":
				axis=Vector([1.0,1.0,-1.0])
				offset=Vector([0.0,0.0,1.0])*offset
			else:
				raise MatrixError("error defining mirror axis")
						
			MirrorMatrix=Matrix([[axis[0],0.0,0.0,0.0],[0.0,axis[1],0.0,0.0],[0.0,0.0,axis[2],0.0],[offset[0],offset[1],offset[2],1.0]])
			OffsetMatrix=Matrix([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[offset[0],offset[1],offset[2],1.0]])
			return Matrix(self*MirrorMatrix*OffsetMatrix)
		else:
			return None