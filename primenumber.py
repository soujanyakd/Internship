#•	Develop code, which prints all Prime Numbers between 0 to 10, using list comprehension

prime_number=[n for n in range(2,10)if all((n%i)!=0 for i in range(2,n))]
print(prime_number)