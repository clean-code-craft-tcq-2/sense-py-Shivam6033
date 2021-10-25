import math

def calculateStats(numbers):
  if(len(numbers)>0):
    avgValue = sum(numbers) / len(numbers)
    minimumValue = min(numbers)
    maximumValue = max(numbers)
    return { 'avg':avgValue, 'min':minimumValue, 'max':maximumValue }
  else:
    return { 'avg':math.nan, 'min':math.nan, 'max':math.nan }

class LEDAlert:
	def __init__(self):
		self.ledGlows = False 
  
class EmailAlert:
  def __init__(self):
    self.emailSent=False #Default = No Glow
    
class StatsAlerter:
	def __init__(self, maxThreshold, alertList):
		self.maxThreshold = maxThreshold
		self.alertList = alertList
		
	def checkAndAlert(self, values):
		result = calculateStats(values)
		if result["max"] > self.maxThreshold:
			self.alertList[0].emailSent = True
			self.alertList[1].ledGlows = True
