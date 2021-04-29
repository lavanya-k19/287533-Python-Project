'''
we have to import csv file for file
handling functions
'''
import csv
'''
here we are creating the 
empty list 
for storing records
'''
listt = []
'''
it is the main class 
for entire program
'''
class majordonor:

    def __init__(self, name, phone, mail, group, amount):

        self.name = name
        self.phone = phone
        self.mail = mail
        self.group = group
        self.amount = amount

class bloodgrp(majordonor):

    def __init__(self, name, phone, mail, group, amount):
        majordonor.__init__(self, name, phone, mail, group, amount)

    def search_donor(self, phone):

        f = 0

        for line in listt:

            alpha, beta, ceta, deta, eta, feta = line

            if beta == phone:

                print("Record is Found:\n")
                print(line)
                f = 1
                return "Found"
        if f != 1:
            print("Record is not found.")
            return "Not Found"

    def read_data(self, listt):
        file = open('filedata.csv', mode = 'r')
        csvFile = csv.reader(file)
        for line in csvFile:
            listt.append(line)

    def write_data(self, listt):

        file1 = open('filedata.txt', 'w')

        for line in listt:

            alpha, beta, ceta, deta, eta, feta = line
            '''writing 
            the 
            functions
            '''
            file1.write("Name:")
            file1.write(alpha)
            file1.write("\n")

            file1.write("Phone Num:")
            file1.write(beta)
            file1.write("\n")

            file1.write("Mail ID:")
            file1.write(ceta)
            file1.write("\n")

            file1.write("Blood Group:")
            file1.write(deta)
            file1.write("\n")

            file1.write("Amount:")
            file1.write(eta)
            file1.write("\n")

            file1.write("\n")
            file1.write("\n")
            '''
            it will prints data records

            '''
            print("Name:")
            print(alpha)
            print("\n")

            print("Phone Num:")
            print(beta)
            print("\n")

            print("Mail ID:")
            print(ceta)
            print("\n")

            print("Blood Group:")
            print(eta)
            print("\n")

            print("Amount:")
            print(deta)
            print("\n")

            print("\n")
            print("\n")