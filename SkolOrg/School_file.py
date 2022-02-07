class School:

    def __init__(self,Id, Name, Adress, Student):
        self.Id = Id
        self.Name = Name
        self.Adress = Adress
        self.Student = Student

        def __str__(self):
            return f"Id:{self.Id} Name:{self.Name} Adress:{self.Adress}  Student:{self.student}"

        """
        Id, Name, Adress, Student
        Datatyper: String, String, String, [Student]
        """
        pass

    def add_student(self):
        """Lägg till en elev"""
        pass

    def remove_student(self):
        """Ta bort en specifik elev"""
        pass

    def remove_class(self):
        """Ta bort alla elever från en specifik klass"""
        pass

    def change_address(self):
        pass
