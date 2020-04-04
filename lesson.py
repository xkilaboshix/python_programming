class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S')
tesla_car.__enable_auto_run = "XXXXXXXXXXXXX"
print(tesla_car.__enable_auto_run)

class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

