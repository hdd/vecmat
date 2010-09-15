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


ITERATIONS=100000
import os
from datetime import datetime
import timeit

def __testInformations():
	print "TEST INFORMATION:"
	print "-"*100
	print "DATE %s "%datetime.now()
	print "%s ITERATION/s"%ITERATIONS
	systemInfo = os.uname()
	print "PLATFORM %s-%s"%(systemInfo[0],systemInfo[-1])	
	print "-"*100

#	ANGLE FUNCTIONS 	
def angleSpeed():
	print "angle sumRad : %s"%timeit.Timer("sumRad()","from angleSpeedTest import sumRad").timeit(ITERATIONS)	
	print "angle sumDeg : %s"%timeit.Timer("sumDeg()","from angleSpeedTest import sumDeg").timeit(ITERATIONS)
	print "angle sumDegRad : %s"%timeit.Timer("sumDegRad()","from angleSpeedTest import sumDegRad").timeit(ITERATIONS)
	print "angle sumRadDeg : %s"%timeit.Timer("sumRadDeg()","from angleSpeedTest import sumRadDeg").timeit(ITERATIONS)
	print "angle sumDegFloat : %s"%timeit.Timer("sumDegFloat()","from angleSpeedTest import sumDegFloat").timeit(ITERATIONS)
	print "angle sumRadFloat : %s"%timeit.Timer("sumRadFloat()","from angleSpeedTest import sumRadFloat").timeit(ITERATIONS)	
	
	print "angle subRad : %s"%timeit.Timer("subRad()","from angleSpeedTest import subRad").timeit(ITERATIONS)	
	print "angle subDeg : %s"%timeit.Timer("subDeg()","from angleSpeedTest import subDeg").timeit(ITERATIONS)
	print "angle subDegRad : %s"%timeit.Timer("subDegRad()","from angleSpeedTest import subDegRad").timeit(ITERATIONS)
	print "angle subRadDeg : %s"%timeit.Timer("subRadDeg()","from angleSpeedTest import subRadDeg").timeit(ITERATIONS)
	print "angle subDegFloat : %s"%timeit.Timer("subDegFloat()","from angleSpeedTest import subDegFloat").timeit(ITERATIONS)
	print "angle subRadFloat : %s"%timeit.Timer("subRadFloat()","from angleSpeedTest import subRadFloat").timeit(ITERATIONS)	

	print "angle mulRad : %s"%timeit.Timer("mulRad()","from angleSpeedTest import mulRad").timeit(ITERATIONS)	
	print "angle mulDeg : %s"%timeit.Timer("mulDeg()","from angleSpeedTest import mulDeg").timeit(ITERATIONS)
	print "angle mulDegRad : %s"%timeit.Timer("mulDegRad()","from angleSpeedTest import mulDegRad").timeit(ITERATIONS)
	print "angle mulRadDeg : %s"%timeit.Timer("mulRadDeg()","from angleSpeedTest import mulRadDeg").timeit(ITERATIONS)
	print "angle mulDegFloat : %s"%timeit.Timer("mulDegFloat()","from angleSpeedTest import mulDegFloat").timeit(ITERATIONS)
	print "angle mulRadFloat : %s"%timeit.Timer("mulRadFloat()","from angleSpeedTest import mulRadFloat").timeit(ITERATIONS)	
	
	print "angle divRad : %s"%timeit.Timer("divRad()","from angleSpeedTest import divRad").timeit(ITERATIONS)	
	print "angle divDeg : %s"%timeit.Timer("divDeg()","from angleSpeedTest import divDeg").timeit(ITERATIONS)
	print "angle divDegRad : %s"%timeit.Timer("divDegRad()","from angleSpeedTest import divDegRad").timeit(ITERATIONS)
	print "angle divRadDeg : %s"%timeit.Timer("divRadDeg()","from angleSpeedTest import divRadDeg").timeit(ITERATIONS)
	print "angle divDegFloat : %s"%timeit.Timer("divDegFloat()","from angleSpeedTest import divDegFloat").timeit(ITERATIONS)
	print "angle divRadFloat : %s"%timeit.Timer("divRadFloat()","from angleSpeedTest import divRadFloat").timeit(ITERATIONS)	
	
	print "angle cmpareFloat : %s"%timeit.Timer("compareFloat()","from angleSpeedTest import compareFloat").timeit(ITERATIONS)	
	print "angle cmpareInt : %s"%timeit.Timer("compareInt()","from angleSpeedTest import compareInt").timeit(ITERATIONS)	
	print "angle cmpareRad : %s"%timeit.Timer("compareRad()","from angleSpeedTest import compareRad").timeit(ITERATIONS)	
	print "angle cmpareDeg : %s"%timeit.Timer("compareDeg()","from angleSpeedTest import compareDeg").timeit(ITERATIONS)	

def vectorSpeed():
	print "vector sumVec : %s"%timeit.Timer("sumVec()","from vectorSpeedTest import sumVec").timeit(ITERATIONS)
		
	print "vector subVec : %s"%timeit.Timer("subVec()","from vectorSpeedTest import subVec").timeit(ITERATIONS)	
	
	print "vector mulVecFloat : %s"%timeit.Timer("mulVecFloat()","from vectorSpeedTest import mulVecFloat").timeit(ITERATIONS)	
	print "vector mulVecInt : %s"%timeit.Timer("mulVecInt()","from vectorSpeedTest import mulVecInt").timeit(ITERATIONS)	

	print "vector divVecFloat : %s"%timeit.Timer("divVecFloat()","from vectorSpeedTest import divVecFloat").timeit(ITERATIONS)	
	print "vector divVecInt : %s"%timeit.Timer("divVecInt()","from vectorSpeedTest import divVecInt").timeit(ITERATIONS)	
	
	print "vector dotVec : %s"%timeit.Timer("dotVec()","from vectorSpeedTest import dotVec").timeit(ITERATIONS)	
	print "vector crossVec : %s"%timeit.Timer("crossVec()","from vectorSpeedTest import crossVec").timeit(ITERATIONS)	
	print "vector normVec : %s"%timeit.Timer("normVec()","from vectorSpeedTest import normVec").timeit(ITERATIONS)	
	print "vector angleBetweenVec : %s"%timeit.Timer("angleBetweenVec()","from vectorSpeedTest import angleBetweenVec").timeit(ITERATIONS)	


def matrixSpeed():
	print "matrix mulMat : %s"%timeit.Timer("mulMat()","from matrixSpeedTest import mulMat").timeit(ITERATIONS)	
	print "matrix mulMatVec : %s"%timeit.Timer("mulMatVec()","from matrixSpeedTest import mulMatVec").timeit(ITERATIONS)	
	print "matrix inverseMat : %s"%timeit.Timer("inverseMat()","from matrixSpeedTest import inverseMat").timeit(ITERATIONS)		
	print "matrix trasposeMat : %s"%timeit.Timer("trasposeMat()","from matrixSpeedTest import trasposeMat").timeit(ITERATIONS)		
		
def real_main():
	__testInformations()
	angleSpeed()
	vectorSpeed()
	matrixSpeed()
	
def profile_main():
    # This is the main function for profiling
    # We've renamed our original main() above to real_main()
    import cProfile, pstats
    prof = cProfile.Profile()
    prof = prof.runctx("real_main()", globals(), locals())
    print "<pre>"
    stats = pstats.Stats(prof)
    stats.sort_stats("time")  # Or cumulative
    stats.print_stats(80)  # 80 = how many to print
    # The rest is optional.
    # stats.print_callees()
    # stats.print_callers()
    print "</pre>"


if __name__ == "__main__":
	real_main()