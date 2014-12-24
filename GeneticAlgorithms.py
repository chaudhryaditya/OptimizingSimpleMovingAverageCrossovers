

#5 Steps to GAs:
	#0.Fitness - got it
	#1.Notation - [short, long] as a Vector
	#2.Selection - Tournament, roulette, top half --> we'll start simple, only breed the top half
	#3.Breeding - only can crossover at one point
	#4.Replacement- 

from LibraryOfEssentialFunctions import *
from VectorsClassNew import *

MAX_RUN_TIME = 120 #seconds
MAX_TRIANGLE_COUNT = 50 #end search after this many applications of the Nelder-Mead algorithm
DOMAIN_LIMIT = 300 # 0 <= x <= DL and 0 <= y <= DL, DL = DOMAIN_LIMIT
def display(chroms):
	print('-------Chromosomes-------')
	for i in range(len(chroms)):
		print(chroms[i], chroms[i].costForMaximiziation())
	print('-------------------------')
	

def sortListBestToWorse(Lst): #List passed by refference, sorted in place-->No return
	Vector.sort(Lst) 

def createSortedListofChroms():
	chroms = []
	[chroms.append(chromosome(MAX)) for i in range(POP)]
	#print('yo', chroms)
	sortListBestToWorse(chroms)
	return chroms
	
	
def chromosome(numberOfGenes):
	from random import randint, random
	v = Vector(int(random() * DOMAIN_LIMIT), int(random() * DOMAIN_LIMIT))
	if v.data[0] > v.data[1]:
		v.data[0], v.data[1] = v.data[1] , v.data[0]
	return v
		
