from LibraryOfEssentialFunctions import *

from VectorsClassNew import*
MAX_RUN_TIME = 120 #seconds
SMALLEST_TRIANGLE_SIZE = .001 #mas length of any side
MAX_TRIANGLE_COUNT = 50 #end search after this many applications of the Nelder-Mead algorithm
DOMAIN_LIMIT = 300 # 0 <= x <= DL and 0 <= y <= DL, DL = DOMAIN_LIMIT
def nextTriangle(A,B,C):#obtains a single point
#Case 0 Sort the vectors
	#print(A)
	[B,C,A] = Vector.sortReverse([A,B,C])#B.cost < A.cost < C.cost

	D = Vector(0,0)
	E = Vector(0,0)
	F = Vector(0,0)
	G = Vector(0,0)
	H = Vector(0,0)
	I = Vector(0,0)
	
	#NOTE:TRYING something out here: we cant have decimals, we need ints, so lets try rounding
	D.equals(B + C - A)
	E.equals(3 * (B + C) / 2 - 2 * A)
	F.equals((3 * (B + C) - 2 * A)/4)
	G.equals((2 * A + B + C) / 4)
	H.equals((A + B) / 2)
	I.equals((B + C)/ 2)
	
#Case 1 vertex A moves to D or E
	if D.costForMinimiziation() < A.costForMinimiziation():
		D.equals(B + C - A)
		A.equals(E)
#Case 2: Vertex A moves to F or G
	#print(A)

	if D.costForMinimiziation() == A.costForMinimiziation():
		F.equals((3 * (B + C) - 2 * A)/4)
		G.equals((2 * A + B + C) / 4)
		if F.costForMinimiziation() < G.costForMinimiziation():
			A.equals(F)
		else:
			A.equals(G)
#Case 3: vertex A moves to H and C moves to I
	if D.costForMinimiziation() > A.costForMinimiziation():
		A.equals(H)
		C.equals(I)
	return [A, B, C]
def triangleHasNotConverged(count, A, B, C): #Boolean result
	
	return not (A == B  or A == C or B == C) and clock() - START < MAX_RUN_TIME

from random import random
def threeRandomVectors(): #Domain is restricted for this problem
	#NOTE: it doesnt matter if the first nmuber is greater or less than the second one, the fitness function takes care of that #errorChekcing
	A = Vector(int(random() * DOMAIN_LIMIT), int(random() * DOMAIN_LIMIT))
	B = Vector(int(random() * DOMAIN_LIMIT), int(random() * DOMAIN_LIMIT))
	C = Vector(int(random() * DOMAIN_LIMIT), int(random() * DOMAIN_LIMIT))

	return [A, B, C]

def NelderMeadSearch():
	A, B, C = threeRandomVectors()
	#print(A, B, C)
	count = 0
	while triangleHasNotConverged(count, A, B, C):
		print(count)
		A, B, C = nextTriangle(A,B,C)
		count += 1
		print('results of iteration ', count, ' : ', A, B, C)
		print(clock() - START)
		
	bestCost = min(A.costForMinimiziation(), B.costForMinimiziation(), C.costForMinimiziation())
	if A.costForMinimiziation() == bestCost:
		return A
	elif B.costForMinimiziation() == bestCost:
		return B
	else:
		return C
	
	
	
	
def NelderMeadRandomResetBestResult():
	from time import clock
	startTime = clock()
	minCostVector = Vector(1, 2)
	minCost = 0
	while clock() - startTime < MAX_RUN_TIME:
		A = NelderMeadSearch()
		print(A)
		if A.costForMinimiziation() < minCost:
			minCostVector = A

		
	return minCostVector, abs(minCostVector.costForMinimiziation())

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i 
		i += step
		

	
#def main():
	#print('Search Results')
	#print('1. Nelder-Mead (random reset)\tcost =', "%4.4f" % round(NelderMeadRandomResetBestResult().cost(), 5))
	#print('2. Random (random reset)\tcost =', "%3.4f" % round(randomMethod().cost(), 5))
	#print('3. Random Grid\t\t\tcost =', "%3.4f" % round(RandomConstrainedByGridBestResultManyTimes().cost(), 5))	
	#print('4. Random Hill Climb\t\tcost =', "%3.4f" %round(HillClimbManyTimesRandom().cost(), 5))
	#print('5. Hill Climb Grid\t\tcost =', "%3.4f" % round(HillClimbBestResultGridManyTimes().cost(), 5))
	
#if __name__ == '__main__': main()
from time import clock;
def printElapsedTime():
	print( (clock() - START))

def runNelderMead(completeListOfCloses):
	print('Nelder-Mead')

	VectorsClassNew.completeListOfNumbers = completeListOfCloses[:]
	VectorsClassNew.useEntireArray = True
	
	from time import clock
	startTime = clock()
	minCostVector = Vector(1, 2)
	minCost = 0
	while clock() - startTime < MAX_RUN_TIME:
		A = NelderMeadSearch()
		print(A)
		if A.costForMinimiziation() < minCost:
			minCostVector = A

	print('And the min cost is: ', abs(minCostVector.costForMinimiziation()))
	return minCostVector

START = clock()
import VectorsClassNew
def main():
	
	#print('Hello')
	
	START = clock()
	
	#file1 = open ('DowData.txt', mode = 'r', encoding = 'utf 8')
	file1 = open('DowData1.txt', mode = 'r')
	file2 = open('Dates.txt', mode = 'r')
	#file1.write('P3' + ' ' + str(IMAGE_WIDTH) + ' ' + str(IMAGE_HEIGHT) + ' ' + str(255) + '\n')
	completeListOfCloses = []
	for line in file1:
		completeListOfCloses.append(float(line.strip()))
	
		
	file1.close()
	
	completeListOfDates = []
	for line in file2:
		completeListOfDates.append(line.strip())
	
	file2.close()
	
	#print(completeListOfDates)
	VectorsClassNew.completeListOfNumbers = completeListOfCloses[:]
	#print(VectorsClass.completeListOfNumbers)
	VectorsClassNew.useEntireArray = False
	A = Vector(84,17)
	print(A.costForMinimiziation())
	result = NelderMeadRandomResetBestResult()
	print('The max cost point is: ', result[0])
	print('The max cost of that point is: ', result[1]) 
	
	
if __name__ == '__main__': main()