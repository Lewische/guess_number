import random
a = random.randint(1,9)
b = random.randint(1,9)
while a == b:
	b = random.randint(1,9)
c = random.randint(1,9)
while c == b or c == a:
	c = random.randint(1,9)
d = random.randint(1,9)
while d == b or d == a or d == c:
	d = random.randint(1,9)
x = a * 1000 + b * 100 + c * 10 + d
print('歡迎來到猜數字的遊戲，會有四個由1至9的數字依照排順序排列，您可以在下方輸入您想猜的數字，若數字正確且順序正確，則會得到一個A，若數字正確惟順序不正確，則會得到一個B，開始遊戲吧!')
guess = input('請輸入要猜的數字:')
x = str(x)
p = 0
while guess != x:
	p = p + 1
	if guess[0] == str(a):
	    y = 1
	    z = 0
	elif guess[1] == str(a):
	    y = 0
	    z = 1
	elif guess[2] == str(a):
	    y = 0
	    z = 1
	elif guess[3] == str(a):
	    y = 0
	    z = 1
	else:
	 	y = 0
	 	z = 0
	if guess[0] == str(b):
	    yy = 0
	    zz = 1
	elif guess[1] == str(b):
		yy = 1
		zz = 0
	elif guess[2] == str(b):
		yy = 0
		zz = 1
	elif guess[3] == str(b):
	    yy = 0
	    zz = 1
	else:
	 	yy = 0
	 	zz = 0
	if guess[0] == str(c):
	    yyy = 0
	    zzz = 1
	elif guess[1] == str(c):
	    yyy = 0
	    zzz = 1
	elif guess[2] == str(c):
	    yyy = 1
	    zzz = 0
	elif guess[3] == str(c):
	    yyy = 0
	    zzz = 1
	else:
	 	yyy = 0
	 	zzz = 0
	if guess[0] == str(d):
	    yyyy = 0
	    zzzz = 1
	elif guess[1] == str(d):
	    yyyy = 0
	    zzzz = 1
	elif guess[2] == str(d):
	    yyyy = 0
	    zzzz = 1
	elif guess[3] == str(d):
	    yyyy = 1
	    zzzz = 0
	else:
	 	yyyy = 0
	 	zzzz = 0
	print(y+yy+yyy+yyyy,'A', z+zz+zzz+zzzz, 'B，繼續努力猜喔!已經猜了', p ,'次了喔')
	guess = input('請輸入要猜的數字:')
print('猜中了!')






 
	