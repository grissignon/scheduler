import datetime
import time
import threading


stop_thread = False
global_fifo= []

################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task(threading.Thread):


	name = None
	period = None
	execution_time = None


    	############################################################################
	def __init__(self, name, period, execution_time, fifo_write = False):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.fifo_write = fifo_write
		
		threading.Thread.__init__(self)

    	############################################################################
	def run(self):

		global global_fifo

		while(not stop_thread):
				
			print(self.name + " : Starting task")
			
			if (self.fifo_write == True) :
			
				global_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
			
			else :
				while (len(global_fifo) > 0):
					print(self.name + " : " + global_fifo[0])
					del global_fifo[0]	


			
			time.sleep(self.execution_time)
			print(self.name + " : Stopping task")
			time.sleep(self.period - self.execution_time)




	
####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':


	task_list = []

	# Instanciation of task objects

	task_list.append(my_task(name="thread_1", period=5, execution_time=2, fifo_write=True))
	task_list.append(my_task(name="thread_2", period=15, execution_time=3, fifo_write=True))


	for current_task in task_list :
		current_task.start()










