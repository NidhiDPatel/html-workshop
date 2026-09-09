numbers = [10, 25, 5, 40, 15]

largest = max(numbers)
smallest = min(numbers)

print("Largest element:", largest)
print("Smallest element:", smallest)

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

numbers = [10, 20, 10, 30, 10, 40, 20]

num = int(input("Enter a number: "))

count = numbers.count(num)

print(num, "appears", count, "times")

numbers = [10, 20, 10, 30, 10, 40, 20]

num = int(input("Enter a number: "))

count = numbers.count(num)

print(num, "appears", count, "times")


# Create
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:", student)

# Read
print("Student Name:", student["name"])

# Update
student["age"] = 21
print("After Update:", student)

# Delete
del student["course"]
print("After Delete:", student)



