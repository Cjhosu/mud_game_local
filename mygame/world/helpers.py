import random

#This class rolls any number of 20 sided dice
#It takes an optional pass condition
#If any of the results pass it returns true

class DiceRoll:
    def __init__(self, dice, **kwargs):
        self.dice = dice
        self.pass_cond = kwargs.get("pass_cond") or None
    def roll(self):
        results = []
        pass_cond = self.pass_cond
        for die in range(0,self.dice):
            die_result = random.randint(1,20)
            results.append(die_result)
            if pass_cond and die_result in pass_cond:
                passed = True
                return(results,passed)
            elif pass_cond and die_result not in pass_cond:
                passed = False
            else:
                passed = None
        return(results, passed)


#Using some stat we can add more dice increasing the odds of a pass
def get_num_dice(stat):
    num_dice = 1
    base = 105
    while base < stat and num_dice < 20:
        base += 5
        num_dice +=1
    return num_dice


def equipped_check(caller, item):
    slots = caller.db.slots
    caller = str(caller)
    equipped = False

    if slots:
        if slots[item]:
            equipped = True
            message = caller + "has a "+ item + " equipped"
        else:
            message = caller + "has no "+ item + " equipped"
    else :
        message = caller + " has no equipment slots"

    return equipped, message

def display_prompt(caller):

    if not caller.db.health:
        health = 255
    else:
        health = caller.db.health

    if not caller.db.max_health:
        max_health = 255
    else:
        max_health = caller.db.max_health

    if not caller.db.level:
        level = 1
    else:
        level = caller.db.level

    if not caller.db.xp:
        xp = 0
    else:
        xp = caller.db.xp

    if not caller.db.next_level_xp:
        next_level_xp = 0
    else:
        next_level_xp = caller.db.next_level_xp

    if not caller.db.gold:
        gold = 0
    else:
        gold = caller.db.gold

    prompt = "HP:%i/%i  Level:%i  XP:%i/%i  Gold:%i" % (health, max_health, level, xp, next_level_xp, gold)
    caller.msg(prompt=prompt)

def drop_gold_pieces():
    num_list = [1,2,3]
    number = random.choices(num_list, weights=(4, 2, 1), k=1)
    return number[0]
