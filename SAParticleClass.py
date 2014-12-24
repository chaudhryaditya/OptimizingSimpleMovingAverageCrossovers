from LibraryOfEssentialFunctions import *
from VectorsClassNew import *
import VectorsClassNew 

class SAParticle(object):
	completeListOfNumbers = []
	useEntireArray = False
	bestPointForAllParticles = Vector(0,0,0)
	bestPointForAllParticlesFitness = 0

	constantWeightFactor1 = 0	# [1.5, 2]
	constantWeightFactor2 = 0	# [2, 2.5]
	inertiaWeight = 0	# [.4, 1.4]
	listOfParticles = []
	listOfFitnesses = []
	
	def __init__(self, initialPostitionX, initialPostitionY, initialVelocityX, initialVelocityY):
		#if type(data[0]) == Vector:
			#self.data = list(data[0])
		#else:
			#self.data = list(data)
		self.currentPosition = Vector(initialPostitionX, initialPostitionY)
		#print('yo', self.currentPosition)
		#self.currentPositionRounded = Vector(initialPostitionX, initialPostitionY)
		
		#for i in range(len(self.currentPosition.data)):	#We need integer coordinates
			#self.currentPositionRounded.data[i] = round(self.currentPositionRounded.data[i])

		#print('yo1', self.currentPosition)

		
		#self.velocity = Vector(initialVelocityX, initialVelocityY)
		#self.bestPointForThisParticle = self.currentPosition
		#print(self.currentPosition)
		#self.fitness = self.currentPositionRounded.costForMinimiziation()
		self.fitness = self.currentPosition.costForMinimiziation()
		self.bestPointForThisParticleFitness = self.fitness
		
		
		
	def __repr__(self):
	
		#return repr(tuple((self.currentPositionRounded.data, self.velocity, self.bestPointForThisParticle)))
		return repr(self.currentPosition.data)
	def print(self, n = 2):
		print("Particle(", end ="")
		for j in range(len(self.currentPosition.data) - 1):
			print(round(self.currentPosition.data[j], n), end = ", ")
		print(round(self.data[j + 1], n), end = "")
		print(") ")
		return self
      
