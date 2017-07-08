from random import randint

class Die():
    """A class representing the rolling of die/dice."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    def four_die_drop_low(self):
        """Return the sum of four dice, dropping the lowest value."""
        count = 0
        rolled_4 = []
        while count < 4:
            rolled_4.append(self.roll())
            count += 1
        rolled_4.sort(reverse=True)
        del(rolled_4[-1])
        return(sum(rolled_4))

    def three_die_straight(self):
        """Return the sum of three dice, no modifications"""
        count = 0
        rolled_3 = []
        while count < 3:
            rolled_3.append(self.roll())
            count += 1
        return(sum(rolled_3))

    def straight_six_of_twelve(self):
        """
        Return the top 6 rolls out of 12 random rolls.
        The individual rolls will be the sum of 3d6 straight.
        """
        count = 0
        rolled_12 = []
        while count < 12:
            rolled_12.append(str(self.three_die_straight()))
            count +=1
        rolled_12.sort(key=float)
        del(rolled_12[:6])
        return(rolled_12)

    def best_six_of_twelve(self):
        """
        Return the top 6 rolls out of 12 random rolls.
        The individual rolls will be the sum of 4d6 dropping lowest.
        """
        count = 0
        rolled_12 = []
        while count < 12:
            rolled_12.append(str(self.four_die_drop_low()))
            count += 1
        rolled_12.sort(key=float)
        del(rolled_12[:6])
        return(rolled_12)

    def hp_generation(self, character_class, character_level, const_stat):
        """Return the HP of a character based on class and level."""
        count = 0
        rolled_hp = []

        if const_stat == '3':
            hp_adjustment = -2
        elif const_stat == '4' or const_stat == '5' or const_stat == '6':
            hp_adjustment = -1
        elif const_stat == '15':
            hp_adjustment = 1
        elif const_stat == '16':
            hp_adjustment = 2
        elif const_stat == '17' and character_class == 'fighter' or \
            character_class == 'paladin' or character_class == 'ranger':
            hp_adjustment = 3
        elif const_stat == '18' and character_class == 'fighter' or \
             character_class == 'paladin' or character_class == 'ranger':
            hp_adjustment = 4
        elif const_stat == '17' and character_class != 'fighter' or \
             character_class == 'paladin' or character_class == 'ranger':
            hp_adjustment = 2
        elif const_stat == '18' and character_class != 'fighter' or \
             character_class == 'paladin' or character_class == 'ranger':
            hp_adjustment = 2
        else:
            hp_adjustment = 0

        if character_class == 'cleric':
            max_hit_die = 9
            min_hit_die = character_level
            extra_hp = ((character_level - max_hit_die) * 2)
        elif character_class == 'druid':
            max_hit_die = 14
            min_hit_die = character_level
            extra_hp = 0
        elif character_class == 'fighter' or character_class == 'paladin':
            max_hit_die = 9
            min_hit_die = character_level
            extra_hp = ((character_level - max_hit_die) * 3)
        elif character_class == 'ranger':
            max_hit_die = 10
            if character_level <= max_hit_die:
                min_hit_die = character_level + 1
            else:
                min_hit_die = max_hit_die + 1
            extra_hp = ((character_level - max_hit_die) * 2)
        elif character_class == 'magic user':
            max_hit_die = 11
            min_hit_die = character_level
            extra_hp = character_level - max_hit_die
        elif character_class == 'illusionist':
            max_hit_die = 10
            min_hit_die = character_level
            extra_hp = character_level - max_hit_die
        elif character_class == 'thief':
            max_hit_die = 10
            min_hit_die = character_level
            extra_hp = ((character_level - max_hit_die) * 2)
        elif character_class == 'assassin':
            max_hit_die = 15
            min_hit_die = character_level
            extra_hp = 0
        elif character_class == 'monk':
            max_hit_die = 17
            if character_level <= max_hit_die:
                min_hit_die = character_level + 1
            else:
                min_hit_die = max_hit_die + 1
            extra_hp = 0

        if character_level <= max_hit_die:
            while count < min_hit_die:
                hp_rolled = self.roll() + hp_adjustment
                rolled_hp.append(hp_rolled)
                count += 1
        elif character_level > max_hit_die:
            while count < max_hit_die:
                hp_rolled = self.roll() + hp_adjustment
                rolled_hp.append(hp_rolled)
                count += 1
            rolled_hp.append(extra_hp)

        return(sum(rolled_hp))