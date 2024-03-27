#Palindrome Sayılar

def palindrome_mu(sayi):
    ters=sayi[::-1]
    if(sayi==ters):
        print(sayi,"palindrome sayıdır")
    else:
        print(sayi,"palindrome sayı değildir.")
        
sayi=input("Bir sayı giriniz:")
palindrome_mu(sayi)

