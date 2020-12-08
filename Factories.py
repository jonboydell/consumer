class SteelFactory:
    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = True
        self.max_ticks = 5
        self.tick_counter = self.max_ticks
        self.output = {}
        self.input = {}
        
    def is_consumer(self):
        return self.consumer
        
    
    def is_producer(self):
        return self.producer
        
        
    def tick(self):
    	  if 'coal' in self.input and 'iron' in self.input:
          c = self.input['coal']
          i = self.input['iron']
	        if self.tick_counter <= 1:
	            self.tick_counter = self.max_ticks
	            if "steel" in self.output:
	                self.output["steel"] += 1
	            else:
	                self.output["steel"] = 1
	        else:
	            self.tick_counter -= 1
            
            
