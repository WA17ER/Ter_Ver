from math import factorial


class Veroyatnost:
    def __init__(self, k=None, n=None):
        self.k = k
        self.n = n
        """Класс получает на вход 2 позиционных аргумента для работы с методами теории вероятности по умолчанию оба равны NONE
               k целое число показывающее число благоприятных исходов
               n число общих возможных исходов   
        """

    def chance(self):
        """
        :return:Метод возврашаетсоотношение блаоприятных исходов к общему числу исходов для нахождения классической вероятности
        :rtype: float
        >>> Veroyatnost(1,6).chance()
        0.16666666666666666
        """
        return self.k / self.n

    def combinations(self):
        """
        :return:Метод возврашает число сочетаний из  n  элементов по  k  элементов в каждом (в сочетаниях порядок не важен)
        :rtype: int
        >>> Veroyatnost(2,6).combinations()
        15
        """
        return int(factorial(self.n) / (factorial(self.k) * factorial(self.n - self.k)))


    def arrangements(self):
        """
        :return:Возврашаетчисло размещений из  n  элементов по  k  элементов в каждом. При размещениях порядок важен
        :rtype: int
        >>>Veroyatnost(2,6).arrangements()
        30
        """
        return int(factorial(self.n) / factorial(self.n - self.k))

    def permutations(self):
        """
        :return: Число перестановок из  n  элементов — при перестановках важен порядок, но отличие от размещений в том, что применяются все имеющиеся  n  элементов:
        :rtype: int
        >>> Veroyatnost(None,6).permutations()
        720
        """
        return int(factorial(self.n))

    def un_dependen(self, other):
        """
        :param other: Вероятность возникновения события B(при независимых событиях) или же B при уже произошедшем А(при зависимых)
        :type other:__main__.Veroyatnost
        :return:Возврашает вероятность одновременного появления двух независимых(зависимых) событий
        :rtype:float
        >>> Veroyatnost(1,2).un_dependen(Veroyatnost(1,3))
        0.16666666666666666
        """

        return self.chance() * other.chance()

    def full_chance(self, *args):
        """

        :param args: кортеж из вероятностей событий
        :type args: tuple
        :return: Возврашает полную вероятность события А при списке событий B
        :rtype:float
        >>> Veroyatnost().full_chance(5/8, 0, 1)
        0.5416666666666666
        """
        ter_ver = 1/len(args)
        return sum([ter_ver * args for args in args])


    def bayes(self, *args):
        """
        Метод для формулы Байсона
        :param args: вероятность некоторых событий
        :type args: tuple
        :return:Чтобы определить вероятность события  B  при условии, что событие  A  уже произошло
        :rtype:float
        >>> Veroyatnost().bayes(0.7, 0.2, 0.4)
        0.5384615384615384
        """
        return (1/len(args)* args[0])/self.full_chance(*args)



