
def calculateSMA(completeListOfNumbers, SMALegnth, currentDateAsAnIndexNumber): #NOTE: Returns double
									
	
	#if SMALegnth <= 0: #We dont want negative lengths
		#return 0
	
	runningSum = 0
	
	if currentDateAsAnIndexNumber - SMALegnth + 1 > -1:
		for num in range(currentDateAsAnIndexNumber - SMALegnth + 1, currentDateAsAnIndexNumber + 1):
			#print(num)
			runningSum += completeListOfNumbers[num]
		#print('SMA length: ', SMALegnth) 
		from math import sqrt
		return runningSum/SMALegnth
	
	else: return 0

def convertDateToIndex(listOfDates, year, month, day):
	date = str(year) + '-' + str(month) + '-' + str(day)
	#print(date)
	for index in range(len(listOfDates)):
		#if listOfDates[index] == date:   
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
	if dateOfCrossover + xNumberOfDays - 1 < len(completeListOfNumbers):
		return completeListOfNumbers[dateOfCrossover + xNumberOfDays - 1] - completeListOfNumbers[dateOfCrossover] > 0
	#print(dateOfCrossover + xNumberOfDays - 1)
	#print(completeListOfNumbers)
	print('Error, exceeded date range')
	import sys
	sys.exit()
	
def percentIncreaseInXDays(xNumberOfDays, completeListOfNumbers, dateOfCrossover):#NOTE: dateOfCrossover is an index
	if dateOfCrossover + xNumberOfDays -1 < len(completeListOfNumbers):
		return (completeListOfNumbers[dateOfCrossover + xNumberOfDays - 1] - completeListOfNumbers[dateOfCrossover]) / completeListOfNumbers[dateOfCrossover] * 100
	
	print('Error, exceeded date range', dateOfCrossover)
	import sys
	sys.exit()
	
	
	
#NOTE: This is functioF base on percentSuccess in terms of how many times the crossover results in increased stock price
#def functionF(SMALegnthShort, SMALegnthLong, completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
	#if SMALegnthShort <= 1 or SMALegnthLong <= 1:
		#return 0
	
	#if SMALegnthShort > SMALegnthLong: 
		#SMALegnthShort, SMALegnthLong = SMALegnthLong, SMALegnthShort
	
	#percentSuccess = 0
	#time = (SMALegnthShort + SMALegnthLong) / 2
	
	#numberOfTimesUpwardCrossOccurs = 0
	#numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays = 0
	
	#for dateIndex in range(startDateIndex + SMALegnthLong, endDateIndex - xNumberOfDays):
		
		#if SMAAboveCrossoverHasOccured(SMALegnthShort, SMALegnthLong, dateIndex, dateIndex + 1, completeListOfNumbers):
			#numberOfTimesUpwardCrossOccurs += 1
			
			#if StockPriceIncreasedWithinXDaysOfCrossover(xNumberOfDays, completeListOfNumbers, dateIndex + 1):
				#numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays += 1

	#if numberOfTimesUpwardCrossOccurs != 0:
		#percentSuccess = numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays/numberOfTimesUpwardCrossOccurs * 100
	
	#else:
		#return -1
	##print(numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays, numberOfTimesUpwardCrossOccurs)
	#from math import sqrt
	#return percentSuccess/sqrt(time) 	#NOTE:Aight. we're gonna try something different
							##I think im discounting the fitness too much for time
							##lets try dividing by roo(time) instead of just time
							
#NOTE: This is functioF base on percentSuccess in terms of average magnitude in increase in stock price
def functionF(SMALegnthShort, SMALegnthLong, completeListOfNumbers, startDateIndex, endDateIndex, xNumberOfDays):
	if SMALegnthShort <= 1 or SMALegnthLong <= 1:
		return 0
	
	if SMALegnthShort > SMALegnthLong: 
		SMALegnthShort, SMALegnthLong = SMALegnthLong, SMALegnthShort
	
	percentSuccess = 0
	time = (SMALegnthShort + SMALegnthLong) / 2
	
	numberOfTimesUpwardCrossOccurs = 0
	numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays = 0
	
	sumOfPercentIncreases = 0

	for dateIndex in range(startDateIndex + SMALegnthLong, endDateIndex - xNumberOfDays):
		

		if SMAAboveCrossoverHasOccured(SMALegnthShort, SMALegnthLong, dateIndex, dateIndex + 1, completeListOfNumbers):
			numberOfTimesUpwardCrossOccurs += 1
			
			percentIncrease = percentIncreaseInXDays(xNumberOfDays, completeListOfNumbers, dateIndex + 1)
			sumOfPercentIncreases += percentIncrease
			#print(percentIncrease)
			#if StockPriceIncreasedWithinXDaysOfCrossover(xNumberOfDays, completeListOfNumbers, dateIndex + 1):
				#numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays += 1

	if numberOfTimesUpwardCrossOccurs != 0:
		percentSuccess = sumOfPercentIncreases/numberOfTimesUpwardCrossOccurs 
		#print('avg percent change after crossover: ', percentSuccess)
	
	else:
		return -1
	#print(numberOfTimesUpwardCrossResultsInIncreasedStockPriceWithinXDays, numberOfTimesUpwardCrossOccurs)
	from math import sqrt
	return percentSuccess/sqrt(time) 	#NOTE:Aight. we're gonna try something different
							#I think im discounting the fitness too much for time
							#lets try dividing by roo(time) instead of just time
	#if 1 < SMALegnthShort <= 300 and 1 < SMALegnthLong <= 300:
		#return ( SMALegnthShort + SMALegnthLong)
	
	#else:
		#return -1000

def main():
	
	
	
	
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
	print(percentIncreaseInXDays(5, completeListOfCloses, 0))
	#functionF(5,10,completeListOfCloses,0,10000,5)
	
	print(completeListOfCloses[0], completeListOfCloses[4])
if __name__ == '__main__': main()