def breedPopulationWithSimpleSelection(chroms):	#breed top half of pop with best chrom
	from random import randint
	parent1 = chroms[0]
	newChroms = []
	for i in range(1, POP//2 + 1):
		parent2 = chroms[i]
		r = 1#randint(0, MAX)
		child1 = Vector(parent1.data[0], parent2.data[1]) #parent1[:r] + parent2[r:]
		child2 = Vector(parent2.data[0], parent1.data[1])#parent2[:r] + parent1[r:]
		
		
		if parent1.data[0] > parent2.data[1]:#Put chroms in right place
			child1 = Vector(parent2.data[1], parent1.data[0])
		if parent2.data[0] > parent1.data[1]:
			child2 = Vector(parent1.data[1], parent2.data[0])
			
		newChroms.append(child1)
		newChroms.append(child2)
		#print('new chroms: ', newChroms)
	#print(type(newChroms[0]) == Vector)
	sortListBestToWorse(newChroms)
	return newChroms

def tournamentSelection(chroms):	 
		from random import randint	#Return the best two of three randomly selcted
		index1 = randint(0, len(chroms) - 1) #Pick 3 random indicies
		index2 = randint(0, len(chroms) - 1) 
		index3 = randint(0, len(chroms) - 1) 

		while index1 == index2:
			index2 = randint(0, len(chroms) - 1) 
		while index1 == index3 or index2 == index3:
			index3 = randint(0, len(chroms) - 1) 
		
		setOfParents = [chroms[index1], chroms[index2], chroms[index3]]
		sortListBestToWorse(setOfParents)
		#print(setOfParents[0].costForMaximiziation(), setOfParents[1].costForMaximiziation(),setOfParents[2].costForMaximiziation())
		#display(setOfParents)

		setOfParents.pop(2)	#Remove element with worst cost
		
		#display(setOfParents)

		return setOfParents[0], setOfParents[1] 
		
def breedPopulationWithTournamentSelection(chroms):		
		newChroms = []
		for i in range(POP//2):
			parent1, parent2 = tournamentSelection(chroms)
			
			child1 = Vector(parent1.data[0], parent2.data[1]) #parent1[:r] + parent2[r:]
			child2 = Vector(parent2.data[0], parent1.data[1])#parent2[:r] + parent1[r:]
			
			if parent1.data[0] > parent2.data[1]:#Put chroms in right place
				child1 = Vector(parent2.data[1], parent1.data[0])
			if parent2.data[0] > parent1.data[1]:
				child2 = Vector(parent1.data[1], parent2.data[0])
				
			newChroms.append(child1)
			newChroms.append(child2)
		
		
		sortListBestToWorse(newChroms)
		return newChroms


def rouletteSelection(chroms):	#List is sorted best to worst
		from random import random
		sumOfFitnesses = 0
		listOfCosts = []
		for c in chroms:
			costOfThisChrom = c.costForMaximiziation()
			listOfCosts.append(costOfThisChrom)
			sumOfFitnesses += costOfThisChrom
		#print('total sum is: ', sumOfFitnesses)
		
		listOfProbs = []
		#maxCost = 0
		
		for cost in listOfCosts:
			listOfProbs.append(cost/ sumOfFitnesses)

		#for c in chroms:
			#cost = c.costForMaximiziation() 
			#listOfProbs.append(c.costForMaximiziation() / sumOfFitnesses)
			
			#if cost / sumOfFitnesses > maxCost:
				#maxCost = cost / sumOfFitnesses
			
		listOfCumulativeProbs = listOfProbs[:]
		
		for i in range(1, len(listOfCumulativeProbs), 1):
			listOfCumulativeProbs[i] = listOfCumulativeProbs[i - 1] + listOfCumulativeProbs[i]
		
		#print(listOfProbs)	

		#print(listOfCumulativeProbs)	
		
		print('list of indiv probs: ', listOfProbs)

		print('each chrom has prob of being picked: ', listOfCumulativeProbs)
		randomDouble1 = random() 
		#print(randomDouble1)
		indexOfFirstParent = -1	#So if it doesnt work itll kick an error
		for i in range(len(chroms) - 1, -1, -1):	#Lowest probs are at end
		#for i in range(len(chroms)):
			if randomDouble1 < listOfCumulativeProbs[i]:
				#if i == 0:
				indexOfFirstParent = i 
				#else:
					#indexOfFirstParent = i - 1
			
		
		randomDouble2 = random()
		indexOfSecondParent = indexOfFirstParent
		#print(randomDouble2)
	
		
		#while(indexOfSecondParent == indexOfFirstParent):
		for i in range(len(chroms) - 1, -1, -1):
			#for i in range(len(chroms)):
				if randomDouble2 < listOfCumulativeProbs[i]:
					#if i == 0:
					indexOfSecondParent = i 
		
		#print(indexOfFirstParent, indexOfSecondParent)
				#else:
					#indexOfSecondParent = i - 1
				
				
		#from random import randint	#Return the best two of three randomly selcted
		#index1 = randint(0, len(chroms) - 1) #Pick 3 random indicies
		#index2 = randint(0, len(chroms) - 1) 
		#index3 = randint(0, len(chroms) - 1) 

		#while index1 == index2:
			#index2 = randint(0, len(chroms) - 1) 
		#while index1 == index3 or index2 == index3:
			#index3 = randint(0, len(chroms) - 1) 
		
		#setOfParents = [chroms[index1], chroms[index2], chroms[index3]]
		#sortListBestToWorse(setOfParents)
		##display(setOfParents)

		#setOfParents.pop(2)	#Remove element with worst cost
		
		#display(setOfParents)
		#print(chroms[indexOfFirstParent], chroms[indexOfSecondParent] )
		#print(indexOfFirstParent, indexOfSecondParent)

		return chroms[indexOfFirstParent], chroms[indexOfSecondParent] 
		
def breedPopulationWithRouletteSelection(chroms):			
		newChroms = []
		for i in range(POP//2):
			parent1, parent2 = rouletteSelection(chroms)
			
			child1 = Vector(parent1.data[0], parent2.data[1]) #parent1[:r] + parent2[r:]
			child2 = Vector(parent2.data[0], parent1.data[1])#parent2[:r] + parent1[r:]
				
			if parent1.data[0] > parent2.data[1]:	#Put chroms in right place
				child1 = Vector(parent2.data[1], parent1.data[0])
			if parent2.data[0] > parent1.data[1]:
				child2 = Vector(parent1.data[1], parent2.data[0])
			
			newChroms.append(child1)
			newChroms.append(child2)
			print('time to breeding ', i, ' = ', clock() - START, '(parent1, parent2,): ', parent1, parent2)
		
		
		sortListBestToWorse(newChroms)
		return newChroms
	
def hasConverged(chroms):
	for i in range(1, len(chroms)):
		if chroms[i] != chroms[i - 1]:
			return False
		
	return True

def runGA(completeListOfCloses):
	print('Genetic Algorithms')

	VectorsClassNew.completeListOfNumbers = completeListOfCloses[:]
	VectorsClassNew.useEntireArray = True
	
	print(VectorsClassNew.useEntireArray )
	chroms = createSortedListofChroms()
	display(chroms)
	
	print('got here')
	
	printElapsedTime()

	#v = Vector(247, 247)
	#print(v.costForMaximiziation())
	#for n in range(GEN):
	sortListBestToWorse(chroms)
	n = 0

	
	while not hasConverged(chroms):
	#while clock() - START < MAX_RUN_TIME:
		chroms = breedPopulationWithSimpleSelection(chroms)
		#chroms = breedPopulationWithTournamentSelection(chroms)
		#chroms = breedPopulationWithRouletteSelection(chroms)
		#print('GENERATION: ', n)
		
		display(chroms)
	
		#printElapsedTime()
		n = n + 1
	print(chroms[0])
	return chroms[0]
#GLOBAL CONSTANTS
MAX = 2
POP = 16
HPOP = POP//2
GEN = 16
import VectorsClassNew
from time import clock;
def printElapsedTime():
	print( (clock() - START))



START = clock()

def main():
	
	
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE
	#NOTE: sort returns least to greatest
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
	VectorsClassNew.useEntireArray = False
	
	chroms = createSortedListofChroms()
	display(chroms)
	
	print('got here')
	
	printElapsedTime()

	#v = Vector(247, 247)
	#print(v.costForMaximiziation())
	#for n in range(GEN):
	sortListBestToWorse(chroms)
	n = 0

	
	while not hasConverged(chroms):
	#while clock() - START < MAX_RUN_TIME:
		chroms = breedPopulationWithSimpleSelection(chroms)
		#chroms = breedPopulationWithTournamentSelection(chroms)
		#chroms = breedPopulationWithRouletteSelection(chroms)
		print('GENERATION: ', n)
		
		display(chroms)
	
		printElapsedTime()
		n = n + 1
	
if __name__ == '__main__': main()