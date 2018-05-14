selections = input("Please select the number [1]Selling or [2]Buying : --> ").lower().strip()
for i in selections:
    if i == "1":
        Select_Currency = [["[1] Us Dollar",31.80,31.75],["[2] UK Pounds", 43.95, 42.23],
                           ["[3] Japan Yen", 29.63, 28.48], ["[4] China Yuán", 5.08, 4.74],
                           ["[5] Korea Won", 0.0323, 0.0271], ["[6] Taiwan Doolar", 1.09, 0.95],
                           ["[7] Singapore Dollar", 24.25, 23.44], ["[8] Hong Kong Dollar", 4.11, 3.95],
                           ["[9] Russia rouble", 0.53, 0.38], ["[10] Malaysia Ringgit", 8.20, 7.72]]
        choose = input("Please select the number of Currency : {} {} {} {} {} {} {} {} {} {} -->".format(Select_Currency[0][0],Select_Currency[1][0],Select_Currency[2][0], Select_Currency[3][0], Select_Currency[4][0],Select_Currency[5][0],Select_Currency[6][0], Select_Currency[7][0],Select_Currency[8][0],Select_Currency[9][0]))
        for j in choose :
            if j == "1":
                print("This a exchange rate right now : ",Select_Currency[0][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[0][2]))
            if j == "2":
                print("This a exchange rate right now : ",Select_Currency[1][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[1][2]))
            if j == "3":
                print("This a exchange rate right now : ",Select_Currency[2][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[2][2]))
            if j == "4":
                print("This a exchange rate right now : ",Select_Currency[3][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[3][2]))
            if j == "5":
                print("This a exchange rate right now : ",Select_Currency[4][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[4][2]))
            if j == "6":
                print("This a exchange rate right now : ",Select_Currency[5][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[5][2]))
            if j == "7":
                print("This a exchange rate right now : ",Select_Currency[6][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[6][2]))
            if j == "8":
                print("This a exchange rate right now : ",Select_Currency[7][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[7][2]))
            if j == "9":
                print("This a exchange rate right now : ",Select_Currency[8][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[8][2]))
            if j == "10":
                print("This a exchange rate right now : ",Select_Currency[9][2])
                monney = int(input("Enter you monney amount : "))
                print("You will totally get {:,.2f} Bath".format(monney * Select_Currency[9][2]))
    if i == "2":
        Select_Currency = [["[1] Us Dollar",31.80,31.75],["[2] UK Pounds", 43.95, 42.23],
                           ["[3] Japan Yen", 29.63, 28.48], ["[4] China Yuán", 5.08, 4.74],
                           ["[5] Korea Won", 0.0323, 0.0271], ["[6] Taiwan Doolar", 1.09, 0.95],
                           ["[7] Singapore Dollar", 24.25, 23.44], ["[8] Hong Kong Dollar", 4.11, 3.95],
                           ["[9] Russia rouble", 0.53, 0.38], ["[10] Malaysia Ringgit", 8.20, 7.72]]
        choose = input("Please select the number of Currency : {} {} {} {} {} {} {} {} {} {} -->".format(Select_Currency[0][0],Select_Currency[1][0],Select_Currency[2][0], Select_Currency[3][0], Select_Currency[4][0],Select_Currency[5][0],Select_Currency[6][0], Select_Currency[7][0],Select_Currency[8][0],Select_Currency[9][0]))
        for j in choose :
            if j == "1":
                print("This a exchange rate right now : ",Select_Currency[0][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[0][1]))
            if j == "2":
                print("This a exchange rate right now : ",Select_Currency[1][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[1][1]))
            if j == "3":
                print("This a exchange rate right now : ",Select_Currency[2][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[2][1]))
            if j == "4":
                print("This a exchange rate right now : ",Select_Currency[3][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[3][1]))
            if j == "5":
                print("This a exchange rate right now : ",Select_Currency[4][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[4][1]))
            if j == "6":
                print("This a exchange rate right now : ",Select_Currency[5][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[5][1]))
            if j == "7":
                print("This a exchange rate right now : ",Select_Currency[6][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[6][1]))
            if j == "8":
                print("This a exchange rate right now : ",Select_Currency[7][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[7][1]))
            if j == "9":
                print("This a exchange rate right now : ",Select_Currency[8][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[8][1]))
            if j == "10":
                print("This a exchange rate right now : ",Select_Currency[9][1])
                monney = int(input("Enter you monney amount : "))
                print("You have to pay {:,.2f} Bath".format(monney * Select_Currency[9][1]))