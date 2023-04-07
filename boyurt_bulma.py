def Boyut2(a,b,c,d):
    cevap=((a*d)-(c*d))
    return cevap
def Boyut3(a,b,c,d,e,f,g,ı,i):
    cevap=(a*((e*i)-(ı*f))-d*((b*i)-(ı*c))+g*((b*f)-(e*c)))
    return cevap
def Boyut2R(a,b,d,e):
    cevap=((a*e)-(d*b))
    return cevap
print("lütfen linner boyutuna bakmak istediğiniz R kuvetini giriniz:")
f=int(input("boyut:"))
if f==2:
    a=int(input("1. değerrleri giriniz"))
    b=int(input("2. değerrleri giriniz"))
    c=int(input("1. değerrleri giriniz"))
    d=int(input("2. değerrleri giriniz"))
    cevap=Boyut2(a,b,c,d)
    print(cevap)
    if (cevap==0):
        print("lineer bağımımlı ve 2 boyutlu değişdir")
    else:
        print("lineer bağımsız ve 2 boyutludur")
elif (f==3):
    a=int(input("1. değerrleri giriniz"))
    b=int(input("2. değerrleri giriniz"))
    c=int(input("3. değerrleri giriniz"))
    d=int(input("1. değerrleri giriniz"))
    e=int(input("2. değerrleri giriniz"))
    f=int(input("3. değerrleri giriniz"))
    g=int(input("1. değerrleri giriniz"))
    ı=int(input("2. değerrleri giriniz"))
    i=int(input("3. değerrleri giriniz"))
    cevap=Boyut3(a,b,c,d,e,f,g,ı,i)
    print(cevap)
    if (cevap==0):
        print("lineer bağımımlı ve 3 boyutlu değişdir")
        cevap2=Boyut2R(a,b,d,e)
        print(cevap2)
        if(cevap2==0):
            print("lineer bağımlı ve 2 boyutlu değildir")
            print("1 boyutlu lineer bağımsızdır")
        
        else:
            print("lineer bağımsız ve 2 boyutludur")
    else:
        print("lineer bağımsız ve 3 boyutludur")