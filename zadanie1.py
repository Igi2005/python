def zadanie1(text):
    data = ""
    for i in text:
        if i == '.' or i == ',':
            pass
        else:
            data = data + i
    print(data)
    data = data.lower()
    words_txt = data.split(" ")
    words = [] #bez powtorzen
    counter = {}
    for i in words_txt:
        if i not in words:
            words.append(i)
    print(words)
    for i in words:
        counter[i] = words_txt.count(i)
    print(counter)

#zadanie1("Ala ma kota, i roberta. Roberta ma ala i kota. Szymon Puk")

def zadanie3():
    class Prostokat:
        def __init__(self,kolor,dlugosc,szerokosc):
            self.kolor = kolor
            self.dlugosc = dlugosc
            self.szerokosc = szerokosc
        def obliczPole(self):
            return self.dlugosc * self.szerokosc
        def obliczObwod(self):
            return 2*self.dlugosc + 2*self.szerokosc
        def wypisz(self):
            print("Prostokat obwod: ", self.obliczObwod()," pole ",self.obliczPole())
        def zmien_dlugosc(self,value):
            self.dlugosc = value
    p1 = Prostokat("Robertowy",10,5)
    p1.wypisz()

def zadanie2():