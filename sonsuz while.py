n = int(input("Notu giriniz:"))
while True: #sonsuz döngü
    if n<=100 and n>=0:
        print("Not başarı ile kaydedildi")
        break
    else:
        print("Lütfen 0-100 aralığında not giriniz")
        n = int(input("Notu giriniz:"))
    
    

