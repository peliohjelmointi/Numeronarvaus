# Numeronarvaus

# Peli kysyy käyttäjää arvaamaan numeroa väliltä 1-10, kunnes käyttäjä arvaa numeron oikein.Sitten ohjelma suljetaan.
# Mikäli numero oli liian iso tai pieni, kerrotaan käyttäjälle "liian iso" tai "liian pieni" ja kysytään uudelleen.
# Mieti miten saat ohjelman toimimaan alla olevilla metodeilla ja ohjeilla.

class NumberGuessingGame:

    def __init__(self):
        self.count = 0
       
    def generate_random_number(self):
        pass 
      
    def ask_number(self):
        while True:
            try:
                number = int(input("Arvaa numero väliltä 1-10"))
            except:
                continue
            if number < 1:
                print("Numero oli liian pieni.")
                continue
            elif number > 10:
                print("Numero on liian pieni")
                continue
            else:
                break
        return number
              
    def add_guess_count(self):
        pass  
           
    def main_game_loop(self):
        random_number = self.add_guess_count()
        while True:
            number_user = self.ask_number()
            if number_user == random_number:
                print(f"Oikein. Arvasit {self.count} kertaa.")
                break


game = NumberGuessingGame()

game.main_game_loop()
