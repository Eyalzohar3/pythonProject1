import socket
import sys
"""targil 7"""

HOST = '127.0.0.1'
PORT = 33010
ADDR = (HOST, PORT)

class client:
    def __init__(self):
        self.mySocket = socket.socket()
        self.account = 0
        self.connection()
        self.bankFunctions()
    def connection(self):
        try:
            self.mySocket.connect((HOST, PORT))
        except:
            print("The server is not availible")
            self.mySocket.close()
            sys.exit()
        fromServer = self.mySocket.recv(1024)
        fromServer = fromServer.decode()
        print(fromServer)
        message = input("")

        while message != "7":
            self.mySocket.send(message.encode())
            if message == '1':
                while True:
                    try:
                        accNumber = int(input("Enter the account number : "))
                        if accNumber <= 0:
                            print("Incorrect account number. ")
                        else:
                            break
                    except:
                        print("Incorrect account number. ")
                accNumber = str(accNumber)
                self.mySocket.send(bytes(accNumber.encode('utf-8')))
                name = input("Enter the account holder name : ")
                self.mySocket.send(bytes(name.encode('utf-8')))
                while True:
                    pinCode = input("Enter PIN number (must be 4 digit) : ")
                    if len(pinCode) != 4:
                        print("Incorrect PIN number. ")
                    else:
                        try:
                            int_pin = int(pinCode)
                            if int_pin <= 0:
                                print("Incorrect PIN number. ")
                            else:
                                break
                        except:
                            print("Incorrect PIN number. ")
                self.mySocket.send(bytes(pinCode.encode('utf-8')))
                moneyInTheBank = int(input("Enter your starting amount of money: "))
                moneyInTheBank = str(moneyInTheBank)
                self.mySocket.send(bytes(moneyInTheBank.encode('utf-8')))
                answer = self.mySocket.recv(1024)
                answer = answer.decode('utf-8')
                print(answer)
                break
            elif message == '2':
                account_number = input("Enter the account number : ")
                self.mySocket.send(bytes(account_number.encode('utf-8')))
                answer = self.mySocket.recv(1024)
                answer = answer.decode('utf-8')
                print(answer)
                break
        if message =='7':
            print("Good day!")
            self.mySocket.close()
            sys.exit()

    def bankFunctions(self):
        fromServer = self.mySocket.recv(1024)
        fromServer = fromServer.decode()
        print(fromServer)
        message = input("")
        while message != "7":
            self.mySocket.send(message.encode())
            if message == '4':
                while True:
                    pin = int(input("Enter your PIN number "))
                    pin = str(pin)

                    if len(pin) != 4:
                        print("Incorrect PIN number.")
                    else:
                        try:
                            int_pin = int(pin)
                            if int_pin <= 0:
                                print("Incorrect PIN number.")
                            else:
                                break
                        except:
                            print("Incorrect PIN number.")

                self.mySocket.send(bytes(pin.encode('utf-8')))
                moneyToDep = self.mySocket.recv(1024)
                moneyToDep = moneyToDep.decode('utf-8')
                print(moneyToDep)
                howMuchMoney = input("")
                self.mySocket.send(bytes(howMuchMoney.encode('utf-8')))
                totalMoney = self.mySocket.recv(1024)
                totalMoney = totalMoney.decode('utf-8')
                print(totalMoney)
            elif message == '5':
                while True:
                    pin = int(input("Enter your PIN number "))
                    pin = str(pin)
                    if len(pin) != 4:
                        print("Incorrect PIN number.")
                    else:
                        try:
                            int_pin = int(pin)
                            if int_pin <= 0:
                                print("Incorrect PIN number.")
                            else:
                                break
                        except:
                            print("Incorrect PIN number.")

                self.mySocket.send(bytes(pin.encode('utf-8')))
                moneyToWid = self.mySocket.recv(1024)
                moneyToWid = moneyToWid.decode('utf-8')
                print(moneyToWid)
                howMuchMoney = input("")
                self.mySocket.send(bytes(howMuchMoney.encode('utf-8')))
                totalMoney = self.mySocket.recv(1024)
                totalMoney = totalMoney.decode('utf-8')
                print(totalMoney)

            elif message == '6':
                path = 'balance'
                self.mySocket.send(bytes(path.encode('utf-8')))
                totalMoney = self.mySocket.recv(1024)
                totalMoney = totalMoney.decode('utf-8')
                print(totalMoney)
            message = input("Enter new request:")
        print("Good day!")
        self.mySocket.close()
        sys.exit()

def main():
    client()

if __name__ == '__main__':
    main()