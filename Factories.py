import Resources as r


class SteelFactory:
    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = True
        self.production_tick_counter = 5
        self.output = {}
        self.input = {}
        self.production_threshold = {
            r.coal: 1,
            r.iron: 1
        }
        self.is_consuming = False

    def is_consumer(self):
        return self.consumer

    def is_producer(self):
        return self.producer

    def decrement_input(self, resource):
        self.input[resource] = self.input[resource] - 1

    def increment_input(self, resource):
        if resource in self.input:
            self.input[resource] = self.input[resource] + 1
        else:
            self.input[resource] = 1

    def meets_production_threshold(self):
        if r.coal in self.input and r.iron in self.input:
            return self.input[r.coal] >= self.production_threshold[r.coal] \
                   and self.input[r.iron] >= self.production_threshold[r.iron]
        else:
            return False

    def tick(self):
        if self.meets_production_threshold() or self.is_consuming:
            self.is_consuming = True
            self.decrement_input(r.coal)
            self.decrement_input(r.iron)
            self.production_tick_counter -= 1
            if self.production_tick_counter <= 0:
                self.is_consuming = False
                self.production_tick_counter = 5
