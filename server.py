import sqlite3
import socket
"""targil 7"""
conn = sqlite3.connect('databaseInfo.db')
cursor = conn.cursor()

IP = '0.0.0.0'
PORT = 33010

class server:

    def __init__(self):
        self.name = ""
        self.moneyInTheBank = 0
        self.pinCode = ""
        self.accNumber = 0
        self.conection()
        self.bankFunctions()

    def conection(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((IP, PORT))
        self.serverSocket.listen(1)
        start = "Welcome to the bank! \n" \
                  "please choose your requested action\n" \
                  "1- Create account\n" \
                  "2- Log in to your account\n" \
                  "7- Exit\n"
        self.clientSocket, self.address = self.serverSocket.accept()
        self.clientSocket.send(bytes((start).encode('utf-8')))
        data = self.clientSocket.recv(1024)
        data = data.decode(('utf-8'))
        while data != '7':
            if data == '1':


                self.accNumber = self.clientSocket.recv(1024)
                self.accNumber = self.accNumber.decode('utf-8')
                self.accNumber = int(self.accNumber)


                self.name = self.clientSocket.recv(1024)
                self.name = self.name.decode('utf-8')

                self.pinCode = self.clientSocket.recv(1024)
                self.pinCode = self.pinCode.decode('utf-8')

                self.moneyInTheBank = self.clientSocket.recv(1024)
                self.moneyInTheBank = self.moneyInTheBank.decode('utf-8')
                self.moneyInTheBank = int(self.moneyInTheBank)
                self.createAccount()
                break
            elif data == '2':
                self.accNumber = self.clientSocket.recv(1024)
                self.accNumber = self.accNumber.decode('utf-8')
                self.accNumber = int(self.accNumber)
                self.sign_in()
                break
            data = self.clientSocket.recv(1024)
            data = data.decode(('utf-8'))

        if data == '7':
            self.clientSocket.close()
            self.serverSocket.close()
    def bankFunctions(self):
        request = "Welcome to the bank! \n" \
                  "Choose your requested action\n" \
                  "4- Deposit money\n" \
                  "5- Withdraw money\n" \
                  "6- Check your balance\n" \
                  "7- Exit\n"
        self.clientSocket.send(bytes((request).encode('utf-8')))
        data = self.clientSocket.recv(1024)
        data=data.decode(('utf-8'))
        data = data.lower()
        while data != '7':
            if data == '4':
                pin = self.clientSocket.recv(1024)
                pin = pin.decode('utf-8')
                self.deposit(pin)

            elif data == '5':
                pin = self.clientSocket.recv(1024)
                pin = pin.decode('utf-8')
                self.withdraw(pin)

            elif data == '6':
                msg = self.clientSocket.recv(1024)
                msg = msg.decode('utf-8')
                self.bankBalance()
            data = self.clientSocket.recv(1024)
            data = data.decode(('utf-8'))
        self.clientSocket.close()
        self.serverSocket.close()

    def createAccount(self):
        cursor.execute("SELECT * FROM account WHERE accountNum = ?", (self.accNumber,))
        data2 = cursor.fetchall()
        if (len(data2) == 0):
            cursor.execute("INSERT INTO account (accountNum,name,pinCode,money) VALUES(?,?,?,?)"
                           , (self.accNumber, self.name, self.pinCode, self.moneyInTheBank))
            self.clientSocket.send(bytes(("\n\n\nAccount Created successfully").encode('utf-8')))
        else:
            self.clientSocket.send(bytes(("\n\n\nYou are already signed up").encode('utf-8')))

        conn.commit()
        rows = cursor.execute("SELECT * FROM account").fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print('nothing')

    def sign_in(self):
        cursor.execute("SELECT * FROM account WHERE accountNum = ?", (self.accNumber,))
        data1 = cursor.fetchall()
        if len(data1) == 0:
            print("Your account number is incorrect")
            self.clientSocket.send(bytes(("Your account number is incorrect...").encode('utf-8')))

        else:
            self.clientSocket.send(bytes(("Welcome to your account!").encode('utf-8')))

            rows = cursor.execute("SELECT * FROM account").fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print('nothing')

    def deposit(self, pin):

        cursor.execute("SELECT pinCode FROM account WHERE accountNum = ?", (self.accNumber,))
        cur_pin = cursor.fetchall()
        for row in cur_pin:
            self.pinCode = row[0]
        if pin == self.pinCode:
            mes = "How much money would you like to deposit?"
            self.clientSocket.send(bytes(mes.encode('utf-8')))
            dep = self.clientSocket.recv(1024)
            dep = dep.decode('utf-8')
            dep = int(dep)

            cursor.execute("SELECT money FROM account WHERE accountNum = ?", (self.accNumber,))
            cur_money = cursor.fetchall()
            for row in cur_money:
                money = row[0]

            self.moneyInTheBank = money
            self.moneyInTheBank = money + dep
            print("deposit completed\ntotal money in Bank is:{} ".format(self.moneyInTheBank))
            self.clientSocket.send(bytes(("deposit completed\ntotal money in Bank is:{} ".format(self.moneyInTheBank)).encode('utf-8')))

            sentence = "UPDATE account SET money= :new_money WHERE accountNum= :accNum "
            cursor.execute(sentence, {"accNum": self.accNumber, "new_money": self.moneyInTheBank}, )
            conn.commit()
        else:
            print("Incorrect PIN number")
            self.clientSocket.send(bytes(("Incorrect PIN number.").encode('utf-8')))


    def withdraw(self,pin):
        if self.accNumber == 0:
            self.clientSocket.send(bytes(("You must enter your account first").encode('utf-8')))
        else:
            cursor.execute("SELECT pinCode FROM account WHERE accountNum = ?", (self.accNumber,))
            curPin = cursor.fetchall()
            for row in curPin:
                self.pinCode = row[0]
            if pin == self.pinCode:
                cursor.execute("SELECT money FROM account WHERE accountNum = ?", (self.accNumber,))
                cur_money = cursor.fetchall()
                for row in cur_money:
                    money = row[0]
                self.moneyInTheBank = money

                mes = "How much money do you want to withdraw?"
                self.clientSocket.send(bytes(mes.encode('utf-8')))
                wid = self.clientSocket.recv(1024)
                wid = wid.decode('utf-8')
                wid = int(wid)
                if wid > self.moneyInTheBank:
                    print("You don't have enough money in bank")
                    self.clientSocket.send(bytes(("You don't have enough money in bank").encode('utf-8')))
                else:
                    self.moneyInTheBank = self.moneyInTheBank - wid
                    print("withdraw completed\ntotal money in Bank is:{} ".format(self.moneyInTheBank))
                    self.clientSocket.send(bytes(("withdraw completed\ntotal money in Bank is:{} "
                                                  .format(self.moneyInTheBank)).encode('utf-8')))

                    sentence = "UPDATE account SET money= :new_money WHERE accountNum= :accNum "
                    cursor.execute(sentence, {"accNum": self.accNumber, "new_money": self.moneyInTheBank}, )
                    conn.commit()
            else:
                self.clientSocket.send(bytes(("Incorrect PIN number.").encode('utf-8')))
            rows = cursor.execute("SELECT * FROM account").fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print('nothing')

    def bankBalance(self):
        if self.accNumber == 0:
            self.clientSocket.send(bytes(("You must enter your account first").encode('utf-8')))
        else:
            cursor.execute("SELECT money FROM account WHERE accountNum = ?", (self.accNumber,))
            id_row = cursor.fetchall()
            for row in id_row:
                id = row[0]
            self.moneyInTheBank = id
            print("Your balance at this current time is:{} ".format(self.moneyInTheBank))
            self.clientSocket.send(bytes(("Your balance at this current time is:{} "
                                          .format(self.moneyInTheBank)).encode('utf-8')))

def main():
    server()

if __name__ == '__main__':
    main()