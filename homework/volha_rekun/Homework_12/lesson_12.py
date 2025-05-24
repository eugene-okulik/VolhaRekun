# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.


class Cvetok:
    def __init__(self, svezest, cvet, dlina, cena, vrema_zhizni):
        self.svezest = svezest
        self.cvet = cvet
        self.dlina = dlina
        self.cena = cena
        self.vrema_zhizni = vrema_zhizni

    def __repr__(self):
        return f"{type(self).__name__}(svezest={self.svezest}, cvet={self.cvet}, dlina={self.dlina}, cena={self.cena})"


class Romashka(Cvetok):
    def __init__(self, svezest, cvet, dlina, cena, vrema_zhizni):
        super().__init__(svezest, cvet, dlina, cena, vrema_zhizni)


class Vasilok(Cvetok):
    def __init__(self, svezest, cvet, dlina, cena, vrema_zhizni):
        super().__init__(svezest, cvet, dlina, cena, vrema_zhizni)


class Buket:
    def __init__(self, cvety):
        self.cvety = cvety

    @property
    def cena(self):
        i = 0
        for a in self.cvety:
            i += a.cena
        return i

    @property
    def vremya_uviadania(self):
        if len(self.cvety) == 0:
            return 0
        else:
            i = 0
            for a in self.cvety:
                i += a.vrema_zhizni
            return i / len(self.cvety)

# Позволить сортировку цветов в букете на основе различных параметров(свежесть/цвет/длина стебля/стоимость)(методы)
# 0 - сегодня, 1 - вчера, 2 -давно ( примечание автора решения домашки:)

    def sort_by_svezest(self):
        self.cvety.sort(key=lambda i: i.svezest)

    def sort_by_cvet_cvetka(self):
        self.cvety.sort(key=lambda i: i.cvet)

    def sort_by_dlina_cvetka(self):
        self.cvety.sort(key=lambda i: i.dlina)

    def sort_by_cena_cvetka(self):
        self.cvety.sort(key=lambda i: i.cena)

# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод)
    def svezhije(self):
        rezultat = []
        for i in self.cvety:
            if i.svezest == 0:
                rezultat.append(i)
        return rezultat


rastenie1 = Romashka(svezest=1, cvet="belyj", dlina=34, cena=155, vrema_zhizni=1)
rastenie2 = Vasilok(svezest=0, cvet="krasnyj", dlina=14, cena=14, vrema_zhizni=100)
cvetok3 = Romashka(svezest=2, cvet="seryj", dlina=7, cena=71, vrema_zhizni=15)
buket1 = Buket([rastenie1, rastenie2, cvetok3])
# print(buket1.cvety)
print(buket1.cena)
print(buket1.vremya_uviadania)

buket1.sort_by_svezest()
print(buket1.cvety)

buket1.sort_by_cvet_cvetka()
print(buket1.cvety)

buket1.sort_by_dlina_cvetka()
print(buket1.cvety)

buket1.sort_by_cena_cvetka()
print(buket1.cvety)

print(buket1.svezhije())
