import Resources as r


class SteelFactory:
    production_tick_threshold = 5

    def __init__(self, name):
        self.name = name
        self.producer = True
        self.consumer = True
        self.production_tick_counter = self.production_tick_threshold
        self.output = {r.steel: 0}
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

    def increment_output(self, resource):
        if resource in self.output:
            self.output[resource] = self.output[resource] + 1
        else:
            self.output[resource] = 1

    def meets_production_threshold(self):
        if r.coal in self.input and r.iron in self.input:
            return self.input[r.coal] >= self.production_threshold[r.coal] \
                   and self.input[r.iron] >= self.production_threshold[r.iron]
        else:
            return False

    def tick(self):
        if self.meets_production_threshold() and not self.is_consuming:
            self.decrement_input(r.coal)
            self.decrement_input(r.iron)
            self.is_consuming = True

        if self.is_consuming:
            self.production_tick_counter -= 1
            if self.production_tick_counter <= 0:
                self.is_consuming = False
                self.production_tick_counter = self.production_tick_threshold
                self.increment_output(r.steel)
