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

from unit.vectorUnitTest import VectorUnitTest
from unit.angleUnitTest import AngleUnitTest
from unit.matrixUnitTest import MatrixUnitTest

if __name__ == '__main__':
	
	angleSuite = unittest.TestLoader().loadTestsFromTestCase(AngleUnitTest)
	unittest.TextTestRunner(verbosity=3).run(angleSuite)
	
	vectorSuite = unittest.TestLoader().loadTestsFromTestCase(VectorUnitTest)
	unittest.TextTestRunner(verbosity=3).run(vectorSuite)
	
	matrixSuite = unittest.TestLoader().loadTestsFromTestCase(MatrixUnitTest)
	unittest.TextTestRunner(verbosity=3).run(matrixSuite)