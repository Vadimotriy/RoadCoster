from database import Session, Prices

def get_total_price(session):
    sums = [i.price for i in session.query(Prices).all()]
    return sum(sums)

if __name__ == '__main__':
    session = Session()
    print("Выберите действие.", end=" ")
    while True:
        action = input("(1) - вписать новую сумму (2) - просмотреть траты: ")

        if action == "1":
            road_price = input("Введите сумму: ")
            while True:
                if not road_price.isdigit():
                    road_price = input("Это не сумма! Попробуйте еще раз: ")
                else:
                    data = Prices(price=road_price)
                    session.add(data)
                    session.commit()
                    print(f"\nИтоговая сумма: {get_total_price(session)} руб.")
                    break
            break

        elif action == "2":
            print("\n----------------------------------")

            prices = session.query(Prices).all()
            for i in prices:
                print(f"{i.time} --- {i.price} руб.")
            print("----------------------------------")
            print(f"\nИтоговая сумма: {get_total_price(session)} руб.")
            break

        else:
            if action.isdigit(): print("Нет такого варианта!", end=" ")
            else: print("Впишите номер!", end=" ")
