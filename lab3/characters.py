class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
   
    def attack_description(self):
        return f"attacks with {self.name} for {self.damage} damage"

class Character:
    def __init__(self, name, special_power):
        self.name = name
        self.special_power = special_power
        self.weapon = None
    
    def __str__(self):
        return f"I am {self.name}, a {self.__class__.__name__}"

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} {self.weapon.attack_description()}!"
        return f"{self.name} attacks with bare hands for 5 damage!"

    def get_status(self):
        weapon_info = self.weapon.name if self.weapon else "unarmed"
        return f"{self.name} the {self.__class__.__name__} - Weapon: {weapon_info}"

    def summon_power(self):
        raise NotImplementedError("Subclasses must implement summon_power()")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "Berserker Rage")
    def summon_power(self):
        return f"{self.name} unleashes {self.special_power}! Attack power doubled!"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Arcane Blast")
    def summon_power(self):
        return f"{self.name} channels {self.special_power}! Enemies are stunned!"

class Ranger(Character):
    def __init__(self,name):
        super().__init__(name,"Critical hit")
    def summon_power(self):
        return f"{self.name} fires a {self.special_power}! Enemy takes 2x damage!"

Axe = Weapon(name="Axe", damage = "10")
Bow = Weapon(name="Bow", damage = "10")
Staff = Weapon(name = "Staff", damage = "15")

army = [
    Warrior("Thorin"),
    Mage("Gandalf"),
    Ranger("Legolas")
]

print("---My Army---")
for character in army:
    if character.__class__.__name__ =="Warrior":
        character.equip_weapon(Axe)
    elif character.__class__.__name__ =="Mage":
        character.equip_weapon(Staff)
    else:
        character.equip_weapon(Bow)
    print(character.__str__())
    print(character.get_status())
    print(character.summon_power())

print("---Weapon swap demo---")
print(army[2].attack())
character.equip_weapon(Axe)
print(army[2].attack())

## An equipment is modeled as a composition because it is a temporary attribute that can change at any given moment. 
## Hence why we model it as a composition to allow for seamless change, where as if we used inheritance instead we would of had to make a specific class for each class type with the different weapons.