# Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)

try:
    with open('emails.txt', 'r') as f:
        for line in f:
            if line.__contains__('gmail.com'):
                hesh,mail=line.split()

                with open('emailresult.txt','a') as f:
                    f.write(mail+'\n')


except Exception:
    print('Name error')

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
import pickle
class Book:
    shoplist=[]
    try:
        with open('file.pkl', 'rb') as f:

            shoplist=pickle.load(f)

    except Exception:
        print('File error')






    def update(cls):
        try:
            with open('file.pkl', 'wb') as f:
                pickle.dump(cls.shoplist, f)

        except Exception:
            print('error')



    @classmethod

    def additem(cls,id,name,price):
        cls.shoplist.append([id,name,price])
        cls.update(cls)






    @classmethod
    def showshoplist(cls):
        print(cls.shoplist)

    @classmethod
    def delshoplist(cls,id):
        for i in cls.shoplist:
            if i[0] == id:
                cls.shoplist.remove(i)
                cls.update(cls)
    @classmethod
    def searchshoplist(cls,name=None):
        for i in cls.shoplist:
            if i[1] == name or i[0] == name or i[2] == name:
                print(i)


    @classmethod
    def findmaxpriceitem(cls):
        max_arr=max(cls.shoplist, key=lambda x: x[2])
        print(max_arr)




# Book.additem(1,'bike',1)
# Book.additem(2,'car',10909090)
# Book.additem(3,'bicycle',200000000)

# Book.searchshoplist(1)





while True:
    print('1) вивід всіх покупок')
    print('2) додавати покупку в книгу')
    print('3) шукати по будь якому полю покупку')
    print('4)  показати найдорожчу покупку')
    print('5) видаляти покупку по id')
    print('0) вихід')

    choice=input('enter your choice:')

    if choice=='1':
        Book.showshoplist()
    elif choice == '2':
        Book.additem(int(input('enter your id')),input('enter name'),int(input('enter your price')))


    elif choice=='3':
        Book.searchshoplist(input('enter name or id or price:'))

    elif choice == '4':
        Book.findmaxpriceitem()

    elif choice=='5':
        Book.delshoplist(int(input('enter id to delete:')))

    elif choice=='0':
        break

