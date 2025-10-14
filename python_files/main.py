lambda add(a, x): return a+x

if __name__ == "__main__":
	try:
		print(add(4, 5))
	except Exception as e:
		print("Неверные параметры в add")
else:
	print("isn't main")
