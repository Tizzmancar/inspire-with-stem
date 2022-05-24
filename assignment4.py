# write a program to withdraw ksh 25000 if account balance is btw 100000 to 200000
#30% if acc balance btw 500000 and 1000000
#above 1000000 deduct 15000
acc_bal= input("enter account balance")
if (int(acc_bal)>100000) and (int(acc_bal)<200000):
    acc_bal= int(acc_bal)-25000
    print("we have deducted 25000")
elif (int(acc_bal)>500000) and (int(acc_bal)<1000000):
    acc_bal= int(acc_bal)-(int(acc_bal)*0.3)
    print("we have deducted 30%")
elif(int(acc_bal)>1000000):
    acc_bal= int(acc_bal)-15000
    print("we have deducted 15000")
else:
    print("no deductions")

