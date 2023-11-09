p = float(input("Enter Initial principal: "))

r = float(input("Enter initial rate: "))

t = float(input("Enter number of times interest per time period: "))

n = float(input("Enter number of time period elapsed: "))

SI = p * (1 + r * t)
CI = p * (1 + r/n)** n * t
print("YUSUF AND SONS COMPANY")
print(f'Simple interest : {SI}')
print(f'Compound interest : {CI}')