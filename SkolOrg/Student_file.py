class Student:

    def __init__(self):
        """Varje elev ska ha dessa attribut:
        Personnummer, Namn, Ålder, Klass, Skola
        Datatyper: String, String, Int, String, School"""
        pass

    def __eq__(self, other):
        return self.personnr == other

    def change_school(self):
        pass