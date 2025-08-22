class Employees:
    def __init__(self, name, e_id, salary):
        self.name = name
        self.e_id = e_id
        self.salary = salary
    
    def login(self):
        print(f"{self.name} has logged in")

    def logout(self):
        print(f"{self.name} has logged out")

    def taskCompleted(self):
        print(f"{self.name} has completed a task")

    def show_salary(self):
        print(f"{self.name}'s salary is {self.salary}")

employee1 = Employees("Sumit", 1,50000)
# employee1.login()
# employee1.taskCompleted()
# employee1.logout()
# employee1.show_salary()

employee2 = Employees("Rohit", 2,60000)
employee2.login()
employee2.taskCompleted()
employee2.logout()
employee2.show_salary()