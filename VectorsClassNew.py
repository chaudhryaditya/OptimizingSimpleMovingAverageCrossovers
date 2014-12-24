from LibraryOfEssentialFunctions import *

class Vector(object):
	completeListOfNumbers = []
	useEntireArray = False
	
	def __init__(self, *data):
		if type(data[0]) == Vector:
			self.data = list(data[0])
		else:
			self.data = list(data)
		
      
	def __repr__(self):
		return repr(tuple(self.data))
      
	def print(self, n = 2):
		print("Vector(", end ="")
		for j in range(len(self.data) - 1):
			print(round(self.data[j], n), end = ", ")
		print(round(self.data[j + 1], n), end = "")
		print(") ")
		return self
      
#Functions
	def length(self):
		return (len(self.data))
      
	def vectorList(self):
		return self.data
      
	def equals(self, other):
		self.data = []
		for num in other.vectorList()[:]:
			self.data.append(int(num))
		#self.data = map(int, other.vectorList())
		return tuple(self.data)
		
	
	def vecCost(x,y):
		from math import sin
		if (0 < x < 10) and (0 < y < 10):
			return (x * sin(4 * x) + 1.1 * y * sin(2 * y))
		return float('inf')
		
	def costForMinimiziation(self,startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5):
		#return -1 * functionF(self.data[0], self.data[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays) #NOTE: since nelder mead is a minimization function, we multiply the fitness by -1
																	#	in oder to flip the graph over the x-y plane
		if useEntireArray:
			longLength = self.data[1]
			if self.data[0] > self.data[1]:
				longLength = self.data[0]
			return -1 * functionF(self.data[0], self.data[1], completeListOfNumbers, 0, len(completeListOfNumbers) - longLength , xNumberOfDays) 
			
		else:
			longLength = self.data[1]
			if self.data[0] > self.data[1]:
				longLength = self.data[0]
			return -1 * functionF(self.data[0], self.data[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays)															
																		
	def costForMaximiziation(self,startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5):
		#print('yo i work')
		if useEntireArray:
			longLength = self.data[1]
			if self.data[0] > self.data[1]:
				longLength = self.data[0]
			return functionF(self.data[0], self.data[1], completeListOfNumbers, 0, len(completeListOfNumbers) - longLength , xNumberOfDays) 
			
		else:
			longLength = self.data[1]
			if self.data[0] > self.data[1]:
				longLength = self.data[0]
			return functionF(self.data[0], self.data[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays) 

	def dist(self, other):
		return (self - other).mag()
		
	def dotProd(self, other):
		return sum([self.data[j] * other.data[j] for j in range(len(self.data))])
		
	def crossProd(X, Y):
		return Vector (X.data[1] * Y.data[2] - X.data[2] * Y.data[1], \
				X.data[2] * Y.data[0] - X.data[0] * Y.data[2], \
				X.data[0] * Y.data[1] - X.data[1] * Y.data[0])
				
	def mag(self):
		from math import sqrt
		return sqrt(sum([j * j for j in self.data]))
		
	def normalize(self):
		m = self.mag()
		self.data = (self / m).data
		return self
	
	def swap (A, B):
		T = Vector(0)
		T.equals(A)
		A.equals(B)
		B.equals(T)
		
	def sort(vectorList,startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5):
		if type(vectorList) != list:
			exit('Error: The sort function limitedto a list of Vector elements')
		vectorList.sort(key = Vector.costForMaximiziation, reverse = True)
		#vectorList.sort(key = self.costForMaximiziation(startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5), reverse = True)
		return vectorList
	
	def sortReverse(vectorList):
		if type(vectorList) != list or len(vectorList) != 3 or type(vectorList[0]) != Vector\
				or type(vectorList[1]) != Vector or type(vectorList[2]) != Vector:
			exit('Error: The sort function limitedto a list of three Vector elements')
		vectorList.sort(key = Vector.costForMinimiziation)
		return vectorList
		
#Operators  
	def __add__(self, other):
		return Vector(*[self.data[j] + other.data[j] for j in range(len(self.data))])
		
	def __sub__(self, other):
		return -other + self
		
	def __mul__(self, entity):
		if isinstance(entity, (Vector)):
			return self.crossProd(entity)
		if isinstance(entity, (int, float)):
			return Vector(*[j * entity for j in (self.data)])
		return NotImplemented
		
	def __rmul__(self, num):
		return self*num
		
	def __truediv__(self, num):
		if num == 0: return NotImplemented
		return self*(1.0/num)
		
	def __eq__(self, other):
		return(self.data == other.data)
	
	def __ne__(self, other):
		return not(self.data == other.data)
		
	def __neg__(self):
		return Vector(*[-j for j in self.data])
		
	def __getitem__(self, index):
		return self.data[index]
		
	def __setitem__(self, index, num):
		self.data[index] = num
		return self
	
#def main():
	##Chech to see if code works
	#A = Vector (1,2,3)
	#B = Vector (4,5,6)
	#print(' 1.', A+B)
	#print(' 2.', (A+B).mag())
	#print(' 3.', A.dist(B))
	#print(' 4.', A.dotProd(B))
	#print(' 5.', A.crossProd(B))
	#print(' 6.', A.normalize().mag())
	#print(' 7.', A-B)
	#print(' 8.', 2 * A)
	#print(' 9.', A * 2)
	#print(' 10.', A / 2)
	#A[0] = 100.1234
	#print(' 11.', A)
	#print(' 12.', end = '')
	#A.print()
	#print(' 13.', end = '')
	#A.print(3)
	#print(' 14.', B.cost())
	#print(' 15.', B.cost)
	#C = Vector (9, 8)
	#D = Vector (0, 1, 2, 3)
	#print(' 16.', D.equals(C))
	#print(' 17.', D)
		
#if __name__== '__main__': main()
	
		