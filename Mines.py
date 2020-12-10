import Resources as r


class IronMine:
    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = False
        self.max_ticks = 5
        self.production_tick_counter = self.max_ticks
        self.output = {}

    def is_consumer(self):
        return self.consumer

    def is_producer(self):
        return self.producer

    def decrement_output(self, resource):
        if resource in self.output and self.output[resource] > 0:
            self.output[resource] = self.output[resource] - 1

    def increment_output(self, resource):
        if resource in self.output:
            self.output[resource] = self.output[resource] + 1
        else:
            self.output[resource] = 1

    def tick(self):
        if self.production_tick_counter <= 1:
            self.production_tick_counter = self.max_ticks
            self.increment_output(r.iron)
        else:
            self.production_tick_counter -= 1
            
            
class CoalMine:
    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = False
        self.max_ticks = 5
        self.production_tick_counter = self.max_ticks
        self.output = {}

    def is_consumer(self):
        return self.consumer

    def is_producer(self):
        return self.producer

    def decrement_output(self, resource):
        if resource in self.output and self.output[resource] > 0:
            self.output[resource] = self.output[resource] - 1

    def increment_output(self, resource):
        if resource in self.output:
            self.output[resource] = self.output[resource] + 1
        else:
            self.output[resource] = 1
        
    def tick(self):
        if self.production_tick_counter <= 1:
            self.production_tick_counter = self.max_ticks
            self.increment_output(r.coal)
        else:
            self.production_tick_counter -= 1
