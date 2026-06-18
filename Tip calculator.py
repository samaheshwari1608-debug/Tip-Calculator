# Creating A Tip Calculator:
'''
 what is tip calculator: a tip calculator is a simple tool that calculates how much tip(service charge) you should give the and
the total amount you need to pay.
'''
Bill= float(input("Enter The Bill Amount:\n"))
choice= input("Do You Want To Pay Tip?(Yes/No):\n")
if choice.lower()=="yes":
    Tip_Percent= float(input("Enter The Tip Percentage:\n"))
    Tip_Amount= Bill*Tip_Percent/100
    print("Tip Amount is:", Tip_Amount)
    TotalBill= Bill + Tip_Amount
    print("Total Amount is:", TotalBill)
    print("Thanks, Visit Us Again")
else:    
    print("No Tip Added")
    print("Total Amount is", Bill)
