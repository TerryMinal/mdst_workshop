"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
from random import randrange
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    # try:
    #     in_num = int(input()) 
    # except:
    #     print("HAHAHAHAHAHA YOU'RE SO FUNNYYYY ._. Let's try that again")
    #     part1(num)
    
    if num%2 == 0:
        print("even")
    else:
        print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    num = randrange(1, 9)

    part2_helper(num)
    

def part2_helper(num):
    try:
        in_num = int(input()) 
    except:
        print("HAHAHAHAHAHA YOU'RE SO FUNNYYYY ._. Let's try that again")
        return part2_helper(num)
    
    if in_num == num:
        print("Congrats! You succeeded in something life. Cherish this moment cause you won't get many of them")
        return 0
    
    elif in_num < num:
        print("You underestimate me. Guess higher")
        return part2_helper(num)
    
    else:
        print("my GPA isn't even that high. Guess lower")
        return part2_helper(num)





def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    beg = 0
    end = len(string) - 1

    while (beg <= end):
        if (string[beg] != string[end]):
            print("NAH")
            return 
        beg += 1
        end -= 1

    print("YUP")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    with open(filename, 'w') as f:
        usr = encr(username)
        ps = encr(password)
        f.write(usr.decode() + "\n" + ps.decode())
    return 

    

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    usr = ''
    ps = ''
    with open(filename, 'r') as f:
        usr = f.readline().strip()
        ps = f.readline().strip()
        usre = decr(usr)
        ps = decr(ps)

        print("username: " + usre)
        print("password: " + ps)
            
    if password is not None:
        with open(filename, 'w') as f:
            f.write(usr + "\n" + encr(password).decode())

        
    return 


def encr(string):
    return base64.b64encode(string.encode())

def decr(string):
    # print(string)
    return base64.b64decode(string).decode()


if __name__ == "__main__":
    # part1(3)  # odd!
    # part1(4)  # even!
    # part2()
    # part3("ratrace")  # False
    # part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
