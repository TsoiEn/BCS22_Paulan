class Palindrome:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"'{item}' is successfully pushed")
        print("-----------------------------\n")

    # to remove an item from the stack
    def pop(self):
        if self.stack:
            print (f"lenght of stack 0 - {len(self.stack)-1}")
            index_input = input("Enter the index to pop from the stack: ")
            
            # Check if input is a positive integer
            if index_input.isdigit():  
                index = int(index_input)
                
                # check if the input index is in the range of the indexes in the stack
                # remove the item from the stack
                if 0 <= index < len(self.stack):
                    item = self.stack.pop(index)
                    print(f"Removed item at index {index}: {item}")
                    print("-----------------------------\n")
                else:
                    print(f"Invalid index. Index should be between 0 and {len(self.stack) - 1}.")
                    print("-----------------------------\n")
            else:
                print("Invalid input. Please enter a valid integer.\n")
                print("-----------------------------\n")
        else:
            print("Stack is empty.")
            print("-----------------------------\n")
            return None

    # remove the punctuation and spaces 
    def remove_punctuation(self, s, remove_spaces=True):
        punc = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        res = ""
        for i in s:
            if (i not in punc) and (remove_spaces and i != ' '):
                res += i
        return res
    
    def custom_lower(self, input_string):
        result = ""
        for char in input_string:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
        return result


    # uses the remove_punctuation method and make the string in the stack in lower case
    # returns a new string with new structure
    def clean_string(self, s):
        cleaned_str = self.custom_lower(self.remove_punctuation(s))
        return cleaned_str


    
    def display(self, check_palindrome=True):
        if self.stack:
            # show the contents of the stack
            print("===========================\n")
            print("Stack contents:")
            print(self.stack)

            # string stack to be reversed
            # connect all strings in the stack together
            # print the connected string without the punctuation and spaces 
            for item in reversed(self.stack):
                pass
            connected_string = ''.join(self.stack)
            cleaned_str = self.clean_string(connected_string)
            print (cleaned_str)

            #check if it is palindrome or not
            if check_palindrome:
                # check if cleaned_str is equal to its reverse 
                if cleaned_str == cleaned_str[::-1]:  
                    print("It is a palindrome.\n")
                    print("-----------------------------")
                else:
                    print("It is not a palindrome.")
                    print("-----------------------------\n")
        else:
            print("Stack is empty.")
            print("-----------------------------\n")


palindrome_checker = Palindrome()

while True:
    print("Enter the option below:")
    print("[1] Push Operation\n[2] Pop Operation\n[3] Display Stack and Check Palindrome\n[4] Exit")

    option = int(input())

    if option == 1:
        print("PUSH OPERATION")
        print("==============")
        data = input("Enter the data to push onto the stack: ")
        palindrome_checker.push(data)
    elif option == 2:
        print("POP OPERATION")
        print("=============")
        palindrome_checker.pop()
    elif option == 3:
        palindrome_checker.display()
    elif option == 4:
        break
    else:
        print("Invalid option. Please enter a valid option.\n")
