class IronMine:
    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = False
        self.max_ticks = 5
        self.tick_counter = self.max_ticks
        self.output = {}
        self.input = {}
        
    def is_consumer(self):
        return self.consumer
        
    
    def is_producer(self):
        return self.producer
        
        
    def tick(self):
        if self.tick_counter <= 1:
            self.tick_counter = self.max_ticks
            if "iron" in self.output:
                self.output["iron"] += 1
            else:
                self.output["iron"] = 1
        else:
            self.tick_counter -= 1
            
            
class CoalMine:
    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = False
        self.max_ticks = 5
        self.tick_counter = self.max_ticks
        self.output = {}
        self.input = {}
        
        
    def is_consumer(self):
        return self.consumer
        
    
    def is_producer(self):
        return self.producer
        
        
    def tick(self):
        if self.tick_counter <= 1:
            self.tick_counter = self.max_ticks
            if "coal" in self.output:
                self.output["coal"] += 1
            else:
                self.output["coal"] = 1
        else:
            self.tick_counter -= 1
