#!/usr/bin/env python
import time

class Timer:
	start = None
	stop = None
	result = None

	def __init__(self):
		pass

	def start(self):
		self.start = time.time()
		self.result = 0
		return self.start

	def stop(self):
		self.stop = time.time()
		self.result = self.stop - self.start
		self.start = 0
		return self.stop

	def time(self):
		return self.result




t = Timer()
print "start: %f" % t.start()
i = 0
for i in range(1000000):
	i += i
print " stop: %f" % t.stop()
print " time: %f" % t.time()
