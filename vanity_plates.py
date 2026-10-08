def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return True
#if not (2 <= len(plate) <= 6):
#   return False 

#elif is_valid(plate.isalnum()):
#   return False
#not text[:2].isdigit()
#not text[:1].isdigit(0)
#.isalpha()
#.isdigit()
main()

#.isalpha() checks for letters
#.isdigit() checks for numbers
#if not (2 <= len(plate) <= 6):
#   return False                 checks if the plate characters are not between 2 or 6
# to create a statement to return false if it contains non-alphanumeric characters use the isalnum() sting method. if is_valid(plate.isalnum()):
#   return False
# to create a statement to return false if the first two characters are numbers use: not text[:2].isdigit()
# to create a statement to find the first number and return false if it is zero: not text[:1].isdigit(0)
# to use a loop to identify if there are numbers and set a variable to true if so. 
# Then check if there are letters after that point if the variable is true. If so, return false. use: 