
from LibraryOfEssentialFunctions import *
from VectorsClassNew import *
from SAParticleClass import *
import VectorsClassNew 
import SAParticleClass

from matplotlib import *

MAX_RUN_TIME = 120 #seconds
MAX_TRIANGLE_COUNT = 50 #end search after this many applications of the Nelder-Mead algorithm
DOMAIN_LIMIT = 300 # 0 <= x <= DL and 0 <= y <= DL, DL = DOMAIN_LIMIT

	

#GLOBAL CONSTANTS
MAX = 2
POP = 36	# [15, 30]

def display(particles):
	print('-------Particles-------')
	for i in range(len(particles)):
		print(i, particles[i], particles[i].fitness)
	print('-------------------------')

def createListOfParticles():
	particles = []
	[particles.append(createParticle(MAX)) for i in range(POP)]
	#print('yo', chroms)
	return particles[:]
	
def createListOfParticlesEquallyDistributed():
	import math
	from random import random
	particles = []

	for x in range(0, DOMAIN_LIMIT, DOMAIN_LIMIT//int(math.sqrt(POP))):
		for y in range(0, DOMAIN_LIMIT, DOMAIN_LIMIT//int(math.sqrt(POP))):
			initialX = x
			initialY = y
			
			if initialX == 0:
				initialX += 2
				
			if initialY == 0:
				initialY += 2
				
			if initialX == initialY:
				initialY += 1
			#particles.append(Particle(initialX, initialY, random() * 5 + 3, random() * 5 + 3))	#initial locations are fixed; initial velocities are random; 
			particles.append(SAParticle(initialX, initialY, random() * 0 , random() * 0 ))	
	#[particles.append(createParticle(MAX)) for i in range(POP)]
	#print('yo', chroms)

	print(len(particles))
	return particles[:]

def createListOfParticlesEquallyDistributedTriangle():
	import math
	from random import random
	particles = []
	
	yFactor = 1

	particles.append(SAParticle(2, 3, random() * 0 , random() * 0 ))
	
	
	
	for x in range(2, DOMAIN_LIMIT, DOMAIN_LIMIT//7):
		#print('yFactor is: ', yFactor)

		for y in range(2, x, (x )//yFactor):
			#print(y,x)
			initialX = y
			initialY = x
			
			if initialX == 0:
				initialX += 2
				
			if initialY == 0:
				initialY += 2
				
			if initialX == initialY:
				initialY += 1
			#particles.append(Particle(initialX, initialY, random() * 5 + 3, random() * 5 + 3))	#initial locations are fixed; initial velocities are random; 
			particles.append(SAParticle(initialX, initialY,0, 0))	
			
		yFactor += 1
	#[particles.append(createParticle(MAX)) for i in range(POP)]
	#print('yo', chroms)

	print(len(particles))
	return particles[:]	
	
	
def createListOfParticlesEquallyDistributedInQuadrants():
	import math
	from random import random
	particles = []
	xHalves = [0, DOMAIN_LIMIT//2]
	yHalves = [0, DOMAIN_LIMIT//2]

	for xHalf in xHalves:	#NOTE: 6 particles in each fourth of the search space, last one is completly random
		for yHalf in yHalves:
			for i in range(6):
				initialX = xHalf + random() * (DOMAIN_LIMIT//2)
				initialY = yHalf + random() * (DOMAIN_LIMIT//2)
				
				if initialX == 0:
					initialX += 2
					
				if initialY == 0:
					initialY += 2
					
				if initialX == initialY:
					initialY += 1
				particles.append(Particle(int(initialX), int(initialY), random() * 5 + 3, random() * 5 + 3))	#initial locations are fixed; initial velocities are random;
				
	particles.append(SAParticle(int(random() * DOMAIN_LIMIT), int(random() * DOMAIN_LIMIT), random() * 5 + 3, random() * 5 + 3))
	print(len(particles))
	return particles[:]
	
def createListOfParticlesRadialSquares():
	import math
	from random import random
	particles = []
	divs = [DOMAIN_LIMIT//5 * 2 - 2, DOMAIN_LIMIT//5 * 3 - 2, DOMAIN_LIMIT//5 * 4 - 2, DOMAIN_LIMIT//5 * 5 - 2]
	yDivs = [DOMAIN_LIMIT//5 * 2 - 2, DOMAIN_LIMIT//5 * 3 - 2, DOMAIN_LIMIT//5 * 4 - 2, DOMAIN_LIMIT//5 * 5 - 2]
	
	particles.append(SAParticle(int(random() * 8 + 2), int(random() * 8 + 2), random() * 5 + 3, random() * 5 + 3)) #Two particles within (10, 10)
	particles.append(SAParticle(int(random() * 8 + 2), int(random() * 8 + 2), random() * 5 + 3, random() * 5 + 3))
	
	particles.append(SAParticle(int(random() * (DOMAIN_LIMIT//5 - 2) + 2), int(random() * (DOMAIN_LIMIT//5 - 2) + 2), random() * 5 + 3, random() * 5 + 3)) #Three  particles within (60, 60)
	particles.append(SAParticle(int(random() * (DOMAIN_LIMIT//5 - 2) + 2), int(random() * (DOMAIN_LIMIT//5 - 2) + 2), random() * 5 + 3, random() * 5 + 3))
	particles.append(SAParticle(int(random() * (DOMAIN_LIMIT//5 - 2) + 2), int(random() * (DOMAIN_LIMIT//5 - 2) + 2), random() * 5 + 3, random() * 5 + 3)) 
	
		
	for div in divs:	#NOTE: 5 particles in each square with side legnth of a multiple of 60 of the search space
		for i in range(5):
			initialX = int(random() * div + 2)
			initialY = int(random() * div + 2)
			
			if initialX == 0:
				initialX += 2
				
			if initialY == 0:
				initialY += 2
				
			if initialX == initialY:
				initialY += 1
			particles.append(Particle(initialX, initialY, random() * 5 + 3, random() * 5 + 3))	#initial locations are fixed; initial velocities are random;
				
	print(len(particles))
	return particles[:]
def createParticle(numberOfParameters):
	from random import randint, random
	
	initialX = int(random() * DOMAIN_LIMIT)
	#initialY = int(random() * DOMAIN_LIMIT)
	
	if initialX > initialY:
		initialX, initialY = initialY , initialX
		
	p = SAParticle(initialX, initialY, random() * 5 + 3, random() * 5 + 3)	#initial locations are random; initial velocities are random

	return p

def findBestParticle(listOfParticles):
	
	indexOfBestParticle = 0
	fitnessOfBestParticle = listOfParticles[0].fitness
	
	for i in range(len(listOfParticles)):
		fitnessOfThisParticle = listOfParticles[i].fitness
		#if listOfParticles[i].currentPosition.data[0] > 1000:
			#import sys
			#print('NOT WORKING POSITION', i, listOfParticles[i])
			#sys.exit()
		if fitnessOfThisParticle < fitnessOfBestParticle:	#Yes, minimization
			indexOfBestParticle = i
			fitnessOfBestParticle = fitnessOfThisParticle
			#print('the new best fitness is: ', fitnessOfBestParticle, indexOfBestParticle)
			
			
	#bestParticle = listOfParticles[0]
	#for i in range(len(listOfParticles)):
		#if listOfParticles[i].costForMinimization() < bestParticle.costForMinimization():	#Yes, minimization
			#bestParticle = listOfParticles[i]
	
	#print(indexOfBestParticle)
	return listOfParticles[indexOfBestParticle]
			
			
def updateAllVelocities(listOfParticles):
	for i in range(len(listOfParticles)):
		listOfParticles[i].updateVelocity()
	
	return listOfParticles


def updateAllPositions(listOfParticles, iteration):
	for i in range(len(listOfParticles)):
		listOfParticles[i].updatePosition(temperatureFunction(iteration))
	
	return listOfParticles

		
from time import clock;
def printElapsedTime():
	print( (clock() - START))
   

	
def hasConverged(particles):
	for i in range(1, len(particles)):
		if particles[i].currentPosition != SAParticleClass.bestPointForAllParticles and particles[i].currentPosition + Vector(1,0,) != SAParticleClass.bestPointForAllParticles \
			and particles[i].currentPosition + Vector(0,1) != SAParticleClass.bestPointForAllParticles and particles[i].currentPosition + Vector(-1,0) != SAParticleClass.bestPointForAllParticles\
				and particles[i].currentPosition + Vector(0,-1) != SAParticleClass.bestPointForAllParticles:
					return False
	
	print('PARTICLES HAVE CONVERGED')
	return True

def figureOutBestConstants(completeListOfCloses):
	VectorsClassNew.completeListOfNumbers = completeListOfCloses[:]
	VectorsClassNew.useEntireArray = True
	
	#minParticle = Particle(0,0,0,0)F
	#minFitness = 0
	
	minAvgFitness = 0
	
	inertiaWeight = 0
	selfWeight = 0
	socialWeight = 0
	
	bestInertiaWeight = 0
	bestSelfWeight = 0
	bestSocialWeight = 0
	
	listOfConstantsThatGaveTheSameAvgFitness = []
	
	for inertiaWeight in range (1 , 6, 1):
		for selfWeight in range (5, 16, 1):
			for socialWeight in range (10, 21, 1):
				SAParticleClass.constantWeightFactor1 = selfWeight / 10	# [1.5, 2] ignore these contraints for the moment
				SAParticleClass.constantWeightFactor2 = socialWeight / 10# [2, 2.5]
				SAParticleClass.inertiaWeight = inertiaWeight / 10	# [.4, 1.4]
	
				print(SAParticleClass.inertiaWeight, SAParticleClass.constantWeightFactor1, SAParticleClass.constantWeightFactor2)
				
				sumOfFitnesses = 0
				for i in range(3):
					bestParticle = runPSO(completeListOfCloses)
					bestParticleFitness = bestParticle.costForMinimiziation()
					sumOfFitnesses += bestParticleFitness
					
				if sumOfFitnesses / 3 == minAvgFitness:
					listOfConstantsThatGaveTheSameAvgFitness.append((SAParticleClass.inertiaWeight, SAParticleClass.constantWeightFactor1, SAParticleClass.constantWeightFactor2, sumOfFitnesses / 3)) 
				
				if sumOfFitnesses / 3 < minAvgFitness:
					#minParticle = bestParticle
					#minFitness = bestParticleFitness
					minAvgFitness = sumOfFitnesses / 3 
					
					bestInertiaWeight = SAParticleClass.inertiaWeight
					bestSelfWeight = SAParticleClass.constantWeightFactor1
					bestSocialWeight = SAParticleClass.constantWeightFactor2
					
	print(bestInertiaWeight, bestSelfWeight, bestSocialWeight)
	print(listOfConstantsThatGaveTheSameAvgFitness)

def runSA(completeListOfCloses):
	print('Simulated Annealing')

	VectorsClassNew.completeListOfNumbers = completeListOfCloses[:]
	VectorsClassNew.useEntireArray = False
	print('got here')

	
	#listOfParticles = createListOfParticles()	#Initialize the population of particles
	#listOfParticles = createListOfParticlesEquallyDistributed()
	listOfParticles = createListOfParticlesEquallyDistributedTriangle()

	#listOfParticles = createListOfParticlesEquallyDistributedInQuadrants()	
	#listOfParticles  = createListOfParticlesRadialSquares()
	display(listOfParticles)
	printElapsedTime()
	
	bestParticle = findBestParticle(listOfParticles[:])
	SAParticleClass.bestPointForAllParticles = bestParticle.currentPosition
	SAParticleClass.bestPointForAllParticlesFitness = bestParticle.costForMinimization()
	
	#ParticleClass.listOfParticles = listOfParticles[:]
	#ParticleClass.listOfFitnesses = [p.costForMinimization() for p in ParticleClass.listOfParticles]

	
	SAParticleClass.constantWeightFactor1 = 1	# [1.5, 2] ignore these contraints for the moment
	SAParticleClass.constantWeightFactor2 = 1.3# [2, 2.5]
	SAParticleClass.inertiaWeight = .1	# [.4, 1.4]
	

	iteration = 0
	iterationsSinceGlobalBestParticleHasChanged = 0
	
	while not hasConverged(listOfParticles) and iteration < 50:
		
		#if iteration % 1000 == 0:
		

		listOfParticles = updateAllPositions(listOfParticles[:], iteration)
		
		SAParticleClass.bestPointForAllParticles = bestParticle.currentPosition
		SAParticleClass.bestPointForAllParticlesFitness = bestParticle.costForMinimization()
		
		bestParticle = findBestParticle(listOfParticles[:])
		#if temperatureFunction(iteration) <= 0:
			#display(listOfParticles)
			#print('Done: ', iteration, ' is: ', SAParticleClass.bestPointForAllParticles, SAParticleClass.bestPointForAllParticlesFitness)

			#print('PARTICLES HAVE MORE OR LESS CONVERGED AFTER ', iterationsSinceGlobalBestParticleHasChanged, ' ITERATIONS')
			#printElapsedTime()

			#import sys
			#sys.exit()

		if bestParticle.currentPosition == SAParticleClass.bestPointForAllParticles:
			iterationsSinceGlobalBestParticleHasChanged += 1
		else:
			iterationsSinceGlobalBestParticleHasChanged = 0
		
		if iterationsSinceGlobalBestParticleHasChanged >= 20:
			print('Done: ', iteration, ' is: ', SAParticleClass.bestPointForAllParticles, SAParticleClass.bestPointForAllParticlesFitness)
			break
		
		#if iteration % 1000 == 0:	

		#listOfParticles = updateAllVelocities(listOfParticles[:]) NOT NECCESSART HERE
		
		
		print('ITERATION: ', iteration)
		display(listOfParticles)
		
		print('The Best Particle After Iteration: ', iteration, ' is: ', SAParticleClass.bestPointForAllParticles, SAParticleClass.bestPointForAllParticlesFitness)

		
	
		printElapsedTime()
		iteration += 1
		
		
	
	print(SAParticleClass.bestPointForAllParticles)
	printElapsedTime()

	return SAParticleClass.bestPointForAllParticles



def displayGraph():

	t = arange(0.0, 2.0, 0.01)
	s = sin(2*pi*t)
	plot(t, s)

	xlabel('time (s)')
	ylabel('voltage (mV)')
	title('About as simple as it gets, folks')
	grid(True)
	savefig("test.png")
	show()





START = clock()


def temperatureFunction(iteration):	#NOTE: FIX
	#if iteration != 0:
	return .1 + iteration/100
	#return 0

def main():
	
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
	
	VectorsClassNew.completeListOfNumbers = completeListOfCloses[:]
	VectorsClassNew.useEntireArray = False
	print('got here')
	
	#p = Particle(2.232, 6.2322, 2.4, 5.6)
	#print(p)
	#import sys
	#sys.exit()
	#p1 = Particle(2,6,0,0)
	#p2 = Particle(3,6,0,0)
	#print( p1.currentPosition == p2.currentPosition + Vector(-1,0))
	#import sys
	#sys.exit()
	
	#listOfParticles = createListOfParticles()	#Initialize the population of particles
	#listOfParticles = createListOfParticlesEquallyDistributed()
	listOfParticles = createListOfParticlesEquallyDistributedTriangle()

	#listOfParticles = createListOfParticlesEquallyDistributedInQuadrants()	
	#listOfParticles  = createListOfParticlesRadialSquares()
	display(listOfParticles)
	printElapsedTime()
	
	bestParticle = findBestParticle(listOfParticles[:])
	SAParticleClass.bestPointForAllParticles = bestParticle.currentPosition
	SAParticleClass.bestPointForAllParticlesFitness = bestParticle.costForMinimization()
	
	#ParticleClass.listOfParticles = listOfParticles[:]
	#ParticleClass.listOfFitnesses = [p.costForMinimization() for p in ParticleClass.listOfParticles]

	
	SAParticleClass.constantWeightFactor1 = 1	# [1.5, 2] ignore these contraints for the moment
	SAParticleClass.constantWeightFactor2 = 1.3# [2, 2.5]
	SAParticleClass.inertiaWeight = .1	# [.4, 1.4]
	
	#ParticleClass.bestPointForAllParticles = bestParticle.currentPosition
	#print(ParticleClass.bestPointForAllParticles)

	#print('got here')
	#print('This is the particele,', listOfParticles[1])
	#print('List of fitnesses,', ParticleClass.listOfFitnesses)
	#listOfParticles[1].updateVelocity()
	#print('Updated velocity,', listOfParticles[1])
	
	#listOfParticles[1].updatePosition()
	#print('Updated position,', listOfParticles[1])	
	
	#import sys
	#sys.exit()
	iteration = 0
	iterationsSinceGlobalBestParticleHasChanged = 0
	
	prevBestParticle = SAParticleClass.bestPointForAllParticles
	
	while not hasConverged(listOfParticles) and iteration < 50 and iterationsSinceGlobalBestParticleHasChanged < 30:
		
		#if iteration % 1000 == 0:
		

		listOfParticles = updateAllPositions(listOfParticles[:], iteration)
		
		SAParticleClass.bestPointForAllParticles = bestParticle.currentPosition
		SAParticleClass.bestPointForAllParticlesFitness = bestParticle.costForMinimization()
		
		if prevBestParticle == SAParticleClass.bestPointForAllParticles:
			iterationsSinceGlobalBestParticleHasChanged += 1
		
		bestParticle = findBestParticle(listOfParticles[:])
		#if temperatureFunction(iteration) <= 0:
			#display(listOfParticles)
			#print('Done: ', iteration, ' is: ', SAParticleClass.bestPointForAllParticles, SAParticleClass.bestPointForAllParticlesFitness)

			#print('PARTICLES HAVE MORE OR LESS CONVERGED AFTER ', iterationsSinceGlobalBestParticleHasChanged, ' ITERATIONS')
			#printElapsedTime()

			#import sys
			#sys.exit()

		if bestParticle.currentPosition == SAParticleClass.bestPointForAllParticles:
			iterationsSinceGlobalBestParticleHasChanged += 1
		else:
			iterationsSinceGlobalBestParticleHasChanged = 0
		
		if iterationsSinceGlobalBestParticleHasChanged >= 20:
			print('Done: ', iteration, ' is: ', SAParticleClass.bestPointForAllParticles, SAParticleClass.bestPointForAllParticlesFitness)
			break
		
		#if iteration % 1000 == 0:	

		#listOfParticles = updateAllVelocities(listOfParticles[:]) NOT NECCESSART HERE
		
		
		print('ITERATION: ', iteration)
		display(listOfParticles)
		
		print('The Best Particle After Iteration: ', iteration, ' is: ', SAParticleClass.bestPointForAllParticles, SAParticleClass.bestPointForAllParticlesFitness)

		
		#ParticleClass.listOfParticles = listOfParticles[:]
		#ParticleClass.listOfFitnesses = [p.costForMinimization() for p in ParticleClass.listOfParticles]
		
		#if not ParticleClass.bestPointForAllParticles.costForMinimiziation() == bestParticle.costForMinimization():
				#import sys
				#print('NOT WORKING')
				#print('This: ',ParticleClass.bestPointForAllParticles, 'should be the same as: ', bestParticle.currentPosition)
				#sys.exit()
		#if iteration % 1000 == 0:	
		printElapsedTime()
		iteration += 1
		
		
		
		
		
	
if __name__ == '__main__': main()