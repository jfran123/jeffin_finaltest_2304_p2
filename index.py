class Professor:
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def __str__(self):        return f"Professor {self.name} from {self.department} department"
    def greet(self):
        return f"Hello, My name is {self.name} and I teach in {self.department} department."
    
ilia=Professor("Ilia","ICET")
print(ilia.greet())

sonali=Professor("Sonali","Math")
print(sonali.greet())

class Instructor:
        def __init__(self,name,department,courses=None):
            self.name=name
            self.department=department
            self.courses=courses if courses is not None else []
        def __str__(self):
            return f"Hello, my name is {self.name} and I teach {self.courses} in {self.department}"
        def add_course(self,course):
            self.courses.append(course)
        def remove_course(self,course):
            if course in self.courses:
                self.courses.remove(course)

print("\nCreating first object")
ilia=Instructor("Ilia","ICET","Python,Data Science".split(","))
print(ilia)
course="Machine Learning"
print(f"\nAdding course :{course}")
ilia.add_course(course)
print(ilia)


print("\nCreating second object")
arben=Instructor("Arben","ICET",['Java','Database'])
print(arben)
course="Java"
print(f"\nRemoving course :{course}")
arben.remove_course(course)
print(arben)