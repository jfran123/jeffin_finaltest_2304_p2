class Server:
    def __init__(self, name):
        self.name = name
        self.duties = 'clear tables, mop the floor, take payment, serve customer'.split(',')

    def __str__(self):
        return f"My name is {self.name} and I am responsible for: {self.duties}"


class TeamLeader(Server):
    def __init__(self, name):
        super().__init__(name)
        self.duties.extend('check attendance, assign duty'.split(','))


class Manager(TeamLeader):
    def __init__(self, name):
        super().__init__(name)
        self.duties.extend('create schedule, hire staff'.split(','))


s = Server('John')
print(s)    
t = TeamLeader('Alice')
print(t)
m = Manager('Bob')  
print(m)
