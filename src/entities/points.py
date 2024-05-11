class PointsCounter:
    """
    Pisteidenlaskuriluokka, joka sisältää pistelaskentafunktiot pelin 
    pisteiden laskemiseen.
    """
    @staticmethod
    def calculate_ones(dices):
        """
        Laskee ykkästen summan

        Args:
            dices: Lista nopista.
        
        Returns:
            Ykkösten summa.
        """
        ones_count = 0
        for dice in dices:
            if dice.value == 1:
                ones_count += 1
        return ones_count

    @staticmethod
    def calculate_twos(dices):
        """
        Laskee kakkosten summan.

        Args:
            dices: Lista nopista.
        
        Returns:
            kakkosten summa.
        """
        twos_count = 0
        for dice in dices:
            if dice.value == 2:
                twos_count += 2
        return twos_count

    @staticmethod
    def calculate_threes(dices):
        """
        Laskee kolmosten summan.
        """
        threes_count = 0
        for dice in dices:
            if dice.value == 3:
                threes_count += 3
        return threes_count

    @staticmethod
    def calculate_fours(dices):
        """
        Laskee nelosten summan.
        """
        fours_count = 0
        for dice in dices:
            if dice.value == 4:
                fours_count += 4
        return fours_count

    @staticmethod
    def calculate_fives(dices):
        """
        Laskee vitosten summan.
        """
        fives_count = 0
        for dice in dices:
            if dice.value == 5:
                fives_count += 5
        return fives_count

    @staticmethod
    def calculate_sixes(dices):
        """
        Laskee kutosten summan.
        """
        sixes_count = 0
        for dice in dices:
            if dice.value == 6:
                sixes_count += 6
        return sixes_count

    @staticmethod
    def calculate_pair(dices):
        """
        Laskee parin summan.
        """
        for value in range(6, 0, -1):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 2:
                return value * 2
        return 0

    @staticmethod
    def calculate_two_pairs(dices):
        """
        Laskee kahden parin summan.
        """
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
        """
        Laskee kolmoen saman summan.
        """
        for value in range(1, 7):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 3:
                return sum(dice.value for dice in dices if dice.value == value)
        return 0

    @staticmethod
    def calculate_four_of_a_kind(dices):
        """
        Laskee neljän saman summan.
        """
        for value in range(1, 7):
            count = sum(1 for dice in dices if dice.value == value)
            if count >= 4:
                return value * 4
        return 0


    @staticmethod
    def calculate_small_straight(dices):
        """
        Laskee pieni suoran summan.
        """
        values = sorted(dice.value for dice in dices)
        if values == [1, 2, 3, 4, 5]:
            return 15
        return 0

    @staticmethod
    def calculate_large_straight(dices):
        """
        Laskee suuri suoran summan.
        """
        values = sorted(dice.value for dice in dices)
        if values == [2, 3, 4, 5, 6]:
            return 20
        return 0

    @staticmethod
    def calculate_full_house(dices):
        """
        Laskee täyskäden summan.
        """
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
        """
        Laskee sattuman summan.
        """
        return sum(dice.value for dice in dices)

    @staticmethod
    def calculate_yatzy(dices):
        """
        Tutkii onko viisi samaa.

        Returns:
            palauttaa 50 jos viisi samaa muuten 0.
        """
        for value in range(1, 7):
            if sum(1 for dice in dices if dice.value == value) == 5:
                return 50
        return 0

    @staticmethod
    def calculate_subtotal(scoreboard):
        """
        Laskee pistetaulukosta 1-6 ja bonuksen summan.
        """
        subtotal = 0

        for i, (_, val) in enumerate(scoreboard.items()):
            if i < 6 and val != '':
                subtotal += int(val)

        return subtotal


    @staticmethod
    def calculate_bonus(scoreboard):
        """
        Laskee pistetaulukosta 1-6 summan, jos summana on suurempi kuin 63 niin saa 50.

        Returns:
            palauttaa 50, jos pistetaulukosta 1-6 summa >= 63 muuten 0 
        """
        subtotal = PointsCounter.calculate_subtotal(scoreboard)

        if subtotal != 0 and subtotal >= 63:
            return 50
        else:
            return 0


    @staticmethod
    def calculate_total(scoreboard):
        """
        Laskee kaikkien kohtien summan.
        """
        total = 0

        for i, (_, val) in enumerate(scoreboard.items()):
            if 7 < i < 17 and val != '':
                total += int(val)

        return total+ PointsCounter.calculate_subtotal(scoreboard)

    