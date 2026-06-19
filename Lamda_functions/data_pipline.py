n=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(n)

odd=list(filter(lambda x: x%2!=0, n))
print(odd)

squares=list(map(lambda x: x**2, n))
print(squares)

sum_of_squares=sum(squares)
print(sum_of_squares)