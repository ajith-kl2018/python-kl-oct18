import time
import webbrowser

print ("Starting at :", time.ctime())
for step in range(3):
	time.sleep(10)
	webbrowser.open("http://ddd")
	print("Break :",step)

## Python documentation reference

