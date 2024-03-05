class Employee:
    def __init__(self,surname,position,salary) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary
 
class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary,rating) -> None:
        super().__init__(surname, position, salary)
        self.rating = rating
       
    def change_salary(self):
        if 60 <= self.rating < 75:
            self.salary += self.salary *1.2
        elif 75 <= self.rating < 90:
            self.salary += self.salary *1.4
        elif 90 <= self.rating <= 100:
            self.salary += self.salary * 1.6
    def get_full_info(self):
        return f"""

Name : {self.surname}
Position : {self.position}
Salary : {self.salary}
Rating : {self.rating}

"""


worker1 = Enterprise_employee("Juraev","Main CEO",1000,100)
worker2 = Enterprise_employee("Yusupob","Engineer",100,70)
worker3 = Enterprise_employee("Haydarov","Accounter",200,80)
worker4 = Enterprise_employee("Toirova","Manager",300,90)
worker5 = Enterprise_employee("Turg'unova","Secretary",700,95)

print(worker1.get_full_info())
lst= [worker1, worker2, worker3, worker4, worker5]
for worker in lst:
    print(worker.get_full_info())


