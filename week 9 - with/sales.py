num_days=int(input("How many sales day? :"))
sales_file=open('sales.text','w')
for count in range (1,num_days + 1):
    sales=float(input('How many sales did you do today: ' + str(count) + ':' ))
    sales_file.write(str(sales) + '\n')
sales_file.close()
sales_file1=open('sales.text','r')
for count in range (1,num_days +1):
    sales=float(sales_file1.readline())
    print(sales)
sales_file1.close