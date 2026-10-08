print("Amount due: 50")
total = 50
while True:
    payment = int(input("Coin: "))
    # check if payment is valid
    if payment not in [5, 10, 25]:
        print("Invalid coin")
        continue

    total -= payment
    

    if total <= 0:
        print("Change:" + str(total * -1))
        break

    # if payment < 50:
    #     print("Amount due: ", 50 - payment)
    #     if payment == 50:
    #         break
    # else:
    #     change = payment - 50
    #     print("Change owed: ", change)
    #     break

print("All done")