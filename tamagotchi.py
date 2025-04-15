import time
import os
import random

class SharkTamagotchi:
    def __init__(self):
        self.hunger = 5
        self.happiness = 5
        self.energy = 5
        self.alive = True

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_status(self):
        self.clear()
        print(self.get_ascii_shark())
        print(f"\nHunger:     {self.hunger}/10")
        print(f"Happiness:  {self.happiness}/10")
        print(f"Energy:     {self.energy}/10\n")
    def get_ascii_shark(self):
        if self.hunger >= 9:
            return r"""
                        /""-._
                       .       '""--.._
 :                 \._'/   \           '-.
 \'._______     _.-'       |     .--.     '.
  '.___   '''--/          (    (    \      \
       '''--._             \    '-._/_.-'._/
              '-.        .-'`-.
                 '-._.-'      '--.
            (I'm starving!)
            """
        elif self.happiness <= 2:
            return r"""
                        /""-._
                       .       '""--.._
 :                 \._'/   \           '-.
 \'._______     _.-'       |     .--.     '.
  '.___   '''--/          (    ( .  .\      \
       '''--._             \   (    _/_.-'._/
              '-.        .-'`-.
                 '-._.-'      '--.
            (I'm lonely...)
            """
        elif self.energy <= 2:
            return r"""
                        /""-._
                       .       '""--.._
 :                 \._'/   \           '-.
 \'._______     _.-'       |     .--.     '.
  '.___   '''--/         zZz  ( -__- )     \
       '''--._             \    '-._/_.-'._/
              '-.        .-'`-.
                 '-._.-'      '--.
            (So sleepy...)
            """
        elif not self.alive:
            return r"""
                        /""-._
                       .       '""--.._
 :                 \._'/   \     x     '-.
 \'._______     _.-'       |    x  x     '.
  '.___   '''--/          (     ___       \
       '''--._             \   (___)/_.-'._/
              '-.        .-'`-.
                 '-._.-'      '--.
            (RIP Shark 🦈💀)
            """
        else:
            return r"""
                        /""-._
                       .       '""--.._
 :                 \._'/   \           '-.
 \'._______     _.-'       |     .--.     '.
  '.___   '''--/          (    (    \      \
       '''--._             \    '-._/_.-'._/
              '-.        .-'`-.
                 '-._.-'      '--.
            (I’m a happy shark!)
            """

    def feed(self):
        self.hunger = max(0, self.hunger - 3)
        print("\nYou fed the shark some fish!")
        time.sleep(1)

    def play(self):
        self.happiness = min(10, self.happiness + 2)
        self.energy = max(0, self.energy - 2)
        print("\nYou splashed around and played with the shark!")
        time.sleep(1)

    def rest(self):
        self.energy = min(10, self.energy + 3)
        self.hunger = min(10, self.hunger + 1)
        print("\nThe shark takes a nice nap.")
        time.sleep(1)

    def tick(self):
        self.hunger = min(10, self.hunger + 1)
        self.happiness = max(0, self.happiness - 1)
        self.energy = max(0, self.energy - 1)

        if self.hunger >= 10 or self.happiness <= 0 or self.energy <= 0:
            self.alive = False
            self.clear()
            print("💀 Your shark has passed into the big blue ocean... 💀")

    def run(self):
        while self.alive:
            self.display_status()
            print("What do you want to do?")
            print("1. Feed 🐟")
            print("2. Play 🏀")
            print("3. Rest 😴")
            print("4. Quit 🚪")
            choice = input("> ")

            if choice == "1":
                self.feed()
            elif choice == "2":
                self.play()
            elif choice == "3":
                self.rest()
            elif choice == "4":
                print("Goodbye! Come back soon!")
                break
            else:
                print("Invalid choice.")
                time.sleep(1)

            self.tick()

        if not self.alive:
            self.display_status()
            print("\n💀 Your shark has passed into the big blue ocean... 💀")
            if self.hunger >= 10:
                print("Cause of death: Starvation.")
            elif self.happiness <= 0:
                print("Cause of death: Loneliness.")
            elif self.energy <= 0:
                print("Cause of death: Exhaustion.")
            print("\nPress Enter to exit...")
            input()


# Run it
if __name__ == "__main__":
    game = SharkTamagotchi()
    game.run()
