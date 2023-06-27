# ismlar = ["Lochin", "Temurbek", "Nosirjon"]
# print("Salom ", ismlar[0], ". Najot ta'limga ketamizmi do's\n",ismlar[2], " grant yutib olibdi Najot ta'limga")

# sonlar = [100, -200, 50.65, 125]
# sonlar[1] = sonlar[1] + sonlar[0]
# sonlar[2] = sonlar[2] + 0.35
# sonlar.append(13424524)
# sonlar.insert(0, 50_000_000)
# print(sonlar)


# t_shaxslar = ["Amir Temur", "Beruniy", "Al Xorazmiy"]
# z_shaxslar = ["Ilon Musk", "Anvar Narzullayev", "Saud Abdulvahed"]

# print("Men tarixiy shaxslardan", t_shaxslar.pop(0), "ni yaxshiroq taniyman.")
# print("Men", z_shaxslar.pop(1), "ga shogit tushushni hohlar edim.")


# friends = []
# friends.append("Lochinbel")
# friends.append("Sunnat")
# friends.append("Nosirjon")
# friends.append("Temurbek")
# friends.append("Aloviddin")

# friends.remove("Temurbek")
# friends.remove("Sunnat")

# friends.insert(0, "Murodjon")
# friends.insert(2, "Otabek")
# friends.insert(4, "Erali aka")

# mexmonlar = []
# mexmonlar.append(friends.pop(0))
# mexmonlar.append(friends.pop(1))
# mexmonlar.append(friends.pop(3))
# print("Do'stlar:", friends)
# print("Mexmonlar:", mexmonlar)


############  ro'yxatlar bilan ishlash 

# ismlar = ["Muhriddin", "Azamjon", "Durdona", "Fayoza"]
# ismlar.reverse()
# print(len(ismlar))


# sonlar = list(range(10, 17))
# juft_sonlar = list(range(10, 30, 3)) # 10 dan 30 gacha

# sonlar = list(range(15))  # 0 dan 15 gacha sonlar (0, 1, 2, ...... , 13, 14)
# print(sonlar)

# numbers = list(range(11))
# minimum = min(numbers)
# maximum = max(numbers)
# summa = sum(numbers)

# print("Eng kichik son: ", minimum)
# print("Eng katta son: ", maximum)
# print("Sonlar yig'indisi: ", summa)




# books = ["Diqqat", "Zero to one", "1984", "Oq kema", "Sohibqiron", "Atom odatlar"]
# read_books = books[1:5]  #1 dan boshlab 5-indeksgacha kesish

# another_books = books[:]

# another_books.append("O'tgan kunlar")
# another_books.append("Raqamli qala")

# print(books)
# print(another_books)

# my_family = ("Alisher", "Nigora", "Muhriddin", "Farangiz", "Fayoza")
# print("Mening oila azolarim: ", my_family)
# print(my_family[2])



# names = ("Abdumajid", "Payzilla", "Mag'firatxon", "Quvondiq", "Anzirat", "Gulsapsar")
# print(names)
# names = list(names)
# names.remove("Quvondiq")
# names.remove("Payzilla")
# names.append("Toshtemrixon")
# names.append("Zarbibi")
# names = tuple(names)
# print(names)



# countries = ["Qozog'iston", "Tojikiston", "Qirg'ziston", "Turkmaniston", "Afg'oniston"]
#print("O'zbekitonning qo'shni davlatlari: ", countries)
# print("Ro'yxatda", len(countries), "ta davlat bor")

#print(sorted(countries))
# countries.reverse()
# print("Teskari ro'yxat:", countries)

# print(countries)
# # countries.sort()
# countries.sort(reverse=True)
# print(countries)

numbers = list(range(120, 1200, 2))
# print("120 dan 1200 gacha juft sonlar:", numbers)
# summa = sum(numbers)

# eng_katta = max(numbers)
# eng_kichik = min(numbers)
# print("Max element: ", eng_katta, "\nMin element: ", eng_kichik)
# print(eng_katta, "-", eng_kichik, "=", eng_katta-eng_kichik)

el_soni = len(numbers)
# print("Ro'yxatdagi elementlar soni: ", el_soni)

# boshidan = numbers[0:20]
# print("Boshidan: ", boshidan)

# urtadan = numbers[260:280]
# print("O'rtasidan: ", urtadan)

# urtadan2 = numbers[len(numbers):len(numbers)]
# print("O'rtasidan2: ", urtadan2)

# oxiridan = numbers[520:540]
# print("Oxiridan1: ", oxiridan)

# oxiridan2 = numbers[len(numbers)-20:len(numbers)]
# print("Oxiridan2: ", oxiridan2)

# meals = ["Osh", "Manti", "Kasha", "Lavash", "Tuxum", "Hot Dog"]
# breakfast = meals[:]
# breakfast.remove("Osh")
# breakfast.remove("Manti")
# breakfast.remove("Lavash")
# breakfast.remove("Hot Dog")
# breakfast.append("Qaymoq")
# breakfast.append("Paxlava")
# print(breakfast)
# breakfast = tuple(breakfast)
# breakfast[2] = "Birnimalar"
# print(breakfast)


juralar = ["Murodjon", "Nosirjon", "Lochinbek", "Sunnat", "temurbek"]
for juram in juralar:
    print("Qalaysan", juram)