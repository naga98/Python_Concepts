class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage! ({self.health} HP left)")

    def is_alive(self):
        return self.health > 0

    def status(self):
        print(f"{self.name} | Level: {self.level} | HP: {self.health}")


class Warrior(GameCharacter):
    def __init__(self, name, health, level, sword_power):
        super().__init__(name, health, level)
        self.sword_power = sword_power

    def sword_attack(self, target):
        print(f"{self.name} swings a sword at {target.name}!")
        target.take_damage(self.sword_power)


class Archer(GameCharacter):
    def __init__(self, name, health, level, arrow_power):
        super().__init__(name, health, level)
        self.arrow_power = arrow_power

    def arrow_attack(self, target):
        print(f"{self.name} shoots an arrow at {target.name}!")
        target.take_damage(self.arrow_power)


class Wizard(GameCharacter):
    def __init__(self, name, health, level, magic_power):
        super().__init__(name, health, level)
        self.magic_power = magic_power

    def magic_attack(self, target):
        print(f"{self.name} casts a spell on {target.name}!")
        target.take_damage(self.magic_power)


def main():
    warrior = Warrior("Conan", health=120, level=5, sword_power=25)
    archer = Archer("Legolas", health=90, level=4, arrow_power=20)
    wizard = Wizard("Gandalf", health=80, level=6, magic_power=35)

    for character in (warrior, archer, wizard):
        character.status()

    print("\n--- Battle Begins ---")
    warrior.sword_attack(wizard)
    archer.arrow_attack(warrior)
    wizard.magic_attack(archer)

    print("\n--- Final Status ---")
    for character in (warrior, archer, wizard):
        character.status()
        print(f"{character.name} alive: {character.is_alive()}")


if __name__ == "__main__":
    main()
