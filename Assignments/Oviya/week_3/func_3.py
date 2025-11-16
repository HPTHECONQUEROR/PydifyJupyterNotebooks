even_numbers=lambda nums:[x for x in nums if x%2==0]
user_input= input("enter numbers")
nums=[int(n) for n in user_input.split()]
print(even_numbers(nums))