my_name=input('Please enter your name: ')

Please enter your name: Ananya

my_name
Out[2]: 'Ananya'

file=open('name.txt',mode='w')

file
Out[4]: <_io.TextIOWrapper name='name.txt' mode='w' encoding='cp1252'>

file.write(my_name)
Out[5]: 6

file.close()

file=open('name.txt',mode='r')

file.read()
Out[8]: 'Ananya'