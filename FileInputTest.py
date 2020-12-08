j = open('ofile.txt', 'w')
j.write("John Told Me Something\nHohohoho")
j = open('ofile.txt')
print(j.read())
