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

__author__ = '$Author$'
__version__ = '$Revision$'
__date__ = '$Date$'
__id__= '$Id$'

#	ANGLE EXCEPTIONS 
class AngleError(Exception):
	'''
	exception handler for angle
	'''
	def __init__(self,value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)

#	ANGLE CLASS
class Angle(float):
	"""
	Angle class
	by default the angle is expressed as radians
	"""
	def __init__(self,ang):
		self._val=ang
		
		if isinstance(ang, int):
			self._val=float(ang)
			
		self._isDeg=False
		self._isRad=True
		return

	def __repr__(self):
		return repr(self._val)
	
	def __div__(self,other):
		
		if (isinstance(other, Angle)):		
			if self.isDeg() and other.isDeg():
				'''
				if bothe angles are degree
				'''
				return Angle(self._val / other._val).setAsDeg()
			
			if self.isRad() and other.isRad():
				'''
				if bothe angles are rad
				'''
				return Angle(self._val / other._val)			
			
			elif self.isDeg() and other.isRad():
				'''
				if the the first is in degree and the other is in radiants
				'''
				return Angle(self.toRad()._val / other._val)
				
			elif self.isRad() and other.isDeg():
				'''
				if the the first is in radiants and the other is in degree
				'''
				return Angle(self._val / other.toRad()._val)			
		
		if (isinstance(other, float)) or (isinstance(other, int)):
			'''
			sum with a float..
			'''
			if self.isDeg() :
				'''
				if the angle is in degree return degree
				'''
				val = self._val / float(other)
				return Angle(val).setAsDeg()
			
			elif self.isRad():
				'''
				if the angle is a radiats, return in radiants
				'''
				val = self._val / float(other)
				return Angle(val)	
				
	def __mul__(self,other):
		
		if (isinstance(other, Angle)):		
			if self.isDeg() and other.isDeg():
				'''
				if bothe angles are degree
				'''
				return Angle(self._val * other._val).setAsDeg()
			
			if self.isRad() and other.isRad():
				'''
				if bothe angles are rad
				'''
				return Angle(self._val * other._val)			
			
			elif self.isDeg() and other.isRad():
				'''
				if the the first is in degree and the other is in radiants
				'''
				return Angle(self.toRad()._val * other._val)
				
			elif self.isRad() and other.isDeg():
				'''
				if the the first is in radiants and the other is in degree
				'''
				return Angle(self._val * other.toRad()._val)			
		
		if (isinstance(other, float)) or (isinstance(other, int)):
			'''
			sum with a float..
			'''
			if self.isDeg() :
				'''
				if the angle is in degree return degree
				'''
				val = self._val * float(other)
				return Angle(val).setAsDeg()
			
			elif self.isRad():
				'''
				if the angle is a radiats, return in radiants
				'''
				val = self._val * float(other)
				return Angle(val)	
			
	def __sub__(self,other):
		
		if (isinstance(other, Angle)):		
			if self.isDeg() and other.isDeg():
				'''
				if bothe angles are degree
				'''
				return Angle(self._val - other._val).setAsDeg()
			
			if self.isRad() and other.isRad():
				'''
				if bothe angles are rad
				'''
				return Angle(self._val - other._val)			
			
			elif self.isDeg() and other.isRad():
				'''
				if the the first is in degree and the other is in radiants
				'''
				return Angle(self.toRad()._val - other._val)
				
			elif self.isRad() and other.isDeg():
				'''
				if the the first is in radiants and the other is in degree
				'''
				return Angle(self._val - other.toRad()._val)			
		
		if (isinstance(other, float)) or (isinstance(other, int)):
			'''
			sum with a float..
			'''
			if self.isDeg() :
				'''
				if the angle is in degree return degree
				'''
				val = self._val - float(other)
				return Angle(val).setAsDeg()
			
			elif self.isRad():
				'''
				if the angle is a radiats, return in radiants
				'''
				val = self._val - float(other)
				return Angle(val)	
	
	def __add__(self,other):
		
		if (isinstance(other, Angle)):		
			if self.isDeg() and other.isDeg():
				'''
				if bothe angles are degree
				'''
				return Angle(self._val + other._val).setAsDeg()
			
			if self.isRad() and other.isRad():
				'''
				if bothe angles are rad
				'''
				return Angle(self._val + other._val)	
							
			elif self.isDeg() and other.isRad():
				'''
				if the the first is in degree and the other is in radiants
				'''
				return Angle(self.toRad()._val + other._val)
				
			elif self.isRad() and other.isDeg():
				'''
				if the the first is in radiants and the other is in degree
				'''
				return Angle(self._val + other.toRad()._val)			
		
		if (isinstance(other, float)) or (isinstance(other, int)):
			'''
			sum with a float..
			'''
			if self.isDeg() :
				'''
				if the angle is in degree return degree
				'''
				val = self._val + float(other)
				return Angle(val).setAsDeg()
			
			elif self.isRad():
				'''
				if the angle is a radiats, return in radiants
				'''
				val = self._val + float(other)
				return Angle(val)
			
	def __eq__(self,other):
		if (isinstance(other, Angle)):		
			'''
			if we compare 2 angle types
			'''	
			if (self.isDeg() == other.isDeg()) or (self.isRad() == other.isRad()):
				'''
				if the angles are of the same type
				'''
				return (self._val == other._val)
			
			if self.isDeg() and other.isRad():
				'''
				if the the first is in degree and the other is in radiants
				'''
				return (self.toRad()._val == other._val)
				
			if self.isRad() and other.isDeg():
				'''
				if the the first is in radiants and the other is in degree
				'''
				return (self.toDeg()._val == other._val)
		
		if (isinstance(other, float)) or (isinstance(other, int)):
			'''
			compare with a float..
			'''
			return (self._val == float(other))

		
		else:
			return False
	
	def __ne__(self,other):
		if (isinstance(other, Angle)):		
			'''
			if we compare 2 angle types
			'''	
			if (self.isDeg() == other.isDeg()) or (self.isRad() == other.isRad()):
				'''
				if the angles are of the same type
				'''
				return (self._val != other._val)
			
			if self.isDeg() and other.isRad():
				'''
				if the the first is in degree and the other is in radiants
				'''
				return (self.toRad()._val != other._val)
				
			if self.isRad() and other.isDeg():
				'''
				if the the first is in radiants and the other is in degree
				'''
				return (self.toDeg()._val != other._val)
		
		if (isinstance(other, float)) or (isinstance(other, int)):
			'''
			compare with a float..
			'''
			return (self._val != float(other))

		
		else:
			return False
			
	def isDeg(self):
		'''
		check if the angle is expressed in degree
		'''
		return self._isDeg
	
	def isRad(self):
		'''
		check if the angle is expressed in radiants
		'''
		return self._isRad

	def setAsDeg(self):
		'''
		define the angle as expressed in degree
		'''
		self._isDeg=True
		self._isRad=False
		return self
		
	def toDeg(self):
		"""
		convert value to degree
		"""
		value = None
		
		if self.isDeg():
			#AngleError("value is already a Deg")
			value = self
			value._isRad=False
			value._isDeg=True
			
		else:
			value = Angle(math.degrees(self._val)).setAsDeg()
		return value

	def toRad(self):
		"""
		convert value to radians
		"""
		value = None
		
		if self.isRad():
			#AngleError("value is already a Rad")
			value = self
			value._isRad=True
			value._isDeg=False
			
		else:
			value = Angle(math.radians(self._val))
			value._isRad=True
			value._isDeg=False
			
		return value
