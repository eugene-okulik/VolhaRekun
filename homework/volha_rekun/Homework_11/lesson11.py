# Библиотека
# Первый класс
# Создайте класс book с атрибутами:

# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN

# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.

# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага

class Book:
    material = "бумага"
    naliczie_texta = True
    
    def __init__(self, nazwanie_knigi, awtor, kol_wo_str, ISBN):
        self.nazwanie_knigi = nazwanie_knigi
        self.awtor = awtor
        self.kol_wo_str = kol_wo_str
        self.ISBN = ISBN
        self.is_reserved = False

    def __str__(self):
        if self.is_reserved == False:
            return f"Название: {self.nazwanie_knigi}, Автор: {self.awtor}, Кол-во стр: {self.kol_wo_str}, material: {self.material}"
        else:
            return (
                f"Название: {self.nazwanie_knigi}, "
                f"Автор: {self.awtor}, "
                f"Кол-во стр: {self.kol_wo_str}, "
                f"material: {self.material}, "
                f"зарезервирована"
            )

kniga1 = Book("Zima", "awtor1", 63, 3456)
kniga2 = Book("Vesna", "awtor2", 123, 346)
kniga3 = Book("Leto", "awtor1", 13, 1156)
kniga4 = Book("Osen", "awtor3", 23, 745)
kniga5 = Book("Bez_imeni", "awtor3", 1523, 5116)

kniga3.is_reserved = True

print(kniga1)
print(kniga2)
print(kniga3)
print(kniga4)
print(kniga5)

# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников.
# В нем будут дополнительные атрибуты:

# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)

# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:

# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:

# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

class Uczebniki(Book):
    def __init__(self, nazwanie_knigi, awtor, kol_wo_str, ISBN, szkolnij_predmet, nomer_klassa, zadania):
        super().__init__(nazwanie_knigi, awtor, kol_wo_str, ISBN)
        self.szkolnij_predmet = szkolnij_predmet
        self.nomer_klassa = nomer_klassa
        self.zadania = zadania
    
    def __str__(self):
        if self.is_reserved == False:
            return f"Название: {self.nazwanie_knigi}, Автор: {self.awtor}, Кол-во стр: {self.kol_wo_str}, предмет: {self.szkolnij_predmet}, номер_класса: {self.nomer_klassa}"
        else:
            return (
                f"Название: {self.nazwanie_knigi}, "
                f"Автор: {self.awtor}, "
                f"Кол-во стр: {self.kol_wo_str}, "
                f"предмет: {self.szkolnij_predmet}, "
                f"номер_класса: {self.nomer_klassa}, "
                f"зарезервирована"
            )

kniga6 = Uczebniki("Matem", "awtor6", 53, 3456, "matem", 6, True)
kniga7 = Uczebniki("Russkij", "awtor7", 33, 3456, "russkij_jaz", 7, True)
kniga8 = Uczebniki("Anglijskij", "awtor8", 333, 3456, "anglijskij_jaz",6, True)
kniga7.is_reserved = True

print(kniga6)
print(kniga7)
print(kniga8)
