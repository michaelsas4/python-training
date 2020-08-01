def say_hi(name, username, password, email, age, address, monthlyincome, yearlyincome):
    print("my name is " + name + ", my username is " + username + ", my password is " + password + ", my email is" + email + ", i am" + age + ", my address" + address + ", my monthlyincome is" + monthlyincome + ", my yearlyincome" +yearlyincome)
say_hi("Mike", "Mike", "5656", "gmail.com", "65", "no 6 majidun awori", "655" , "666")





Name = input("enter your name: " ) 
Age = input("enter your age: ")
location = input("enter your location: ")
Amountborrowed = input("enter amount borrowed: ")
interest = str(int(Amountborrowed) * 0.25)
total = str(int(Amountborrowed) *12)
print("my is: " + Name + "and am: " + Age + "i stay at: " + location)
print("i borrowed: " + Amountborrowed + "with: " + interest + "and the total is: " +total)