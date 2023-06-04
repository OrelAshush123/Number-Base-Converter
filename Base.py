def convert_char_to_num(char):  
    """
    This function converts a character 'A' to 'F' to its corresponding 
    integer value from 10 to 15. Otherwise, it returns False.
    """
    if char == 'A': return 10
    elif char == 'B': return 11
    elif char == 'C': return 12
    elif char == 'D': return 13
    elif char == 'E': return 14
    elif char == 'F': return 15
    
    else: return False

def convert_num_to_char(num):
    """
    This function converts an integer value from 10 to 15 to 
    its corresponding character 'A' to 'F'. Otherwise, it returns False.
    """
    if num == 10: return 'A'
    elif num == 11: return 'B'
    elif num == 12: return 'C'
    elif num == 13: return 'D'
    elif num == 14: return 'E'
    elif num == 15: return 'F'
    
    else: return False
def if_Friend(Fb,Tb): # (from base)-"Fb" (to base)-"Tb"
    """
    This function checks if two bases, Fb and Tb, are "friends." 
    Two bases are considered friends if one can be 
    obtained by raising the other to a power between 1 and 8.
    """
    if Fb < Tb:
        for i in range(1,9):
            if Fb**i == Tb:
                return True
    else:
        for i in range(1,9):
            if Tb**i == Fb:
                return True
            
    return False

def This_legal(num,B):
    """
    This function checks if a given number 'num' is valid in a given base 'B'.
    It ensures that all the characters in the number are within the valid range of the base.
    """
    try:
        elements = [".","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        myElements = elements[:B+1]
        for i in num:
            if i not in myElements: return False
        
        return True
    
    except:
        return False
    
################## From B_ To B10  #######################

def __inner_To_B10(listC,Fb,start,stop):
    """
    This is a helper function for converting a number from base Fb to base 10.
    It performs the conversion using the positional notation and returns the result.
    """
    answer = 0
    n = 0
    for i in range(start, stop, -1):
        answer += listC[n]*Fb**i
        n += 1
    return answer

def To_B10(num, Fb, Tb):
    """
    This function converts a number num from base Fb to base 10 or from a base with a decimal 
    point (e.g., 1.01) to base 10. It separates the integer part from the fractional part, 
    converts each part separately, and returns the sum of the two converted parts.
    """
    CharOfNum = []
    for i in num:
        if i == '.':
            num = num[(len(CharOfNum)+1):]
            break 
        try:
            CharOfNum.append(int(i)) # if there is a digit that is above 10 (A-F), it will throw an error.
        except:  
            CharOfNum.append(convert_char_to_num(i)) # and the func "convert_char_to_num" will be activated. 
    else:   
        return __inner_To_B10(CharOfNum, Fb, len(CharOfNum)-1, -1) # 
    
    CharOfNumOverdot = []
    for i in num:
        try:
            CharOfNumOverdot.append(int(i))
        except:
            CharOfNumOverdot.append(convert_char_to_num(i))
    
    return __inner_To_B10(CharOfNum,Fb, len(CharOfNum)-1, -1) + __inner_To_B10(CharOfNumOverdot,Fb, -1, (len(CharOfNumOverdot)+1)*-1)

########################## From B10 To B_  #######################
def __inner_From_B10(listC):
    """
    This is a helper function for converting a number from base 10 to another base. 
    It converts the individual digits to their corresponding characters if they are greater than 9.
    """
    answer = ""
    for i in listC:
        if i > 9 and i < 16:
            answer += convert_num_to_char(num)
        else:
            answer += str(i)
         
    return answer
    
def From_B10(numS, Fb, Tb):
    """
    This function converts a number 'numS' from base 10 to base Tb. 
    It first checks if the input is an integer or a float.
    - If it's an integer, it performs the conversion by continuously dividing 
      the number by the target base and keeping track of the remainders. 
      Then it uses the helper function '__inner_From_B10' to convert 
      the remainders to their corresponding characters.
    - If it's a float, it separates the integer part from the fractional 
      part and converts each part separately. It performs a similar 
      conversion process as the integer case and appends the fractional part 
      after the integer part using a dot as a separator.
    """
    list_of_char = []
    try:
        num = int(numS)
        while num > 0:
            list_of_char.append(num % Tb)
            num = num//Tb
        return __inner_From_B10(list_of_char[::-1])
    except:
        if numS[0] == '0':
            num = float(numS)
            while num > 0:
                z = num * Tb
                z = float("%.14f" % z)
                _num = int(z//1)
                list_of_char.append(_num)
                num = float("0"+(str(z)[(str(z).index(".")):]))
            return "0." + __inner_From_B10(list_of_char)
    
        else:
            # the long way (1---2 => 1 + 2)
            num1 = int(numS[:(numS.index('.'))])
            num2 = float(("0" + numS[(numS.index('.')):]))
            while num1 > 0:
                _num1 = num1 % Tb
                list_of_char.append(_num1)
                num1 = num1//Tb

            anser1 = __inner_From_B10(list_of_char[::-1])
            list_of_char.clear()

            while num2 > 0:
                z = num2 * Tb
                z = float("%.14f" % z)
                _num2 = int(z//1)
                list_of_char.append(_num2)
                num2 = float("0"+(str(z)[(str(z).index(".")):]))
        
            anser2 = "." + __inner_From_B10(list_of_char)
            return anser1 + anser2
            
########################### MAIN FNANCTION ########################

def main():
    """
    This is the main function that interacts with the user. It takes the number to convert ('num'), 
    the base to convert from ('FromB'), and the base to convert to ('ToB'). 
    It performs several checks and calls the conversion functions accordingly. 
    It also checks if the bases are friends and prints a message accordingly. 
    Finally, it returns the conversion result as a formatted string.
    """
    num = input("Enter a num:")
    FromB = int(input("From B->"))
    ToB = int(input("To B->"))
    
    if FromB is ToB: return False
    if not This_legal(num, FromB):
        return False
             
    if ToB == 10:   
        Anser = To_B10(num,FromB,ToB)
        return "({}){} = ({}){}".format(num, FromB, Anser, ToB)
    elif FromB == 10:
        Anser = From_B10(num,FromB,ToB)
        return "({}){} = ({}){}".format(num, FromB, Anser, ToB)
    
    if if_Friend(FromB, ToB): print("They are friends!")    
    else: print("They are not friends!")

    _num = To_B10(num,FromB,10)
    Anser = From_B10(str(_num),10,ToB)
    return "({}){} = ({}){}".format(num, FromB, Anser, ToB)
        

if __name__ == "__main__":
    """
    This part of the code executes the main function in a loop, 
    continuously taking user input and performing conversions until the program is interrupted.
    """
    while True:
        m = main() 
        if m is not False: print(m)
        else: print("illegal number")

"""
Overall, the code provides a way to convert numbers between different bases, 
including bases with decimal points. It incorporates checks for input 
validity and ensures the bases are "friends" for certain conversions. 
The code could benefit from better variable names and more descriptive 
comments to enhance readability and understanding.
"""
