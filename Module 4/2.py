#Calculating Time

n=int(input("Enter The Units Of Efforts By Ashok Goel: "))
hours=n//3600
minutes=(n-hours*3600)//60
seconds=(n-hours*3600-minutes*60)
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")