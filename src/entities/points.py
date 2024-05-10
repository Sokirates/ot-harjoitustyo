class PointsCounter:
    @staticmethod
    def calculate_ones(dices):
        ones_count = 0
        for dice in dices:
            if dice.value == 1:
                ones_count += 1
        return ones_count

    @staticmethod
    def calculate_twos(dices):
        twos_count = 0
        for dice in dices:
            if dice.value == 2:
                twos_count += 2
        return twos_count

    @staticmethod
    def calculate_threes(dices):
        threes_count = 0
        for dice in dices:
            if dice.value == 3:
                threes_count += 3
        return threes_count

    @staticmethod
    def calculate_fours(dices):
        fours_count = 0
        for dice in dices:
            if dice.value == 4:
                fours_count += 4
        return fours_count

    @staticmethod
    def calculate_fives(dices):
        fives_count = 0
        for dice in dices:
            if dice.value == 5:
                fives_count += 5
        return fives_count

    @staticmethod
    def calculate_sixes(dices):
        sixes_count = 0
        for dice in dices:
            if dice.value == 6:
                sixes_count += 6
        return sixes_count

    @staticmethod
    def calculate_pair(dices):
        for value in range(6, 0, -1):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 2:
                return value * 2
        return 0

    @staticmethod
    def calculate_two_pairs(dices):
        pairs = []
        for value in range(6, 0, -1):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 2:
                pairs.append(value)
            if len(pairs) == 2:
                return sum(pairs) * 2
        return 0

    @staticmethod
    def calculate_three_of_a_kind(dices):
        for value in range(1, 7):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 3:
                return sum(dice.value for dice in dices if dice.value == value)
        return 0

    @staticmethod
    def calculate_four_of_a_kind(dices):
        for value in range(1, 7):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 4:
                return value * 4
        return 0


    @staticmethod
    def calculate_small_straight(dices):
        values = sorted(dice.value for dice in dices)
        if values == [1, 2, 3, 4, 5]:
            return 15
        return 0

    @staticmethod
    def calculate_large_straight(dices):
        values = sorted(dice.value for dice in dices)
        if values == [2, 3, 4, 5, 6]:
            return 20
        return 0

    @staticmethod
    def calculate_full_house(dices):
        for value in range(1, 7):
            count1 = sum(1 for dice in dices if dice.value == value)
            if count1 == 3:
                for value2 in range(1, 7):
                    count2 = sum(1 for dice in dices if dice.value == value2)
                    if count2 == 2 and value2 != value:
                        return sum(dice.value for dice in dices)
        return 0

    @staticmethod
    def calculate_chance(dices):
        return sum(dice.value for dice in dices)

    @staticmethod
    def calculate_yatzy(dices):
        for value in range(1, 7):
            if sum(1 for dice in dices if dice.value == value) == 5:
                return 50
        return 0

    @staticmethod
    def calculate_subtotal(scoreboard):
        return (int(scoreboard['ones'])
                +int(scoreboard["twos"])
                +int(scoreboard["threes"])
                +int(scoreboard["fours"])
                +int(scoreboard["fives"])
                +int(scoreboard["sixes"])
                +int(scoreboard['bonus']))

    @staticmethod
    def calculate_bonus(scoreboard):
        if (int(scoreboard['ones'])
                +int(scoreboard["twos"])
                +int(scoreboard["threes"])
                +int(scoreboard["fours"])
                +int(scoreboard["fives"])
                +int(scoreboard["sixes"])) >= 63:
            return 50
        return 0
