# Author: Alvaro Rivas
# Date: 4/10/16
# Language: Python
# Version: PyCharm Community Edition 4.0.5
# Description: 
# 		Uses regular expressions to verify if phone number entered by user is of fomat:
# 		nnn-nnn-nnnn 				(nnn) nnn-nnnn 
# 		nnnnnnnnnn		   			 nnn nnn nnnn 
# 		1-nnn-nnn-nnnn 				 nnn) nnn-nnnn 
# 		nnn/nnn-nnnn 
# 		where n is a digit between 0 and 9
# ======================================================================================

import re

if __name__ == '__main__':
# Input: Phone number from user 
    phoneNum = raw_input("Enter Phone Number:")
    print(phoneNum)
# Regular Expression
    phoneNum1_re = re.compile('^(1-|\()?[0-9]{3}(-|[" "]|\)|\/)?[0-9]{3}(-|[" "])?[0-9]{4}$')
# if phone number matches format then valid else invalid
    if phoneNum1_re.match(phoneNum):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        print(phoneNum)