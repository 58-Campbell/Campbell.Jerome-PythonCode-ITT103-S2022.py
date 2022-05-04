#Author:Jerome Campbell
#Date Created:April 30, 2022
#Course: ITT103
#Purpose: The purpose of this program is to calculate commission received by a salesperson at JamEx Limited based on theamount of sales made and the catergory to which the salesperson belong
#PROGRAM:JamEx Limited Salesperson Commission calculation

#Calculation of JamEx Limited Salesperson Commission

addMore = "y"

while addMore == "y":        
        class1 = int(input("please enter your class 1,2 OR 3: "))
        if class1 == 1:
                sales_amt = float(input("please enter sales_amt: "))
                sales_person_number = int(input(" please enter your unique number "))
                        
                first_last_name = input("Please Enter first_last name: ")

                if sales_amt <= 1000 :
                        rate = 0.06
                        commission = (rate * sales_amt)
                
                        print("your commission is: $", \
                        format(commission, ',.2f'), sep='')
                elif sales_amt > 1000 and sales_amt < 2000 :
                        rate = 0.07
                        commission = (rate * sales_amt)
                
                        print("your commission is: $", \
                        format(commission, ',.2f'), sep='')
                elif sales_amt >= 2000 :
                        rate = 0.10
                        commission = (rate * sales_amt)
        elif class1 == 2 :
                sales_amt = float(input("please enter sales_amt: "))
                print("please press y for yes or any other key to end")
                sales_person_number = int(input("please enter sales_person_number: "))
                first_last_name = input("Please Enter first_last name: ")

                if sales_amt <= 1000 :
                        rate = 0.04
                        commission = (rate * sales_amt)
                
                        print("your commission is: $", \
                        format(commission, ',.2f'), sep='')
                elif sales_amt > 1000 :
                        rate = 0.06
                        commission = (rate * sales_amt)
                
                        print("your commission is: $", \
                        format(commission, ',.2f'), sep='')
        elif class1 == 3:
                rate = 0.045
                commission = (rate * sales_amt)
                
                print("your commission is: $", \
                format(commission, ',.2f'), sep='')

        

        else:
                print("Invalid entry")
                cont = input("Do you want to continue: y/n: ")

                if cont == "n" or cont == "N" :
                        print("you have reached the end of this program")
                        
                else:
                        continue
        print("Press y to addmore data or seclect any other key to end")
        addMore = input("Do you want to add records? y/n: ")
print("Thank you for using this progam goobye")
        

        
