
import math

def calculateStats(numbers):
  if(len(numbers)>0):
    avgValue = sum(numbers) / len(numbers)
    minimum_value = min(numbers)
    maximum_value = max(numbers)
    return { 'avg':avgValue, 'min':maximum_value, 'max':minimum_value }
  else:
    return { 'avg':math.nan, 'min':math.nan, 'max':math.nan }

class LEDAlert:
	def __init__(self):
		self.led_glows = False
  
class EmailAlert:
  def __init__(self):
    self.email_sent=False
    
class StatsAlerter:
	def __init__(self, maxThreshold, alertList):
		self.max_threshold = maxThreshold
		self.alert_list = alertList
		
	def checkAndAlert(self, values):
		result = calculateStats(values)
		if result["max"] > self.maxThreshold:
			self.alertList[0].email_sent = True
			self.alertList[1].led_glows = True