#Functions
	def length(self):
		return (len(self.currentPosition.data))
      
	#def vectorList(self):
		#return self.data
      
	#def equals(self, other):
		#self.data = []
		#for num in other.vectorList()[:]:
			#self.data.append(int(num))
		##self.data = map(int, other.vectorList())
		#return tuple(self.data)
		
	
	#def vecCost(x,y):
		#from math import sin
		#if (0 < x < 10) and (0 < y < 10):
			#return (x * sin(4 * x) + 1.1 * y * sin(2 * y))
		#return float('inf')
	
		#NOTE
		#NOTE
		#NOTE
		#NOTE
		#NOTE
		#NOTE
		#NOTE
		#NOTE
		#NOTE: PSO needs the minimization function
	def costForMinimization(self,startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5):
	
		#return self.currentPosition.costForMinimiziation()	
		
		#return self.currentPositionRounded.costForMinimiziation()
	
		return self.currentPosition.costForMinimiziation()
	
		#	in oder to flip the graph over the x-y plane
		#if useEntireArray:
			#longLength = self.data[1]
			#if self.data[0] > self.data[1]:
				#longLength = self.data[0]
			#return -1 * functionF(self.data[0], self.data[1], completeListOfNumbers, 0, len(completeListOfNumbers) - longLength , xNumberOfDays) 
			
		#else:
			#longLength = self.data[1]
			#if self.data[0] > self.data[1]:
				#longLength = self.data[0]
			#return -1 * functionF(self.data[0], self.data[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays)															
																		
	#def costForMaximiziation(self,startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5):
		##print('yo i work')
		##if useEntireArray:
			##longLength = self.data[1]
			##if self.data[0] > self.data[1]:
				##longLength = self.data[0]
			##return functionF(self.data[0], self.data[1], completeListOfNumbers, 0, len(completeListOfNumbers) - longLength , xNumberOfDays) 
			
		##else:
			##longLength = self.data[1]
			##if self.data[0] > self.data[1]:
				##longLength = self.data[0]
			##return functionF(self.data[0], self.data[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays) 
			#return self.currentPosition.costForMaximiziation()

	#def updateVelocity(self):
		#from random import random
		#randomFactor1 = random()
		#randomFactor2 = random()
		
		##if self.fitness < bestPointForAllParticles.costForMinimiziation():
			##import sys
			##print('NOT WORKING', self.fitness)
			##sys.exit()
		#myInertiaWeight = (1.1 - self.fitness / bestPointForAllParticlesFitness) * inertiaWeight
		#myConstantWeightFactor1 = (1.1 - self.fitness / bestPointForAllParticlesFitness) * constantWeightFactor1
		#myConstantWeightFactor2 = (1.1 - self.fitness / bestPointForAllParticlesFitness) * constantWeightFactor2

		##myInertiaWeight =  inertiaWeight
		##myConstantWeightFactor1 =  constantWeightFactor1
		##myConstantWeightFactor2 = constantWeightFactor2
		
		#newVelocityForThisParticle = myInertiaWeight * self.velocity + myConstantWeightFactor1 * randomFactor1 *  (self.bestPointForThisParticle - self.currentPosition)\
								#+ myConstantWeightFactor2 * randomFactor2 *(bestPointForAllParticles - self.currentPosition)
							
							
		##NOTE: FULLY INFORMED PSO:
		##newVelocityForThisParticle = myInertiaWeight * self.velocity + myConstantWeightFactor1 * randomFactor1 *  (self.bestPointForThisParticle - self.currentPosition)
		
		
		##sumOfFitnesses = 0
		##for fitness in listOfFitnesses:
			##if not fitness == 1:
				##sumOfFitnesses += fitness
		
		###print('sumOfFitnesses,', sumOfFitnesses)
			
		##for i in range(len(listOfParticles)):
			##relativeFitness = listOfFitnesses[i] / sumOfFitnesses 
			###print(relativeFitness)
			##newVelocityForThisParticle +=  relativeFitness\
				##* myConstantWeightFactor2 * randomFactor2 *(listOfParticles[i].currentPosition - self.currentPosition)
		
							
							
		##if newVelocityForThisParticle.data[0] > 10000:
			##import sys
			##print('NOT WORKING VELOCITY', newVelocityForThisParticle, self)
			##sys.exit()
		##print('Random factors: ', randomFactor1, randomFactor2)
		##print('term 1: ', inertiaWeight * self.velocity)
		##print('term 2: ', constantWeightFactor1 * randomFactor1 *  (self.bestPointForThisParticle - self.currentPosition))
		##print('constantWeightFactor2: ', constantWeightFactor2)
		##print('bestPointForAllParticles: ', bestPointForAllParticles)
		##print('term 3: ', constantWeightFactor2 * randomFactor2 *(bestPointForAllParticles - self.currentPosition))

		#self.velocity = newVelocityForThisParticle
		
	def updatePosition(self, temperature):
	
		#newPositionForThisParticle = self.currentPosition + self.velocity
		#for i in range(len(newPositionForThisParticle.data)):	#We need integer coordinates
			#newPositionForThisParticle.data[i] = round(newPositionForThisParticle.data[i])
		
		#newFitness = newPositionForThisParticle.costForMinimiziation()
		##NOTE: If this doesnt work, try not updating the currentPosition unless newPositionForThisParticle is better
		#if newFitness < self.bestPointForThisParticleFitness:
			#self.bestPointForThisParticle = newPositionForThisParticle
			##print('best position for this particle has changed')
		
		##if newPositionForThisParticle.data[0] > 10000:
			##import sys
			##print('NOT WORKING POSITION', newPositionForThisParticle, self)
			##sys.exit()
		
		#self.fitness = newFitness
		#self.currentPosition = newPositionForThisParticle
		
		
		#rowAdjustment = {-1,0,1}
		#columnAdjustment = {-1, 0, 1}
		
		if temperature == 0:
			return
		from random import randint, random
		vectorToAddToXAndY = [-1,1]
		addToGetNewPosition = Vector(vectorToAddToXAndY[randint(0,1)], vectorToAddToXAndY[randint(0,1)])
		
		newPositionForThisParticle = self.currentPosition + addToGetNewPosition
		#newPositionForThisParticleRounded = self.currentPosition + self.velocity
		#for i in range(len(newPositionForThisParticleRounded.data)):	#We need integer coordinates
		for i in range(len(newPositionForThisParticle.data)):	#We need integer coordinates
			#newPositionForThisParticleRounded.data[i] = round(newPositionForThisParticleRounded.data[i])
			newPositionForThisParticle.data[i] = round(newPositionForThisParticle.data[i])

		#newFitness = newPositionForThisParticleRounded.costForMinimiziation()
		newFitness = newPositionForThisParticle.costForMinimiziation()
		
		#NOTE:EXPONENTIAL PROBABILITY THING
		from math import exp
		
		cutOffProbability = min(1, abs( exp(-(newFitness - self.fitness)/temperature)) )
		#print(exp(-(newFitness - self.fitness)/temperature)))
		
		
		if newFitness < self.fitness:	#If the new point is better, we're good
			self.fitness = newFitness
			self.currentPosition = newPositionForThisParticle
			
		
		
		elif random() < cutOffProbability:	#If the new point is worse, still accept it with probability of e^-(newFitness - oldFitness)/temperature
			#print(newFitness, self.fitness, temperature, abs((-(newFitness - self.fitness)/temperature)))

			self.fitness = newFitness
			self.currentPosition = newPositionForThisParticle

		#NOTE: If this doesnt work, try not updating the currentPosition unless newPositionForThisParticle is better
		#if newFitness < self.bestPointForThisParticleFitness:
			##self.bestPointForThisParticle = newPositionForThisParticleRounded
			#self.bestPointForThisParticle = newPositionForThisParticle
			
		
			
			#print('best position for this particle has changed')
		
		#if newPositionForThisParticle.data[0] > 10000:
			#import sys
			#print('NOT WORKING POSITION', newPositionForThisParticle, self)
			#sys.exit()
		
		#self.fitness = newFitness
		#self.currentPosition = newPositionForThisParticle
		#self.currentPositionRounded = newPositionForThisParticleRounded
		
		
		
		 
		
		
		
		
	#def dist(self, other):
		#return (self - other).mag()
		
	#def dotProd(self, other):
		#return sum([self.data[j] * other.data[j] for j in range(len(self.data))])
		
	#def crossProd(X, Y):
		#return Vector (X.data[1] * Y.data[2] - X.data[2] * Y.data[1], \
				#X.data[2] * Y.data[0] - X.data[0] * Y.data[2], \
				#X.data[0] * Y.data[1] - X.data[1] * Y.data[0])
				
	#def mag(self):
		#from math import sqrt
		#return sqrt(sum([j * j for j in self.data]))
		
	#def normalize(self):
		#m = self.mag()
		#self.data = (self / m).data
		#return self
	
	#def swap (A, B):
		#T = Vector(0)
		#T.equals(A)
		#A.equals(B)
		#B.equals(T)
		
	#def sort(vectorList,startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5):
		#if type(vectorList) != list:
			#exit('Error: The sort function limitedto a list of Vector elements')
		#vectorList.sort(key = Vector.costForMaximiziation, reverse = True)
		##vectorList.sort(key = self.costForMaximiziation(startDateIndex = 0, endDateIndex = 10000, xNumberOfDays = 5), reverse = True)
		#return vectorList
	
	#def sortReverse(vectorList):
		#if type(vectorList) != list or len(vectorList) != 3 or type(vectorList[0]) != Vector\
				#or type(vectorList[1]) != Vector or type(vectorList[2]) != Vector:
			#exit('Error: The sort function limitedto a list of three Vector elements')
		#vectorList.sort(key = Vector.costForMinimiziation)
		#return vectorList
		
#Operators  
	def __add__(self, other):
		return Vector(*[self.currentPosition.data[j] + other.currentPosition.data[j] for j in range(len(self.currentPosition.data))])
		
	def __sub__(self, other):
		return -other + self
		
	#def __mul__(self, entity):
		#if isinstance(entity, (Vector)):
			#return self.crossProd(entity)
		#if isinstance(entity, (int, float)):
			#return Vector(*[j * entity for j in (self.data)])
		#return NotImplemented
		
	#def __rmul__(self, num):
		#return self*num
		
	#def __truediv__(self, num):
		#if num == 0: return NotImplemented
		#return self*(1.0/num)
		
	def __eq__(self, other):
		return(self.currentPosition.data == other.currentPosition.data)
	
	def __ne__(self, other):
		return not(self.currentPosition.data == other.currentPosition.data)
		
	def __neg__(self):
		return Vector(*[-j for j in self.currentPosition.data])
		
	def __getitem__(self, index):
		return self.currentPosition.data[index]
		
	def __setitem__(self, index, num):
		self.currentPosition.data[index] = num
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
	
		