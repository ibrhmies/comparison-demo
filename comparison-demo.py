#1->girilen iki sayıdan hangisi büyüktür?

x = int(input('x: '))

y = int(input('y: '))

sonuc = (x > y)

print(sonuc)

sonuc = (x < y)

print(sonuc)


#2->girilen sayının çift mi tek mi olduğunu gösterin.

a = int(input('a: '))

sonuc = (a%2==0)

print(f"girilen a değeri çifttir: {sonuc} ")


#3-> girilen sayının pozitif mi negatif mi olduğunu gösterin.

a = int(input('a: '))

sonuc = (a > 0)

print(f'a pozitiftir: {sonuc}')


#4->kullanıcıdan vize(%40)  ve final(%60) notunu alıp ortalamasını al 55 i geçiyorsa geçti geçmiyorsa kaldı.

vize = int(input('vize: '))
final = int(input('final: '))

sonuc = (vize*40/100+final*60/100 >= 55)

print(f"öğrenci geçti: {sonuc} ")

#5->parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
email = "ibrhmiss@gmail.com"

password = 12345

x = str(input("E-mail giriniz: "))

y = int(input("Password giriniz: "))

sonuc1 = (x == email)

sonuc2 = (y == password)

print(f"emaili doğru girdiniz: {sonuc1} ,password doğru girdiniz: {sonuc2}")
