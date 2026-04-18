class LoginTizimi:
    def __init__(self):
        self.foydalanuvchilar = {
            "admin": "admin",
            "user": "user"
        }

    def login(self, username, password):
        if username in self.foydalanuvchilar and self.foydalanuvchilar[username] == password:
            return True
        return False

login_tizimi = LoginTizimi()

def main():
    username = input("Istalgan foydalanuvchi nomini kiriting: ")
    password = input("Parolni kiriting: ")
    if login_tizimi.login(username, password):
        print("Tizimga muvaffaqiyatli kirildi!")
    else:
        print("Xatolik: Foydalanuvchi nomi yoki parol noto'g'ri.")

if __name__ == "__main__":
    main()
```

Kodni ishga tushirish uchun quyidagilarni amalga oshiring:

1. Kodni yozing va `python` ni ishga tushiring.
2. `username` va `password` ni kiritib, `Enter` tugmasini bosing.
3. Tizimga muvaffaqiyatli kirish uchun `admin` va `admin` ni kiritib, `Enter` tugmasini bosing.
4. Xatolikni tekshirish uchun `user` va `user` yoki `admin` va `user` yoki boshqa noto'g'ri ma'lumotlarni kiritib, `Enter` tugmasini bosing.
