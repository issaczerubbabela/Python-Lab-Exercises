import random
#rpg

class Player:
    self.LvlLimit = [x for x in range(10,70,3)]
    self.hpLimit = [x for x in range(5,75,3.5)]
    self.mpLimit = self.hpLimit
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.mp = 5
        self.level = 1
        self.xpNext = 10
        self.alive = 1

    def level_up(self, exp_gained):
        self.xpNext -= exp_gained
        if xpNext < 1 :
            self.level += 1
            self.xpNext = LvlLimit[level-1]
            self.hp = hpLimit[level-1]

    def display_stats(self):
        print("Player Name: {name}\
                Level: {level}\
                HP: {hp}\
                MP: {mp}")

    def receive_damage(self, dmg_received):
        self.hp-=dmg_received
        print("mob did {dmg} damage to {player}".format(dmg_received, self.name))
        if self.hp<1:
            print("{player} has fainted".format(self.name))
            self.alive = 0

    def respawn(self):
        pass

    def death_msg(self):
        pass
    
    def attack(self):
        print("Player has inflicted {damage} on mob".format(self.level*1.1))
        return self.level*1.1

    def run(self):
        pass

class Mob:
    def __init__(self, player_level):
        self.level = player_level
        self.hp = level * 2.5


class Game:
    def __init__(self, player1):
        self.player = player1
        player.name = input("Enter player name: ")
       
    def startGame(self, mob1):
        while player.alive:
            print("A mob appeared")
            self.mob = mob1
            while mob.alive:
                print("What does the player do?\n\t1.Attack\n\t2.Run")
                opt = int(input("(1-2): "))
                if(opt==1):
                    mob.receive_dmg(player.attack())
                    print("{player} did {dmg} damage to mob".format(player.name, player.attack())
                    if mob.hp < 1:
                        print("The mob has fainted")
                          break
    def endGame(self):
        print("Game has Ended")

def main():

if __name__="__main__":
    main()
