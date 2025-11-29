class MathOperations:

 def factorial(self, n):

    if n == 0:
        return 1
    return n * self.factorial(n - 1)  


 def fibonacci(self, n):

    if n <= 1:
        return self.fibonacci

    return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    # As calls reach base cases, results pop back up and combine.


if __name__ == "__main__":
    opt=MathOperations #object definied here
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    value = int(input("Enter a number: "))

    if choice == "1":
        ans = opt.factorial(value) 
    elif choice == "2":
        ans = opt.fibonacci(value)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)
