def calculateSMA(completeListOfNumbers, SMALegnth, currentDateAsAnIndexNumber): #NOTE: Returns double
	runningSum = 0
	
	if currentDateAsAnIndexNumber - SMALegnth + 1 > -1:
		for num in range(currentDateAsAnIndexNumber - SMALegnth + 1, currentDateAsAnIndexNumber + 1):
			runningSum += completeListOfNumbers[num]
		#print('SMA length: ', SMALegnth) 
		return runningSum/SMALegnth
	
	else: return 0

def convertDateToIndex(listOfDates, year, month, day):
	date = str(year) + '-' + str(month) + '-' + str(day)
	print(date)
	for index in range(len(listOfDates)):
		if listOfDates[index] == date:   
			return index
		
		
def SMAAboveCrossoverHasOccured(SMALegnthShort, SMALegnthLong, date1, date2, completeListOfNumbers):	#NOTE: returns boolean, dates are indicies
	if SMALegnthShort > SMALegnthLong: 
		SMALegnthShort, SMALegnthLong = SMALegnthLong, SMALegnthShort 
	if date1 > date2: 
		date1, date2 = date2, date1

	if calculateSMA(completeListOfNumbers, SMALegnthShort, date1) < calculateSMA(completeListOfNumbers, SMALegnthLong, date1):	#If short SMA is originally < long SMA
		if calculateSMA(completeListOfNumbers, SMALegnthShort, date2) > calculateSMA(completeListOfNumbers, SMALegnthLong, date2):	#But then becomes more
			return True	#an upward crossover has occured
		
	return False	#otherwise no
	
def StockPriceIncreasedWithinXDaysOfCrossover(xNumberOfDays, completeListOfNumbers, dateOfCrossover):	#NOTE: dateOfCrossover is an index
	if dateOfCrossover + xNumberOfDays < len(completeListOfNumbers):
		return completeListOfNumbers[dateOfCrossover + xNumberOfDays] - completeListOfNumbers[dateOfCrossover] > 0
	
	print('Error, exceeded date range')
	import sys
	sys.exit()
	
