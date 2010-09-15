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


from vecmat.matrix import Matrix
from vecmat.vector import Vector

def mulMatVec():
	m1=Matrix()
	v1=Vector([1,2,3])
	m1*v1
	
def mulMat():
	m1=Matrix()
	m2=Matrix()
	m1*m2
	
def inverseMat():
	m1= Matrix([[2,2,1,1],[1,2,3,1],[1,2,1,3],[7,1,3,4]])
	m1.inverse()
	
def trasposeMat():
	m1= Matrix([[2,2,1,1],[1,2,3,1],[1,2,1,3],[7,1,3,4]])
	m1.transpose()
	
	
		