from tkinter import *
from tkinter.ttk import *

import ystockquote
import SMAs
import GeneticAlgorithms
import VectorsClassNew
import NelderMeadNew
import PSO
import ParticleClass
import HillClimbing
import NelderMeadNew
import DifferentialEvolution
import SA
#from matplotlib import *


from LibraryOfEssentialFunctions import *
from VectorsClassNew import *
from ParticleClass import *


from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
  

class Application(Frame):  
	
	
	def say_hi(self):
		print ("hi there, everyone!")
	
	def about(self):
		print('hi')

	def displayInfo(self):
		#self.counter += 1
		t = Toplevel(self)
		
		if self.algorithmVar.get() == 0:
			t.wm_title("Hill Climbing",)
			#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
			photo = PhotoImage(file="hillClimbing.gif")
			w = Label(t, image=photo)
			w.photo = photo
			w.pack()

		if self.algorithmVar.get() == 1:
			t.wm_title("Nelder-Mead")
			#frame = Frame(t)
			#frame.grid(row = 0,column = 0, sticky = W +E + N + S)
			#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
			photo = PhotoImage(file="nelderMead.gif")
			w = Label(t, image=photo)
			w.photo = photo
			w.grid(row = 0, sticky = W +E + N + S)
			
		if self.algorithmVar.get() == 2:
			t.wm_title("Genetic Algorithm")
			#frame = Frame(t)
			#frame.grid(row = 0,column = 0, sticky = W +E + N + S)
			#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
			photo = PhotoImage(file="geneticAlgorithm.gif")
			w = Label(t, image=photo)
			w.photo = photo
			w.grid(row = 0, sticky = W +E + N + S)
			
		if self.algorithmVar.get() == 3:
			t.wm_title("Differential Evolution")
			#frame = Frame(t)
			#frame.grid(row = 0,column = 0, sticky = W +E + N + S)
			#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
			photo = PhotoImage(file="de.gif")
			w = Label(t, image=photo)
			w.photo = photo
			w.grid(row = 0, sticky = W +E + N + S)
			#l.pack(anchor = N, side="top", fill="both", expand=True, padx=100, pady=100)
			
		if self.algorithmVar.get() == 4:
			t.wm_title("Particle Swarm Optimization")
			#frame = Frame(t)
			#frame.grid(row = 0,column = 0, sticky = W +E + N + S)
			#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
			photo = PhotoImage(file="pso.gif")
			w = Label(t, image=photo)
			w.photo = photo
			w.grid(row = 0, sticky = W +E + N + S)
			#l.pack(anchor = N, side="top", fill="both", expand=True, padx=100, pady=100)

		if self.algorithmVar.get() == 5:
			t.wm_title("Simulated Annealing")
			#frame = Frame(t)
			#frame.grid(row = 0,column = 0, sticky = W +E + N + S)
			#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
			photo = PhotoImage(file="pso.gif")
			w = Label(t, image=photo)
			w.photo = photo
			w.grid(row = 0, sticky = W +E + N + S)
			#l.pack(anchor = N, side="top", fill="both", expand=True, padx=100, pady=100)
	def selectOptimizationAlgorithm(self):
		print('0')
		#self.create_window()
		
	def createWidgets(self):
		self.arrayofIndicies = ['DJIA', '^GSPC', '^IXIC', '^RUA']
		#from  import * 
		#import tkinter.tkFont

		#helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
		
		titleStlye = Style()
		titleStlye.configure("Title.TLabel", foreground="midnight blue", background="orange", font = ("Cambria",22,"bold"),  )
		
		
		self.titleLabel = Label(self, text="Optimizing Simple Moving Average Crossovers", style ="Title.TLabel" )
		self.titleLabel.grid(row = 0, column = 1,  sticky = W + E + S + N)
		
		self.bufferL = Label(self, style ="Title.TLabel" )
		self.bufferL.grid(row = 0,column = 0, sticky = W + E + S + N)
		
		self.bufferR = Label(self, style ="Title.TLabel" )
		self.bufferR.grid(row = 0,column = 2, sticky = W + E + S + N)

		#self.QUIT = Button(self)
		#self.QUIT["text"] = "QUIT"
		#self.QUIT["fg"]   = "red"
		#self.QUIT["command"] =  self.quit

		#self.QUIT.pack({"side": "left"})

		#self.hi_there = Button(self)
		#self.hi_there["text"] = "Hello",
		#self.hi_there["command"] = self.say_hi

		#self.hi_there.pack({"side": "left"})

		#self.textBox = Entry(self)
		#self.textBox.pack()
		
		#left = Label(m1, text="left pane")
		#m1.add(left)

		#m2 = PanedWindow(m1, orient=VERTICAL)
		#m1.add(m2)

		#top = Label(m2, text="top pane")
		#m2.add(top)

		#bottom = Label(m2, text="bottom pane")
		#m2.add(bottom)

		
		#NOTE: Left most column = select your optimization method
		#self.aboutFrame = LabelFrame(self, text="About")
		#self.aboutFrame.grid(row = 0, column = 0, sticky = N)
		
		
		#self.aboutLabel = Label(self.aboutFrame, text="This application finds the best ")
		#self.aboutLabel.pack(anchor = W)
		optimizationMethodsFrameStlye = Style()
		optimizationMethodsFrameStlye.configure("OptimizationFrame.TLabelframe", foreground="black", background="SkyBlue2", )
		
		#optimizationMethodsFrameStlye.configure('OptimizationFrame.TLabelframe.Label', font=('courier', 15, 'bold'))
		#optimizationMethodsFrameStlye.configure('OptimizationFrame.TLabelframe.Label', foreground ='red')
		optimizationMethodsFrameStlye.configure('OptimizationFrame.TLabelframe.Label',foreground="midnight blue", background='SkyBlue2', font = ("Cambria",16,))

		
		
		
		self.optimizationMethodsFrame = LabelFrame(self, text="Select Optimization Method", style = 'OptimizationFrame.TLabelframe')#background='SkyBlue2')
		self.optimizationMethodsFrame.grid(row = 1, column = 0, sticky = W +E + N + S)

		#self.listOfOptimizationMethods = Label(self.optimizationMethodsFrame,)
		#self.listOfOptimizationMethods .pack()
		
		optimizationMethodsRadioButtonStlye = Style()
		optimizationMethodsRadioButtonStlye.configure("OptimizationFrame.TRadiobutton", foreground="midnight blue", background="SkyBlue2", font = ("Cambria",12,))
		
		self.algorithmVar = IntVar()
		
		self.hillClimbingButton = Radiobutton(self.optimizationMethodsFrame, text="Hill Climbing", variable=self.algorithmVar, value=0,
				command= self.selectOptimizationAlgorithm,style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		self.hillClimbingButton.pack(anchor = W )
		
		
		self.nelderMeadButton = Radiobutton(self.optimizationMethodsFrame, text="Nelder-Mead", variable=self.algorithmVar, value=1,
                  command= self.selectOptimizationAlgorithm,style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		self.nelderMeadButton.pack( anchor = W  )


		self.geneticAlgorithmButton = Radiobutton(self.optimizationMethodsFrame, text="Genetic Algorithm", variable=self.algorithmVar, value=2,
				command= self.selectOptimizationAlgorithm,style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		self.geneticAlgorithmButton.pack(anchor = W  )
		
		
		self.differentialEvolutionButton = Radiobutton(self.optimizationMethodsFrame, text="Differential Evolution", variable=self.algorithmVar, value=3,
				command= self.selectOptimizationAlgorithm,style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		self.differentialEvolutionButton.pack(anchor = W  )
		
		
		self.psoButton = Radiobutton(self.optimizationMethodsFrame, text="Particle Swarm Evolution (Recommended)", variable=self.algorithmVar, value=4,
				command= self.selectOptimizationAlgorithm,style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		self.psoButton.pack(anchor = W  )


		self.SAButton = Radiobutton(self.optimizationMethodsFrame, text="Simulated Annealing", variable=self.algorithmVar, value=5,
				command= self.selectOptimizationAlgorithm,style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		self.SAButton.pack(anchor = W  )
		
		
		optimizationMethodsLabelStlye = Style()
		optimizationMethodsLabelStlye.configure("OptimizationFrame.TLabel", foreground="midnight blue", background="SkyBlue2")

		#self.saLabel = Label(self.optimizationMethodsFrame, text="Simulate Annealing (Not Yet Implemented)", style = 'OptimizationFrame.TRadiobutton')#background='SkyBlue2')
		#self.saLabel.pack(anchor = W  )
		
		
		optimizationMethodsButtonStlye = Style()
		optimizationMethodsButtonStlye.configure("OptimizationFrame.TButton", foreground="black", background="SkyBlue2", font = ("Cambria",12,))
		
		self.algoInfoButton = Button(self.optimizationMethodsFrame, text = 'Display Information', command = self.displayInfo,style = 'OptimizationFrame.TButton')#background='SkyBlue2')
		self.algoInfoButton.pack(pady = 40 )

		#NOTE: Middle column = input data
		
		
		
		dataFrameStlye = Style()
		dataFrameStlye.configure("Data.TLabelframe", foreground="black", background="SkyBlue3")
		dataFrameStlye.configure("Data.TLabelframe.Label", foreground="midnight blue", background="SkyBlue3", font = ("Cambria",16,))

		
		self.dataFrame = LabelFrame(self, text="Input Data", style = "Data.TLabelframe")#background='SkyBlue3')
		self.dataFrame.grid(row = 1, column = 1, sticky = W +E + N + S)

		#self.listOfOptimizationMethods = Label(self.optimizationMethodsFrame,)
		#self.listOfOptimizationMethods .pack()
		
		dataRadioButtonStlye = Style()
		dataRadioButtonStlye.configure("DataFrame.TRadiobutton", foreground="midnight blue", background="SkyBlue3", font = ("Cambria",12,))
		
		self.stockVar = IntVar()
		
		self.dowButton = Radiobutton(self.dataFrame, text="Dow Jones Industrial Average (DJIA)", variable=self.stockVar, value=0,command = self.printS, style ="DataFrame.TRadiobutton" )#background='SkyBlue3')
		self.dowButton.grid(row=0, sticky = W)
		
		
		self.spButton = Radiobutton(self.dataFrame, text="S&P 500 (^GSPC)", variable=self.stockVar, value=1,command = self.printS, style ="DataFrame.TRadiobutton")#background='SkyBlue3')
		self.spButton.grid(row=1, sticky = W)


		self.nasdaqButton = Radiobutton(self.dataFrame, text="NASDAQ (^IXIC)", variable=self.stockVar, value=2,command = self.printS, style ="DataFrame.TRadiobutton")#background='SkyBlue3')
		self.nasdaqButton.grid(row=2, sticky = W)
		
		
		self.russelButton = Radiobutton(self.dataFrame, text="Russel 3000 (^RUA)", variable=self.stockVar, value=3,command = self.printS, style ="DataFrame.TRadiobutton")#background='SkyBlue3')
		self.russelButton.grid(row=3, sticky = W)
		
		
		#self.psoButton = Radiobutton(self.dataFrame, text="Particle Swarm Evolution (Recommended)", variable=self.algorithmVar, value=4,
				#command= self.selectOptimizationAlgorithm)
		#self.psoButton.grid(row=4, sticky = W)
		
		
		self.enterStockButton = Radiobutton(self.dataFrame, text="Enter Stock Symbol: ", variable=self.stockVar, value=4,command = self.printS, style ="DataFrame.TRadiobutton")#background='SkyBlue3')
		self.enterStockButton.grid(row=4, sticky = W)

		self.tickerSymbol = self.arrayofIndicies[0]
		
		#self.tickerLabel = Label(self.dataFrame, text="Enter Stock Symbol: ")
		#self.tickerLabel.grid(row=5, sticky = W)
		#Label(self, text="Enter Ticker: ").grid(row=0)
		#Label(self, text="Second").grid(row=1)
		
		dataTextStlye = Style()
		dataTextStlye.configure("DataFrame.TEntry", foreground="black", background="SkyBlue3", font = ("Cambria",12,))
		
		self.tickerTextBox = Entry(self.dataFrame, state = 'disabled', style = "DataFrame.TEntry")
		self.tickerTextBox.grid(row=4, column = 1)

		dataLabelStlye = Style()
		dataLabelStlye.configure("DataFrame.TLabel", foreground="midnight blue", background="SkyBlue3", font = ("Cambria",12,))
			
		self.datesLabel = Label(self.dataFrame, text="Enter Sample Dates (YYYY-MM-DD): ", style = "DataFrame.TLabel")#background='SkyBlue3')
		self.datesLabel.grid(row=7, sticky = W)


		#self.fromLabel = Label(self.dataFrame, text="to", style = "DataFrame.TLabel", font = ("Cambria",12,))#background='SkyBlue3')
		#self.fromLabel.grid(row=8, column = 1)


		self.date1TextBox = Entry(self.dataFrame, )
		self.date1TextBox.grid(row=8, column=0)
		
		self.date1TextBox.insert(0, "Start Date")


		#date1TextBox.configure(state='disabled')

		self.toLabel = Label(self.dataFrame, text="to", style = "DataFrame.TLabel", font = ("Cambria",12,))#background='SkyBlue3')
		self.toLabel.grid(row=8, column = 1)

		self.date2TextBox = Entry(self.dataFrame, text = 'From')
		self.date2TextBox.grid(row=8, column = 2)
		
		self.date2TextBox.insert(0, "End Date")
		
		
		self.pressed = 0


		dataCheckStlye = Style()
		dataCheckStlye.configure("DataFrame.TCheckbutton", foreground="midnight blue", background="SkyBlue3", font = ("Cambria",12,))
		
		
		self.selectAllDatesCheckBox = Checkbutton(self.dataFrame, text = 'Select all possible dates', variable = self.pressed, command = self.disableDates, onvalue = 1, offvalue = 0, style  ="DataFrame.TCheckbutton")#background='SkyBlue3')
		self.selectAllDatesCheckBox.grid(row = 8, column = 3)
		
		self.selectAllDatesCheckBox.invoke()
		self.selectAllDatesCheckBox.invoke()
		
		self.startDate = ''
		self.endDate = ''
		if self.pressed == 1:
			self.date1TextBox.configure(state='disabled')
			self.date2TextBox.configure(state='disabled')
		if self.pressed == 0: 
			self.date1TextBox.configure(state='normal')
			self.date2TextBox.configure(state='normal')
		
		dataButtonStlye = Style()
		dataButtonStlye.configure("DataFrame.TButton", foreground="black", background="SkyBlue3", font = ("Cambria",12,))
		
		self.makeGraphButton = Button(self.dataFrame, text = 'Display Graph of Close Data', command = self.displayGraphOfCloseData, style ="DataFrame.TButton" )#background='SkyBlue3')
		self.makeGraphButton.grid(row = 9, columnspan = 4, pady = 20)
		
		
		
		print('got here')
		#NOTE: Right most column = run
		
		
		runFrameStlye = Style()
		runFrameStlye.configure("RunFrame.TLabelframe", foreground="black", background="SkyBlue2")
		runFrameStlye.configure("RunFrame.TLabelframe.Label", foreground="midnight blue", background="SkyBlue2", font = ("Times New Roman",16,))
		#runFrameStlye.configure("RunFrame.TFrame", foreground="black", background="SkyBlue4")
		
		
		self.runFrame = LabelFrame(self, text="Run Algorithm", style = "RunFrame.TLabelframe")#background='SkyBlue4')
		self.runFrame.grid(row = 1, column = 2, sticky = W +E + N + S)
		
		runButtonStlye = Style()
		runButtonStlye.configure("RunFrame.TButton", foreground="black", background="SkyBlue2", font = ("Cambria",12,))
		
		self.goButton = Button(self.runFrame, text = 'Find Best Crossover', command = self.getBestCrossover, style = "RunFrame.TButton")#background='SkyBlue4')
		self.goButton.grid(row = 0)


		runLabelStlye = Style()
		runLabelStlye.configure("RunFrame.TLabel", foreground="midnight blue", background="SkyBlue2", font = ("Cambria",12,))

		#self.bestCrossoverLabel = Label(self.runFrame, text='The Best Crossover is: ', style = "RunFrame.TLabel")#background='SkyBlue4')
		self.bestCrossoverLabel = Label(self.runFrame, style = "RunFrame.TLabel")#background='SkyBlue4')
		self.bestCrossoverLabel.grid(row=1, column = 0)
	
		self.answerText = ''
		self.answerLabel = Label(self.runFrame, text= self.answerText,style = "RunFrame.TLabel")#background='SkyBlue4')
		self.answerLabel.grid(row=1, column = 1)
		
		
	def printS(self):
		if self.stockVar.get() != 4:
			self.tickerTextBox.configure(state='disabled')
		else: 
			self.tickerTextBox.configure(state='normal')
			
		

		if self.stockVar.get() != 4:
			self.tickerSymbol = self.arrayofIndicies[self.stockVar.get()]		
		
		else:
			self.tickerSymbol = self.tickerTextBox.get()
		
		if self.pressed == 1:
			self.selectAllDatesCheckBox.invoke()
		self.pressed = 0
		self.date1TextBox.configure(state='normal')
		self.date2TextBox.configure(state='normal')
		
		print(self.tickerSymbol)
	
	def getBestCrossover(self):
		from pprint import pprint
		
		#self.tickerSymbol = self.tickerTextBox.get()

		if self.stockVar.get() == 4:
			self.tickerSymbol = self.tickerTextBox.get()
		print(self.pressed)
		if self.pressed == 0:	#Box not checked
			self.startDate = self.date1TextBox.get()
			self.endDate = self.date2TextBox.get()
		#print(startDate, endDate)
		#print((ystockquote.get_historical_prices(tickerSymbol, startDate, endDate).keys()))
		#print(str(ystockquote.get_historical_prices(tickerSymbol, startDate, endDate)))
		entireDictionaryOfData = ystockquote.get_historical_prices(self.tickerSymbol, self.startDate, self.endDate)
		#entireDictionaryOfData = ystockquote.get_historical_prices('CAS', '2013-11-01', '2013-11-05')
		#pprint(entireDictionaryOfData.keys())
		
		listOfDates = self.getListOfDatesFromHistoricalData(entireDictionaryOfData)
		#print(listOfDates)
		listOfCloses = self.getListOfClosesFromHistoricalData(entireDictionaryOfData,listOfDates)
		#print(entireStringOfData.find("'Close'"))
		#print(ystockquote.get_trade_date('GOOG'))
		
		
		#theBestCrossover = PSO.runPSO(listOfCloses)
		
		if self.algorithmVar.get() == 0:
			theBestCrossover = HillClimbing.runHillClimbing(listOfCloses)
		if self.algorithmVar.get() == 1:
			theBestCrossover = NelderMeadNew.runNelderMead(listOfCloses)
		if self.algorithmVar.get() == 2:
			theBestCrossover = GeneticAlgorithms.runGA(listOfCloses)
		if self.algorithmVar.get() == 3:
			theBestCrossover = DifferentialEvolution.runDE(listOfCloses)
		if self.algorithmVar.get() == 4:
			theBestCrossover = PSO.runPSO(listOfCloses)
		if self.algorithmVar.get() == 5:
			theBestCrossover = SA.runSA(listOfCloses)
			#theBestCrossover = PSO.figureOutBestConstants(listOfCloses)
			

		#theBestCrossover = NelderMeadNew.runNelderMead(listOfCloses)

		
		
		shortLength = theBestCrossover[0]
		longLength = theBestCrossover[1]
		
		if shortLength > longLength: 
			shortLength, longLength = longLength, shortLength
		#return ('Short Length = '', Long Length = ').format(shortLength, longLength
		#print(listOfDates)
		self.bestCrossoverLabel['text'] = 'The Best Crossover is: '
		self.answerLabel['text'] = 'Short Length = '+ str(shortLength) + ', Long Length = ' + str(longLength)
		
		self.makeGraph(listOfCloses, listOfDates, self.tickerSymbol, shortLength, longLength)
		#return 'Short Length = '+ str(shortLength) + ', Long Length = ' + str(longLength)
		#displayGraph()
	
	def disableDates(self):
		if self.pressed == 0:
			self.pressed = 1
		else:
			self.pressed = 0
		#print(self.pressed)
		if self.pressed == 1:
			self.date1TextBox.configure(state='disabled')
			self.date2TextBox.configure(state='disabled')
			self.startDate = '1900-01-01'
			
			if self.stockVar.get() == 4:
				self.tickerSymbol = self.tickerTextBox.get()
				
			self.endDate = ystockquote.get_last_trade_date(self.tickerSymbol)
			month = self.endDate[1 : self.endDate.find('/')]
			if month in ['1','2','3','4','5','6','7','8','9']:
				month = '0' + month
			print(month)
			day = self.endDate[self.endDate.find('/') + 1 : self.endDate.rfind('/')]
			if day in ['1','2','3','4','5','6','7','8','9']:
				day = '0' + day
			print(day)
			year = self.endDate[self.endDate.rfind('/') + 1 : len(self.endDate) - 1]
			#print(self.endDate)
			print(year)#, month, day)
			self.endDate = year + '-' + month + '-' + day
			print(self.startDate, self.endDate)
		if self.pressed == 0: 
			self.date1TextBox.configure(state='normal')
			self.date2TextBox.configure(state='normal')
			
	def __init__(self, master=None):
	
		
		Frame.__init__(self, master)#background='IndianRed4')
		

		#self.config()
		self.pack()
		self.createWidgets()
		
	def getListOfDatesFromHistoricalData(self, entireDictionaryOfData):
		listOfDates = []
		
		#startYear = startDate[0 : startDate.find('-')]
		#startMonth = startDate[startDate.find('-') + 1 : startDate.rfind('-')]
		#startDay = startDate[startDate.rfind('-') + 1 : len(startDate)]
		
		#endYear = endDate[0 : endDate.find('-')]
		#endMonth = endDate[endDate.find('-') + 1 : endDate.rfind('-')]
		#endDay = endDate[endDate.rfind('-') + 1 : len(endDate)]
		#for year in range(startYear, endYear + 1): 	#The second index in range is non-inclusive
			#for month in range(startYear, endYear + 1): 	#The second index in range is non-inclusive
				#for year in range(startYear, endYear + 1): 	#The second index in range is non-inclusive
		listOfDates = list(entireDictionaryOfData.keys())
		listOfDates.sort()
		#print('Yo',listOfDates)
		#for dateString in entireDictionaryOfData.keys():
			#print(dateString)
			#dateString = dateString.strip()
			#listOfDates.append(dateString)
			##year = dateString[0 : dateString.find('-')]
			###print(year)
			##month = dateString[dateString.find('-') + 1 : dateString.rfind('-')]
			###print(month)
			##day = dateString[dateString.rfind('-') + 1 : len(dateString)]
			###print(day)
		##listOfDates.sort()
		#print(listOfDates)
		return listOfDates[:]
	
	def getListOfClosesFromHistoricalData(self,entireDictionaryOfData, listOfDates):
		listOfCloses = []
		for key in listOfDates:
			dictionaryOfDataForOneDate = entireDictionaryOfData[key]
			#print(dateString)
			closeOfThisDate = float(dictionaryOfDataForOneDate['Close'])
			#dateString = dateString.strip()
			listOfCloses.append(closeOfThisDate)
			#year = dateString[0 : dateString.find('-')]
			##print(year)
			#month = dateString[dateString.find('-') + 1 : dateString.rfind('-')]
			##print(month)
			#day = dateString[dateString.rfind('-') + 1 : len(dateString)]
			##print(day)
		#print(listOfCloses)
		return listOfCloses[:]
	
	def displayGraphOfCloseData(self):

		from pprint import pprint
		
		#self.tickerSymbol = self.tickerTextBox.get()

		#if self.stockVar.get() != 4:
			#self.tickerSymbol = self.arrayofIndicies[self.stockVar.get()]
			#print(self.tickerSymbol)
		
		if self.stockVar.get() == 4:
			self.tickerSymbol = self.tickerTextBox.get()
			
		print(self.pressed)
		if self.pressed == 0:	#Box not checked
			self.startDate = self.date1TextBox.get()
			self.endDate = self.date2TextBox.get()
		#print(startDate, endDate)
		#print((ystockquote.get_historical_prices(tickerSymbol, startDate, endDate).keys()))
		#print(str(ystockquote.get_historical_prices(tickerSymbol, startDate, endDate)))
		entireDictionaryOfData = ystockquote.get_historical_prices(self.tickerSymbol, self.startDate, self.endDate)
		#entireDictionaryOfData = ystockquote.get_historical_prices('CAS', '2013-11-01', '2013-11-05')
		#pprint(entireDictionaryOfData.keys())
		
		completeListOfDates = self.getListOfDatesFromHistoricalData(entireDictionaryOfData)
		#print(listOfDates)
		completeListOfCloses = self.getListOfClosesFromHistoricalData(entireDictionaryOfData,completeListOfDates)
		
		
		
		t = completeListOfCloses
		s = completeListOfDates

		dateList = []
		for string in s:
			#print(string)
			year = string[ : string.find('-')]
			month = string[string.find('-') + 1 : string.rfind('-')]
			day = string[string.rfind('-') + 1 : len(string)]
			#print(year, month, day)
			dateList.append(datetime.date( int(year), int(month), int(day) ))

		#print(t)
		#s = math.sin(t)
		#import sys
		#sys.exit()
		fig, ax = plt.subplots()

		plt.plot(dateList,t, label = 'Daily Close')
		
	
		datemin = dateList[0]
		datemax = dateList[len(dateList) - 1]
		ax.set_xlim(datemin, datemax)
		
		
		
		ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
		#ax.format_ydata = price

		#graph.set_ylim(0, 3000)

		fig.autofmt_xdate()



		# Create plots with pre-defined labels.
		# Alternatively, you can pass labels explicitly when calling `legend`.

		#ax.plot(t, c, 'k--', label='Model length')
		#ax.plot(shortSMALegnthList, d, 'k:', label='Data length')
		#ax.plot(longSMALegnthList, c+d, 'k', label='Total message length')

		# Now add the legend with some customizations.
		legend = ax.legend(loc='upper center', shadow=True)

		legend.draggable(True)
		# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
		frame  = legend.get_frame()
		frame.set_facecolor('0.90')
		
		# Set the fontsize
		for label in legend.get_texts():
			label.set_fontsize('large')

		for label in legend.get_lines():
			label.set_linewidth(1.5)  # the legend line width

		plt.xlabel('Date')
		plt.ylabel('Close')
		plt.title(self.tickerSymbol)
		plt.grid(True)
		plt.savefig("test.png")  
		
		

		
		plt.show()


	def makeGraph(self,completeListOfCloses, completeListOfDates, stockSymbol, shortSMALegnth, longSMALegnth):
		
		

		t = completeListOfCloses
		s = completeListOfDates

		dateList = []
		for string in s:
			#print(string)
			year = string[ : string.find('-')]
			month = string[string.find('-') + 1 : string.rfind('-')]
			day = string[string.rfind('-') + 1 : len(string)]
			#print(year, month, day)
			dateList.append(datetime.date( int(year), int(month), int(day) ))

		#print(t)
		#s = math.sin(t)
		#import sys
		#sys.exit()
		fig, ax = plt.subplots()

		plt.plot(dateList,t, label = 'Daily Close')
		
		
		
		shortSMALegnthList = []
		
		for i in range(0, len(dateList)):
			shortSMALegnthList.append(calculateSMA(completeListOfCloses, 2, i))
		
		
		longSMALegnthList = []
		
		for i in range(0, len(dateList)):
			longSMALegnthList.append(calculateSMA(completeListOfCloses, 6, i))
		
		#shortLabel = 
		#longLabel = 
		plt.plot(dateList,shortSMALegnthList, label = 'Short SMA Length: ' +  str(shortSMALegnth) + ' Days')
		plt.plot(dateList,longSMALegnthList, label = 'Long SMA Length: ' + str(longSMALegnth) + ' Days')
		
		#graph.plot(t)
		#years    = mdates.YearLocator()   # every year
		#months   = mdates.MonthLocator()  # every month
		#yearsFmt = mdates.DateFormatter('%Y')

		#graph.xaxis.set_major_locator(years)
		#graph.xaxis.set_major_formatter(yearsFmt)
		#graph.xaxis.set_minor_locator(months)
		
		datemin = dateList[0]
		datemax = dateList[len(dateList) - 1]
		ax.set_xlim(datemin, datemax)
		
		
		
		ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
		#ax.format_ydata = price

		#graph.set_ylim(0, 3000)

		fig.autofmt_xdate()



		# Create plots with pre-defined labels.
		# Alternatively, you can pass labels explicitly when calling `legend`.

		#ax.plot(t, c, 'k--', label='Model length')
		#ax.plot(shortSMALegnthList, d, 'k:', label='Data length')
		#ax.plot(longSMALegnthList, c+d, 'k', label='Total message length')

		# Now add the legend with some customizations.
		legend = ax.legend(loc='upper center', shadow=True)

		legend.draggable(True)
		# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
		frame  = legend.get_frame()
		frame.set_facecolor('0.90')
		
		# Set the fontsize
		for label in legend.get_texts():
			label.set_fontsize('large')

		for label in legend.get_lines():
			label.set_linewidth(1.5)  # the legend line width

		plt.xlabel('Date')
		plt.ylabel('Close')
		plt.title(stockSymbol)
		plt.grid(True)
		plt.savefig("test.png")  
		
		

		
		plt.show()

def about():
	print('hi')
	
def aboutWindow():
	print('yoyoyoy')
	t = Toplevel()	

	t.wm_title("About this Application",)
	#l = Label(t, wraplength = 500, text= "Hill Climbing operates based on the analogy of a climber ascending a mountain in the dark. The algorithm starts at a random position, and checks that position's neighbors. The algorithm then assumes the position of the best neighbor. If no neighbors are better than the current position, the algorithm has finished.")
	
	#frame = Frame(t)
	#frame.pack(expand = True, fill = 'both')
	text = Text(t)

	#aboutTextFile = file('about.txt') # get a file handle
	
	aboutTextFile = open('about.txt', mode = 'r')
	
	aboutText = aboutTextFile.read() # read the file to variable
	#print(aboutText)
	aboutTextFile.close() # close file handle

	text.insert(0.0,aboutText) # insert the file's text into the text
	
	aboutGraph = PhotoImage(file="about.gif")
	text.image = aboutGraph
	#print(t.winfo_reqwidth())
	text.image_create(INSERT, image =  aboutGraph)#, padx = t.winfo_reqwidth()//2)
	
	
	aboutText2File = open('about2.txt', mode = 'r')
	
	aboutText2 = aboutText2File.read() # read the file to variable
	#print(aboutText)
	aboutText2File.close() # close file handle

	text.insert(END,aboutText2) # insert the file's text into the textBox
	
	aboutFormulas = PhotoImage(file="aboutFormulas.gif")
	text.image2 = aboutFormulas
	#print(t.winfo_reqwidth())
	text.image_create(INSERT, image =  aboutFormulas)#, padx = t.winfo_reqwidth()//2)
	
	
	aboutText3File = open('about3.txt', mode = 'r')
	
	aboutText3 = aboutText3File.read() # read the file to variable
	#print(aboutText)
	aboutText3File.close() # close file handle

	text.insert(END,aboutText3) # insert the file's text into the textBox
	
	text.config(state = 'disabled')
	text.pack(expand = True, fill = 'both')

	
	#photo = PhotoImage(file="hillClimbing.gif")
	#w = Label(t, image=photo)
	#w.photo = photo
	#w.pack()



def do():
	print('ggg')
	
	
def main():
	root = Tk()
	root.wm_title('Optimizing Simple Moving Average Crossovers')
	
	print('ypypypypyp')
   
	
	menubar = Menu(root, )#background = 'red', foreground = 'red')
	#filemenu = Menu(menubar, tearoff=0)
	#filemenu.add_command(label="New", command=donothing)
	#filemenu.add_command(label="Open", command=donothing)
	#filemenu.add_command(label="Save", command=donothing)
	#filemenu.add_command(label="Save as...", command=donothing)
	#filemenu.add_command(label="Close", command=donothing)

	#filemenu.add_separator()

	#filemenu.add_command(label="Exit", command=root.quit)
	
	#menuStlye = Style()
	#menuStlye.configure("Menu.TMenubutton", foreground="black", background="IndianRed4", )
	
	
	menubar.add_command(label="About", command = aboutWindow,  ) #background = 'red', foreground = 'red')
	#editmenu = Menu(menubar, tearoff=0)
	#editmenu.add_command(label="Undo", command=donothing)

	#editmenu.add_separator()

	#editmenu.add_command(label="Cut", command=donothing)
	#editmenu.add_command(label="Copy", command=donothing)
	#editmenu.add_command(label="Paste", command=donothing)
	#editmenu.add_command(label="Delete", command=donothing)
	#editmenu.add_command(label="Select All", command=donothing)

	#menubar.add_cascade(label="Edit", menu=editmenu)
	#helpmenu = Menu(menubar, tearoff=0)
	#helpmenu.add_command(label="Help Index", command=donothing)
	#helpmenu.add_command(label="About...", command=donothing)
	#menubar.add_cascade(label="Help", menu=helpmenu)
	
	
	#s = Style()
	#s.theme_use('vista')
	#root.config(menu=menubar)
	
	
	root.config(menu=menubar,)
	#root.configure(background='black')
	app = Application(master=root)
	app.mainloop()
	root.destroy()



if __name__ == '__main__': main()
