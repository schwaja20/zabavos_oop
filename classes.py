"""
kazda clasa ma nazev s VELKYM PISMENKEM!!!!!!!!!!
trida vs objekt > podle obj muzeme vytvorit predpis tridy, tri da je to co definuje jak bude dana vec vypadat
instance = triad do ktere nasypu data

1. definovat atributy

_ = podrtzitko mame jen pro rozliseni a lepsi orientaci v programu --> nemusi tam byt
ve trech uvozovkach ma byt popis te classy, co to dela atd

pokud jsou jen pred atributem 2 podrtzitka povazuje se za privatni --> nedostanu se k ni

privatni: napr.: check if file exists = overeni existence veci
"""


class Person():
    """
    Class that represents a person
    """

    def __init__(self, _name, _birth, _email_adress):
        self.name = _name
        self.birth = _birth
        self.email_adress = _email_adress
        self.__adress = None

    def __str__(self):
        return "Hello, I am " + self.name

    def get_age(self):
        return 2022 - self.birth

    def purchase_parking_pass(self):
        pass

    def setAdress(self, _street, _city):
        self.__adress = Adress(_street, _city)

    def getAdress(self):
        return self.__adress


p1 = Person(
    _name="Petr",
    _birth=20,
    _email_adress="petr@parker.com")

p1.setAdress("Novoborska", "Praha")
print(p1.get_age())


class Teacher(Person):
    """
    Class that represents a teacher
    """

    def __init__(self, _name, _birth, _email_adress, _salary, _num):
        super.__init__(_name, _birth, _email_adress)
        self.salary = _salary
        self.staff_number = _num
        self.email_adress = _email_adress
        self.salary = _salary
        self.num = _num

    def validate(self):
        pass

    def output_as_label(self):
        pass

    def teach(self):
        print("I am teaching")


t1 = Teacher(
    _name="David",
    _birth=1956,
    _email_adress="dejvino@sad.cz"
)


class Adress():
    """
    Class That represents an adress
    """

    def __init__(self, _street, _city):
        self.street = _street
        self.city = _city

