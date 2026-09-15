# classes and inheritance

class Person:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def double_speed(self):
        self.speed *= 2
    def take_damage(self, amount):
        self.health -= amount

class Special(Person): # Special is a child of Person so everything in person is inherited
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.toughness_modifier = 0.9
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)    

Richard = Special(100, 90, 80)
John = Person(50,40,30)

print(Richard.health)
print(John.speed)

Richard.take_damage(40)

John.double_speed()
print(f"John's speed: {John.speed}")
print(f"Richard's health: {Richard.health}")
