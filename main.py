from ntpath import join
from operator import index
import random as ra
import time

companies = ['IKEA', 'McDonald\'s', 'Asian Delicious', 'Tyresö Wok', 'Bodens Pizzeria',]
    
class Kock:
    def __init__(self, name: str, trait: str, role: str, speciality: str, course_meal: object) -> None:
        self.name = name
        self.age = ra.randint(10, 110)
        self.trait = trait
        self.role = role
        self.speciality = speciality
        self.course_meal = course_meal
        self.experience = ra.randint(1, self.age - 2)
        self.company = companies[ra.randint(0, len(companies) - 1)]
    
    # Kockens CV
    def __call__(self):
        print(f"""
{self.name}s CV:
Ålder: {self.age}
Företag: {self.company}
Anställning: {self.role}
År av erfarenhet: {self.experience} år
Personlig egenskap: {self.trait}
            """)

    def print_course_meal(self):
        print(f"{self.name}s stjärnrätt: {self.course_meal.name}. Gud vad gott!")
    
    def change_course_meal(self, new_meal: object):
        self.course_meal = new_meal
        print(f"{self.name}s nya stärnrätt är: {self.course_meal.name}. Låter utsökt!")

    def change_speciality(self, new_speciality: str):
        self.speciality = new_speciality
        print(f"{self.name}s nya specialitet är: {self.speciality}. Imponerande!")

class Meal:
    def __init__(self, name: str, rating: int, chef: str) -> None:
        self.name = name
        self.ingredients = []
        self.rating = f"{rating}/5"
        self.chef = chef
    
    def change_rating(self, new_rating: int):
        self.rating = f"{new_rating}/5"
        print(f"Det nya betyget för {self.name} är {self.rating} stjärnor.")

    def add_ingredients(self, new_ingredients):
        if isinstance(new_ingredients, list) == True:
            for i in new_ingredients:
                self.ingredients.append(i)
        
        if isinstance(new_ingredients, str) == True:
            self.ingredients.append(new_ingredients)

    def make(self, portions: int):
        time_to_make = portions * 5
        if portions is None:
            portions = 1
        joined_ingredients = ""
        for i in self.ingredients:
            if self.ingredients.index(i) == len(self.ingredients) - 1:
                joined_ingredients = f"{joined_ingredients[:-2]} och {i}"
            else:
                joined_ingredients = f"{joined_ingredients}{i}, "
        if portions == 1:
            print(f"Nu gör vi {portions} portion av {self.name} med ingredienserna {joined_ingredients}. Det kommer att ta {time_to_make} sekunder.")
        else:
            print(f"Nu gör vi {portions} portioner av {self.name} med ingredienserna {joined_ingredients}. Det kommer att ta {time_to_make} sekunder.")
        for i in range(1, time_to_make+1):
            time.sleep(1)
            time_to_make -= 1
            print(f"Återstående tid: {time_to_make} sekunder")
        time.sleep(1)
        print("Klar! Varsågod att äta!")


def main():
    makaroner_med_köttbullar = Meal('Makaroner med Köttbullar', 3, 'Oliver')
    makaroner_med_köttbullar.add_ingredients(['Makaroner', 'Köttbullar'])
    makaroner_med_köttbullar.add_ingredients('Ketchup')
    makaroner_med_köttbullar.change_rating(5)

    tomatsoppa = Meal('Tomatsoppa', 1, 'Oliver')
    tomatsoppa.add_ingredients(['Tomater', 'Vatten'])
    tomatsoppa.change_rating(2)
    
    
    Oliver = Kock('Oliver', 'Vänlig', 'Köksmästare', 'Koka pasta', makaroner_med_köttbullar)
    Oliver()
    Oliver.print_course_meal()
    Oliver.change_course_meal(tomatsoppa)
    Oliver.change_speciality('Laga Soppa')

    print("")
    makaroner_med_köttbullar.make(3)
    print("")
    tomatsoppa.make(1)

            

if __name__ == "__main__":
    main()
