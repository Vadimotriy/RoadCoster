if __name__ == '__main__':
    print("Выберите действие")
    while True:
        action = input("(1) - вписать новую сумму (2) - просмотреть траты: ")

        if action == "1":
            break

        elif action == "2":
            break

        else:
            if action.isdigit(): print("Нет такого варианта!")
            else: print("Впишите номер!")