def functionF(SMALegnthShort, SMALegnthLong, completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
	if SMALegnthShort > SMALegnthLong: 
		SMALegnthShort, SMALegnthLong = SMALegnthLong, SMALegnthShort
		
	percentSuccess = 0
	time = (SMALegnthShort + SMALegnthLong) / 2
	numberOfTimesUpwardCrossOccurs = 0
	numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays = 0
	for dateIndex in range(startDateIndex + SMALegnthLong, endDateIndex):
		if SMAAboveCrossoverHasOccured(SMALegnthShort, SMALegnthLong, dateIndex, dateIndex + 1, completeListOfNumbers):
			numberOfTimesUpwardCrossOccurs += 1
			if StockPriceIncreasedWithinXDaysOfCrossover(xNumberOfDays, completeListOfNumbers, dateIndex + 1):
				numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays += 1
	
	if numberOfTimesUpwardCrossOccurs != 0:
		percentSuccess = numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays/numberOfTimesUpwardCrossOccurs * 100
	else:
		return -1
	#print(numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays, numberOfTimesUpwardCrossOccurs)
	return percentSuccess/time

def HillClimbNextPoint(completeListOfNumbers, SMALegnthShort, SMALegnthLong, startDateIndex, endDateIndex, xNumberOfDays):
	
	maxCostPoint = [SMALegnthShort, SMALegnthLong]
	for shortLength in [SMALegnthShort - 1, SMALegnthShort + 1]:
		for longLength in [SMALegnthLong - 1, SMALegnthLong + 1]:
			if shortLength > 1 and longLength > 1:
				if functionF(shortLength, longLength, completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays) > functionF(SMALegnthShort, SMALegnthLong, completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
					maxCostPoint = [shortLength, longLength]
					#print('Our current min cost point is: ', minCostPoint)
		
	return maxCostPoint
	


def HillClimbSearch(completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
	from random import randint
	currentPoint = [randint(2, 300), randint(2, 300)]
	while currentPoint[0] == currentPoint[1]:
		currentPoint[0] = randint(2, 300)
	if currentPoint[0] > currentPoint[1]:
		currentPoint[0], currentPoint[1] = currentPoint[1], currentPoint[0]
	#print('We start with: ', currentPoint[0], currentPoint[1], functionF(currentPoint[0], currentPoint[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays))
	pointsSearched = 0
	while True:
		newPoint = HillClimbNextPoint(completeListOfNumbers, currentPoint[0], currentPoint[1], startDateIndex, endDateIndex, xNumberOfDays)
		if functionF(newPoint[0], newPoint[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays) > functionF(currentPoint[0], currentPoint[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
			currentPoint[:] = newPoint[:]	#as long as the new point is better, keeo going. Once we can no longer find a better point, end
		else:
			break
		#print('We are now on', newPoint)
		pointsSearched += 4
	print('points searched = ', pointsSearched)
	return currentPoint, pointsSearched

def HillClimbSearchStartingWithAGIvenPoint(completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays, startX, startY):
	from random import randint
	currentPoint = [startX, startY]
	#while currentPoint[0] == currentPoint[1]:
		#currentPoint[0] = randint(2, 300)
	if currentPoint[0] > currentPoint[1]:
		currentPoint[0], currentPoint[1] = currentPoint[1], currentPoint[0]
	#print('We start with: ', currentPoint[0], currentPoint[1], functionF(currentPoint[0], currentPoint[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays))
	pointsSearched = 0
	while True:
		newPoint = HillClimbNextPoint(completeListOfNumbers, currentPoint[0], currentPoint[1], startDateIndex, endDateIndex, xNumberOfDays)
		if functionF(newPoint[0], newPoint[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays) > functionF(currentPoint[0], currentPoint[1], completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
			currentPoint[:] = newPoint[:]	#as long as the new point is better, keeo going. Once we can no longer find a better point, end
		else:
			break
		#print('We are now on', newPoint)
		pointsSearched += 4
	print('points searched = ', pointsSearched)
	return currentPoint, pointsSearched

from time import clock;
def printElapsedTime():
	print( (clock() - START))



START = clock()
def main():
	
	#print('Hello')
	
	
	
	#file1 = open ('DowData.txt', mode = 'r', encoding = 'utf 8')
	file1 = open('DowData1.txt', mode = 'r')
	file2 = open('Dates.txt', mode = 'r')
	#file1.write('P3' + ' ' + str(IMAGE_WIDTH) + ' ' + str(IMAGE_HEIGHT) + ' ' + str(255) + '\n')
	completeListOfCloses = []
	for line in file1:
		completeListOfCloses.append(float(line.strip()))
		##print(line)
		#stng = line.strip()
		#stng = stng.lower()
		#if len(stng) > 3:
			#t.insert(stng)
		
	file1.close()
	
	completeListOfDates = []
	for line in file2:
		completeListOfDates.append(line.strip())
	
	file2.close()
	
	#print(calculateSMA(completeListOfCloses,5,4))
	#print(convertDateToIndex(completeListOfDates, '1940', '05', '30'))
	#print(SMAAboveCrossoverHasOccured(2, 5, 12, 13, completeListOfCloses))
	#print(StockPriceIncreasedWithinXDaysOfCrossover(5, completeListOfCloses, 13))
	#print('--------------------------------------------')
	
	#print(functionF(5, 10, completeListOfCloses, 0, 10000, 5))
	
	#print('--------------------------------------------')
	
	#point = HillClimbSearch(completeListOfCloses, 0, 10000, 5)
	#print('The point is: ', point[0], point[1], functionF(point[0], point[1], completeListOfCloses, 0, 10000, 5))
	
	maxFitness = 0
	pointOfMaxFitness = [0,0]
	maxShortSMALength = 300
	maxLongSMALength = 300
	listOfPoints = []
	listOfFitnesses = []
	listOfElapsedTimes = []
	listOfNumberOfPointsExamined = []
	listOfStartingPoints = [(int(maxShortSMALength / 4) - 1, int (maxLongSMALength / 4)), (int(maxShortSMALength / 4), int(maxLongSMALength * 3 / 4)), (int(maxShortSMALength * 3 / 4) - 1, int(maxLongSMALength * 3 / 4))]
	numPoints = 10
	#NOTE: WITH RANDOM STARTING POSITIONS: Works much better
	
	for i in range (numPoints):
		startTime = clock() - START
		#printElapsedTime()
		tuppleReturnedByHillCLimbing = HillClimbSearch(completeListOfCloses, 0, 10000, 5)
		point = tuppleReturnedByHillCLimbing[0]
		fitness = functionF(point[0], point[1], completeListOfCloses, 0, 10000, 5)
		if fitness > maxFitness:
			maxFitness = fitness
			pointOfMaxFitness[:] = point[:]
		listOfPoints.append(point[:])
		listOfFitnesses.append(fitness)
		print('Done with iteration: ', i)
		printElapsedTime()
		endTime = clock() - START
		timeElapsed = endTime - startTime
		listOfElapsedTimes.append(timeElapsed)
		listOfNumberOfPointsExamined.append(tuppleReturnedByHillCLimbing[1])
		
	#NOTE: WITH GIVEN STARTING POSITIONS:	Does not work well, we get (73, 76) f = .7516
	#print(listOfStartingPoints)
	#for i in range (len(listOfStartingPoints)):
		
		#startTime = clock() - START
		##printElapsedTime()
		#tuppleReturnedByHillCLimbing = HillClimbSearchStartingWithAGIvenPoint(completeListOfCloses, 0, 10000, 5, listOfStartingPoints[i][0], listOfStartingPoints[i][1])
		
		#point = tuppleReturnedByHillCLimbing[0]
		#fitness = functionF(point[0], point[1], completeListOfCloses, 0, 10000, 5)
		#print('point of iteration, ', i, 'is: ', point, fitness)
		#if fitness > maxFitness:
			#maxFitness = fitness
			#pointOfMaxFitness[:] = point[:]
		#listOfPoints.append(point[:])
		#listOfFitnesses.append(fitness)
		#print('Done with iteration: ', i)
		#printElapsedTime()
		#endTime = clock() - START
		#timeElapsed = endTime - startTime
		#listOfElapsedTimes.append(timeElapsed)
		#listOfNumberOfPointsExamined.append(tuppleReturnedByHillCLimbing[1])
		
	sumOfFitnesses = 0
	for f in listOfFitnesses:
		sumOfFitnesses += f
		
	print('The max point is: ', pointOfMaxFitness[0], pointOfMaxFitness[1], functionF(pointOfMaxFitness[0], pointOfMaxFitness[1], completeListOfCloses, 0, 10000, 5))
	print('The average fitness of all', numPoints, 'is', sumOfFitnesses/numPoints)
	print(listOfElapsedTimes)
	print(listOfNumberOfPointsExamined)
	print('Time elapsed per point examined in each iteration:')
	
	for i in range(numPoints):
		if listOfNumberOfPointsExamined[i] != 0:
			print('Seconds per point examined for iteration ', i, ': ', listOfElapsedTimes[i]/listOfNumberOfPointsExamined[i])
		else:
			print('0 points examined, time elased for iteration is', i, ': ', listOfElapsedTimes[i])

	printElapsedTime()
if __name__ == '__main__': main()