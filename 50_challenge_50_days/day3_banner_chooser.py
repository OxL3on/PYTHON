# Day 3: Conditional Logic (Simple Banner Grabber)
# Take a user’s choice (1 for HTTP, 2 for SSH) and print a banner.
# Concepts: if/elif/else, comparison operators.

def main():
    user_choice = (input("Choose (1: HTTP Banner || 2: SSH Banner): "))

    if user_choice.strip().isdigit():
        if int(user_choice) == 1 : 
            print("############################")
            print("##          HTTP          ##")
            print("############################")
        
        elif int(user_choice) == 2 :
            print("############################")
            print("##           SSH          ##")
            print("############################")
    else:
        print("Invalid Choice : Choice between 1 and 2")

if __name__ == "__main__":
    main()