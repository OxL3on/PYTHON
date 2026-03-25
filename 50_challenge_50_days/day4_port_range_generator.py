# Day 4: Loops (Port Range Generator)
# Use a for loop to print ports 1–1024. Then modify to ask user for a range.
# Concepts: for loops, range(), while loops.

def main():
    for i in range(1, 1025, 1):
        print(i, end=" ")
    
    print("\n")

    start_with = int(input("Enter the number you want the loop to start with: "))
    end_with = int(input("Enter the number you want the loop to end with: "))

    for j in range(start_with, end_with+1):
        print(j, end=" ")

if __name__ == "__main__":
    main()