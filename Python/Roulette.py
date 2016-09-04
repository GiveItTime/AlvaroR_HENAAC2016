#   Author: Alvaro Rivas
#   Date: 04/02/15
#   File: Roulette
#   Program simulates a game of Roulette and all the bets possible. Informs user if they
#   win or loose and calculates winnings,if any.
#=======================================================================================
#   Imports random class necessary to simulate Spin of Roulette Wheel
import random
#========================================================================================
#   Function Spins Wheel, using random to simulate wheel, returns an integer 0-36
def SpinWheel():
    print "Wheel is spinning"
    return random.randint(0,36)
#   end of Spin Wheel Function
#=========================================================================================
#   Function Straight up handles a straight bet, Pays 35 to 1 return 35 if hit 0 otherwise
def StraightUp():
    print "Pick a number 0-36:"
    numberStraight = input()
#   Spins Roulette Wheel
    ballStraight = SpinWheel()
#   Checks to See if you won your bet
    if ballStraight == numberStraight:
        return 35
    else:
        return 0
#   end of Straight Up Function
#==============================================================================================
#   Function Split handles Split bets, Pays 17 to 1, returns 17 if hit 0 otherwise
def Split():
    print "Choose your split bet:"
    print "1) 1,2:\t  2) 1,4:\t  3) 2,3:\t  4) 2,5:\t 5) 3,6:\t 6) 4,5:"
    print "7) 4,7:\t  8) 5,6:\t  9) 5,8:\t10) 6,9:\t11) 7,8:\t12) 7,10:"
    print "13) 8,9:\t14) 8,11:\t15) 9,12:\t16) 10,11:\t17) 10,13:\t18) 11,12:"
    print "19) 11,14:\t20) 12,15:\t21) 13,14:\t22) 13,16:\t23) 14,15:\t24) 14,17:"
    print "25) 15,18:\t26) 16,17:\t27) 16,19:\t28) 17,18:\t29) 17,20:\t30) 18,21:"
    print "31) 19,20:\t32) 19,22:\t33) 20,21:\t34) 20,23:\t35) 21,24:\t36) 22,23:"
    print "37) 22,25:\t38) 23,24:\t39) 23,26:\t40) 24,27:\t41) 25,26:\t42) 25,28:"
    print "43) 26,27:\t44) 26,29:\t45) 27,30:\t46) 28,29:\t47) 28,31:\t48) 29,30:"
    print "49) 29,32:\t50) 30,33:\t51) 31,32:\t52) 31,34:\t53) 32,33:\t54) 32,35:"
    print "55) 33,36:\t56) 34,35:\t57) 35,36:"
    numberSplit = input()
#   Spins Roulette Wheel
    ballSplit = SpinWheel()
#   Checks to see type of Split bet user makes and if they won
    if numberSplit == 1:
        if ballSplit == 1 | ballSplit == 2:
            return 17
        else:
            return 0
    elif numberSplit == 2:
        if ballSplit == 1 | ballSplit == 4:
            return 17
        else:
            return 0
    elif numberSplit == 3:
        if ballSplit == 2 | ballSplit == 3:
            return 17
        else:
            return 0
    elif numberSplit == 4:
        if ballSplit == 2 | ballSplit == 5:
            return 17
        else:
            return 0
    elif numberSplit == 5:
        if ballSplit == 3 | ballSplit == 6:
            return 17
        else:
            return 0
    elif numberSplit == 6:
        if ballSplit == 4 | ballSplit == 5:
            return 17
        else:
            return 0
    elif numberSplit == 7:
        if ballSplit == 4 | ballSplit == 7:
            return 17
        else:
            return 0
    elif numberSplit == 8:
        if ballSplit == 5 | ballSplit == 6:
            return 17
        else:
            return 0
    elif numberSplit == 9:
        if ballSplit == 5 | ballSplit == 8:
            return 17
        else:
            return 0
    elif numberSplit == 10:
        if ballSplit == 6 | ballSplit == 9:
            return 17
        else:
            return 0
    elif numberSplit == 11:
        if ballSplit == 7 | ballSplit == 8:
            return 17
        else:
            return 0
    elif numberSplit == 12:
        if ballSplit == 7 | ballSplit == 10:
            return 17
        else:
            return 0
    elif numberSplit == 13:
        if ballSplit == 8 | ballSplit == 9:
            return 17
        else:
            return 0
    elif numberSplit == 14:
        if ballSplit == 8 | ballSplit == 11:
            return 17
        else:
            return 0
    elif numberSplit == 15:
        if ballSplit == 9 | ballSplit == 12:
            return 17
        else:
            return 0
    elif numberSplit == 16:
        if ballSplit == 10 | ballSplit == 11:
            return 17
        else:
            return 0
    elif numberSplit == 17:
        if ballSplit == 10 | ballSplit == 13:
            return 17
        else:
            return 0
    elif numberSplit == 18:
        if ballSplit == 11 | ballSplit == 12:
            return 17
        else:
            return 0
    elif numberSplit == 19:
        if ballSplit == 11 | ballSplit == 14:
            return 17
        else:
            return 0
    elif numberSplit == 20:
        if ballSplit == 12 | ballSplit == 15:
            return 17
        else:
            return 0
    elif numberSplit == 21:
        if ballSplit == 13 | ballSplit == 14:
            return 17
        else:
            return 0
    elif numberSplit == 22:
        if ballSplit == 13 | ballSplit == 16:
            return 17
        else:
            return 0
    elif numberSplit == 23:
        if ballSplit == 14 | ballSplit == 15:
            return 17
        else:
            return 0
    elif numberSplit == 24:
        if ballSplit == 14 | ballSplit == 17:
            return 17
        else:
            return 0
    elif numberSplit == 25:
        if ballSplit == 15 | ballSplit == 18:
            return 17
        else:
            return 0
    elif numberSplit == 26:
        if ballSplit == 16 | ballSplit == 17:
            return 17
        else:
            return 0
    elif numberSplit == 27:
        if ballSplit == 16 | ballSplit == 19:
            return 17
        else:
            return 0
    elif numberSplit == 28:
        if ballSplit == 17 | ballSplit == 18:
            return 17
        else:
            return 0
    elif numberSplit == 29:
        if ballSplit == 17 | ballSplit == 20:
            return 17
        else:
            return 0
    elif numberSplit == 30:
        if ballSplit == 18 | ballSplit == 21:
            return 17
        else:
            return 0
    elif numberSplit == 31:
        if ballSplit == 19 | ballSplit == 20:
            return 17
        else:
            return 0
    elif numberSplit == 32:
        if ballSplit == 19 | ballSplit == 22:
            return 17
        else:
            return 0
    elif numberSplit == 33:
        if ballSplit == 20 | ballSplit == 21:
            return 17
        else:
            return 0
    elif numberSplit == 34:
        if ballSplit == 20 | ballSplit == 23:
            return 17
        else:
            return 0
    elif numberSplit == 35:
        if ballSplit == 21 | ballSplit == 24:
            return 17
        else:
            return 0
    elif numberSplit == 36:
        if ballSplit == 22 | ballSplit == 23:
            return 17
        else:
            return 0
    elif numberSplit == 37:
        if ballSplit == 22 | ballSplit == 25:
            return 17
        else:
            return 0
    elif numberSplit == 38:
        if ballSplit == 23 | ballSplit == 24:
            return 17
        else:
            return 0
    elif numberSplit == 39:
        if ballSplit == 23 | ballSplit == 26:
            return 17
        else:
            return 0
    elif numberSplit == 40:
        if ballSplit == 24 | ballSplit == 27:
            return 17
        else:
            return 0
    elif numberSplit == 41:
        if ballSplit == 25 | ballSplit == 26:
            return 17
        else:
            return 0
    elif numberSplit == 42:
        if ballSplit == 25 | ballSplit == 28:
            return 17
        else:
            return 0
    elif numberSplit == 43:
        if ballSplit == 26 | ballSplit == 27:
            return 17
        else:
            return 0
    elif numberSplit == 44:
        if ballSplit == 26 | ballSplit == 29:
            return 17
        else:
            return 0
    elif numberSplit == 45:
        if ballSplit == 27 | ballSplit == 30:
            return 17
        else:
            return 0
    elif numberSplit == 46:
        if ballSplit == 28 | ballSplit == 29:
            return 17
        else:
            return 0
    elif numberSplit == 47:
        if ballSplit == 28 | ballSplit == 31:
            return 17
        else:
            return 0
    elif numberSplit == 48:
        if ballSplit == 29 | ballSplit == 30:
            return 17
        else:
            return 0
    elif numberSplit == 49:
        if ballSplit == 29 | ballSplit == 32:
            return 17
        else:
            return 0
    elif numberSplit == 50:
        if ballSplit == 30 | ballSplit == 33:
            return 17
        else:
            return 0
    elif numberSplit == 51:
        if ballSplit == 31 | ballSplit == 32:
            return 17
        else:
            return 0
    elif numberSplit == 52:
        if ballSplit == 31 | ballSplit == 34:
            return 17
        else:
            return 0
    elif numberSplit == 53:
        if ballSplit == 32 | ballSplit == 33:
            return 17
        else:
            return 0
    elif numberSplit == 54:
        if ballSplit == 32 | ballSplit == 35:
            return 17
        else:
            return 0
    elif numberSplit == 55:
        if ballSplit == 33 | ballSplit == 36:
            return 17
        else:
            return 0
    elif numberSplit == 56:
        if ballSplit == 34 | ballSplit == 35:
            return 17
        else:
            return 0
    elif numberSplit == 57:
        if ballSplit == 35 | ballSplit == 36:
            return 17
        else:
            return 0
    else:
        print "Error invalid choice"
# End of Split bet Function
#================================================================================================
#   Function Street handles street bets, Pays 11 to 1, returns 11 if hit 0 otherwise
def Street():
    print "Pick a Street:"
    print "1) 1,2,3:\t2) 4,5,6:\t3) 7,8,9:\t4) 10,11,12:"
    print "5) 13,14,15:\t6) 16,17,18:\t7) 19,20,21:\t8) 22,23,24:"
    print "9) 25,26,27:\t10) 28,29,30:\t11) 31,32,33:\t12) 34,35,36:"
    numberStreet = input()
#   Spins Roulette Wheel
    ballStreet = SpinWheel()
#   Checks Type of bet made by user and if they won
    if numberStreet == 1:
        if ballStreet == 1 or ballStreet == 2 or ballStreet == 3:
            return 11
        else:
            return 0
    elif numberStreet == 2:
        if ballStreet == 4 or ballStreet == 5 or ballStreet == 6:
            return 11
        else:
            return 0
    elif numberStreet == 3:
        if ballStreet == 7 or ballStreet == 8 or ballStreet == 9:
            return 11
        else:
            return 0
    elif numberStreet == 4:
        if ballStreet == 10 or ballStreet == 11 or ballStreet == 12:
            return 11
        else:
            return 0
    elif numberStreet == 5:
        if ballStreet == 13 or ballStreet == 14 or ballStreet == 15:
            return 11
        else:
            return 0
    elif numberStreet == 6:
        if ballStreet == 16 or ballStreet == 17 or ballStreet == 18:
            return 11
        else:
            return 0
    elif numberStreet == 7:
        if ballStreet == 19 or ballStreet == 20 or ballStreet == 21:
            return 11
        else:
            return 0
    elif numberStreet == 8:
        if ballStreet == 22 or ballStreet == 23 or ballStreet == 24:
            return 11
        else:
            return 0
    elif numberStreet == 9:
        if ballStreet == 25 or ballStreet == 26 or ballStreet == 27:
            return 11
        else:
            return 0
    elif numberStreet == 10:
        if ballStreet == 28 or ballStreet == 29 or ballStreet == 30:
            return 11
        else:
            return 0
    elif numberStreet == 11:
        if ballStreet == 31 or ballStreet == 32 or ballStreet == 33:
            return 11
        else:
            return 0
    elif numberStreet == 12:
        if ballStreet == 34 or ballStreet == 35 or ballStreet == 36:
            return 11
        else:
            return 0
    else:
        print "Error invalid choice"
# End of Street bet Function
#============================================================================================
#   Function Corner handles corner bets, Pays 8 to 1, returns 8 if hit 0 otherwise
def Corner():
    print "Pick a Corner:"
    print "1) 1,2,4,5:\t2) 2,3,5,6:\t3) 4,5,7,8:\t4) 5,6,8,9:"
    print "5) 7,8,10,11:\t6) 8,9,11,12:\t7) 10,11,13,14:\t8) 11,12,14,15:"
    print "9) 13,14,16,17:\t10) 14,15,17,18:\t11) 16,17,19,20:\t12) 17,18,20,21:"
    print "13) 19,20,22,23:\t14) 20,21,23,24\t15) 22,23,25,26:\t16) 23,24,26,27:"
    print "17) 25,26,28,29:\t18) 26,27,29,30\t19) 28,29,31,32:\t20) 29,30,32,33:"
    print "21) 31,32,34,35:\t22) 32,33,35,36:"
    numberCorner = input()
#   Spins Roulette Wheel
    ballCorner = SpinWheel()
#   Checks Type of bet made by user and if they won
    if numberCorner == 1:
        if ballCorner == 1 or ballCorner == 2 or ballCorner == 4 or ballCorner == 5:
            return 8
        else:
            return 0
    elif numberCorner == 2:
        if ballCorner == 2 or ballCorner == 3 or ballCorner == 5 or ballCorner == 6:
            return 8
        else:
            return 0
    elif numberCorner == 3:
        if ballCorner == 4 or ballCorner == 5 or ballCorner == 7 or ballCorner == 8:
            return 8
        else:
            return 0
    elif numberCorner == 4:
        if ballCorner == 5 or ballCorner == 6 or ballCorner == 8 or ballCorner == 9:
            return 8
        else:
            return 0
    elif numberCorner == 5:
        if ballCorner == 7 or ballCorner == 8 or ballCorner == 10 or ballCorner == 11:
            return 8
        else:
            return 0
    elif numberCorner == 6:
        if ballCorner == 8 or ballCorner == 9 or ballCorner == 11 or ballCorner == 12:
            return 8
        else:
            return 0
    elif numberCorner == 7:
        if ballCorner == 10 or ballCorner == 11 or ballCorner == 13 or ballCorner == 14:
            return 8
        else:
            return 0
    elif numberCorner == 8:
        if ballCorner == 11 or ballCorner == 12 or ballCorner == 14 or ballCorner == 15:
            return 8
        else:
            return 0
    elif numberCorner == 9:
        if ballCorner == 13 or ballCorner == 14 or ballCorner == 16 or ballCorner == 17:
            return 8
        else:
            return 0
    elif numberCorner == 10:
        if ballCorner == 14 or ballCorner == 15 or ballCorner == 17 or ballCorner == 18:
            return 8
        else:
            return 0
    elif numberCorner == 11:
        if ballCorner == 16 or ballCorner == 17 or ballCorner == 19 or ballCorner == 20:
            return 8
        else:
            return 0
    elif numberCorner == 12:
        if ballCorner == 17 or ballCorner == 18 or ballCorner == 20 or ballCorner == 21:
            return 8
        else:
            return 0
    elif numberCorner == 13:
        if ballCorner == 19 or ballCorner == 20 or ballCorner == 22 or ballCorner == 23:
            return 8
        else:
            return 0
    elif numberCorner == 14:
        if ballCorner == 20 or ballCorner == 21 or ballCorner == 23 or ballCorner == 24:
            return 8
        else:
            return 0
    elif numberCorner == 15:
        if ballCorner == 22 or ballCorner == 23 or ballCorner == 25 or ballCorner == 26:
            return 8
        else:
            return 0
    elif numberCorner == 16:
        if ballCorner == 23 or ballCorner == 24 or ballCorner == 26 or ballCorner == 27:
            return 8
        else:
            return 0
    elif numberCorner == 17:
        if ballCorner == 25 or ballCorner == 26 or ballCorner == 28 or ballCorner == 29:
            return 8
        else:
            return 0
    elif numberCorner == 18:
        if ballCorner == 26 or ballCorner == 27 or ballCorner == 29 or ballCorner == 30:
            return 8
        else:
            return 0
    elif numberCorner == 19:
        if ballCorner == 28 or ballCorner == 29 or ballCorner == 31 or ballCorner == 32:
            return 8
        else:
            return 0
    elif numberCorner == 20:
        if ballCorner == 29 or ballCorner == 30 or ballCorner == 32 or ballCorner == 33:
            return 8
        else:
            return 0
    elif numberCorner == 21:
        if ballCorner == 31 or ballCorner == 32 or ballCorner == 34 or ballCorner == 35:
            return 8
        else:
            return 0
    elif numberCorner == 22:
        if ballCorner == 32 or ballCorner == 33 or ballCorner == 35 or ballCorner == 36:
            return 8
        else:
            return 0
    else:
        print "Error invalid choice"
#   End of Corner Function
#==================================================================================================
#   Function SixLine handles Six line bets, Pays 5 to 1, returns 5 if hit and 0 otherwise
def SixLine():
    print "Pick a Six Line bet:"
    print "1) 1,2,3,4,5,6:\t2) 4,5,6,7,8,9\t3)7,8,9,10,11,12:\t4) 10,11,12,13,14,15:"
    print "5) 13,14,15,16,17,18:\t6) 16,17,18,19,20,21:\t7) 19,20,21,22,23,24:\t8) 22,23,24,25,26,27:"
    print "9) 25,26,27,28,29,30:\t10) 28,29,30,31,32,33:\t 11) 31,32,33,34,35,36:"
    numberSixLine = input()
#   Spins Roulette Wheel
    ballSixLine = SpinWheel()
#   Checks Type of bet made by user and if they won
    if numberSixLine == 1:
        for choice1 in range(1,7):
            if choice1 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 2:
        for choice2 in range(4,10):
            if choice2 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 3:
        for choice3 in range(7,13):
            if choice3 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 4:
        for choice4 in range(10,16):
            if choice4 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 5:
        for choice5 in range(13,19):
            if choice5 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 6:
        for choice6 in range(16,22):
            if choice6 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 7:
        for choice7 in range(19,25):
            if choice7 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 8:
        for choice8 in range(22,28):
            if choice8 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 9:
        for choice9 in range(25,31):
            if choice9 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 10:
        for choice10 in range(28,34):
            if choice10 == ballSixLine:
                return 5
        return 0
    elif numberSixLine == 11:
        for choice11 in range(31,37):
            if choice11 == ballSixLine:
                return 5
        return 0
    else:
        print "Invalid Choice"
# End of Six Line bet Function
#===================================================================================================
#   Function Color, handles color bets, Pays 1 to 1, returns 1 if hits 0 otherwise
def Color():
    print "Pick a color:\n1) Red:\n2) Black:"
    numberColor = input()
#   Spins Roulette Wheel
    ballColor = SpinWheel()
#   Checks Type of bet made by user and if they won
    if numberColor == 1:
        arrayRed = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        for red in arrayRed:
            if red == ballColor:
                return 1
        return 0
    elif numberColor == 2:
        arrayBlack = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        for black in arrayBlack:
            if black == ballColor:
                return 1
        return 0
    else:
        print "Invalid Option"
# end of Color bet Function
#=======================================================================================================
#   Function EvenOrOdd handles Even and Odd bets, Pays 1 to 1, returns 1 if it hits 0 otherwise
def EvenOrOdd():
    print "1) Even:\t2) Odd:"
    numberEvenOrOdd = input()
#   Spins Roulette Wheel
    ballEvenOrOdd = SpinWheel()
#   Checks to see if ball lands on zero, returns 0 if it does since 0 isn't even or odd
    if ballEvenOrOdd == 0:
        return 0
#   Checks Type of bet made by user and if they won
    if numberEvenOrOdd == 1:
        if ballEvenOrOdd % 2 == 0:
            return 1
        else:
            return 0
    elif numberEvenOrOdd == 2:
        if ballEvenOrOdd % 2 == 1:
            return 1
        else:
            return 0
# end of Even or Odd Function
#==============================================================================================================
#   Function HighOrLow handles High and Low bets, Pays 1 to 1, returns 1 if it hits 0 otherwise
def HighOrLow():
    print "Pick High (1-18) or Low (19-36):"
    print "1) High:\t2) Low:"
    numberHighOrLow = input()
#   Spins Roulette Wheel
    ballHighOrLow = SpinWheel()
#   Checks to see if ball lands on zero, returns 0 if it does since 0 isn't a part of high or low grouping
    if ballHighOrLow == 0:
        return 0
#   Checks Type of bet made by user and if they won
    if numberHighOrLow == 1:
        if ballHighOrLow > 18:
            return 1
        else:
            return 0
    elif numberHighOrLow == 2:
        if ballHighOrLow < 19 and ballHighOrLow > 0:
            return 1
        else:
            return 0
    else:
        print "Error Invalid Option"
# end of High or Low Function
#==================================================================================================================
#   Function Dozen handles dozen bets, Pays 2 to 1, returns 2 if it hits and 0 otherwise
def Dozen():
    print "Pick your Dozen:"
    print "1) (1-12):\t2) (13-24):\t3) (24-36):"
    numberDozen = input()
#   Spins Roulette Wheel
    ballDozen = SpinWheel()
#   Checks to see if ball lands on zero, returns 0 if it does since 0 isn't a part of any dozen
    if ballDozen == 0:
        return 0
#   Checks Type of bet made by user and if they won
    if numberDozen == 1:
        for firstDozen in range(1,13):
            if firstDozen == ballDozen:
                return 2
        return 0
    elif numberDozen == 2:
        for secondDozen in range(13,25):
            if secondDozen == ballDozen:
                return 2
        return 0
    elif numberDozen == 3:
        for thirdDozen in range(25,37):
            if thirdDozen == ballDozen:
                return 2
        return 0
    else:
        print "Error Invalid Choice"
#   End of Dozen Function
#==========================================================================================================
#   Function AdjacentDozen handles adjacent dozen bets, Pays 1 to 1, returns 1 if it hits 0 otherwise
def AdjacentDozen():
    print "Pick your Adjacent Dozen:"
    print "1) (1-24):\t2) (13-36):"
    numberAdjacentDozen = input()
#   Spins Roulette Wheel
    ballAdjacentDozen = SpinWheel()
#   Checks to see if ball lands on zero, returns 0 if it does since 0 isn't a part of any adjacent dozen
    if ballAdjacentDozen == 0:
        return 0
#   Checks Type of bet made by user and if they won
    if numberAdjacentDozen == 1:
        for firstAdjacentDozen in range(1,25):
            if firstAdjacentDozen == ballAdjacentDozen:
                return 1
        return 0
    elif numberAdjacentDozen == 2:
        for secondAdjacentDozen in range(13,37):
            if secondAdjacentDozen == ballAdjacentDozen:
                return 1
        return 0
    else:
        print "Error Invalid Choice"
#   end of Adjacent Dozen Function
#==========================================================================================================
#   Function Column handles column bets, Pays 2 to 1, returns 2 if it hits 0 otherwise
def Column():
    print "Pick your Column:"
    print "1) 1st Column (1,4,7,10,13,16,19,22,25,28,31,34):"
    print "2) 2nd Column (2,5,8,11,14,17,20,23,26,29,32,35):"
    print "3) 3rd Column (3,6,9,12,15,18,21,24,27,30,33,36):"
    numberColumn = input()
#   Spins Roulette Wheel
    ballColumn = SpinWheel()
#   Checks to see if ball lands on zero, returns 0 if it does since 0 isn't a part of any column
    if ballColumn == 0:
        return 0
#   Checks Type of bet made by user and if they won
    if numberColumn == 1:
        arrayColumn1 = [1,4,7,10,13,16,19,22,25,28,31,34]
        for columnOne in arrayColumn1:
            if columnOne == ballColumn:
                return 2
        return 0
    elif numberColumn == 2:
        arrayColumn2 = [2,5,8,11,14,17,20,23,26,29,32,35]
        for columnTwo in arrayColumn2:
            if columnTwo == ballColumn:
                return 2
        return 0
    elif numberColumn == 3:
        arrayColumn3 = [3,6,9,12,15,18,21,24,27,30,33,36]
        for columnThree in arrayColumn3:
            if columnThree == ballColumn:
                return 2
        return 0
    else:
        print "Error Invalid Choice"
#   End of Column Function
#=========================================================================================================
#   Function AdjacentColumn handles adjacent column bets, Pays 1 to 1, returns 1 if it hits 0 otherwise
def AdjacentColumn():
    print "Pick your Adjacent Column:"
    print "1) Column 1 and Column 2 (1,4,7,10,13,16,19,22,25,28,31,34)&(2,5,8,11,14,17,20,23,26,29,32,35)"
    print "2) Column 2 and Column 3 (2,5,8,11,14,17,20,23,26,29,32,35)&(3,6,9,12,15,18,21,24,27,30,33,36)"
    numberAdjacentColumn = input()
#   Spins Roulette Wheel
    ballAdjacentColumn = SpinWheel()
#   Checks to see if ball lands on zero, returns 0 if it does since 0 isn't a part of any adjacent column
    if ballAdjacentColumn == 0:
        return 0
#   Checks Type of bet made by user and if they won
    if numberAdjacentColumn == 1:
        arrayColumnOneAndTwo = [1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29,31,32,34,35]
        for columnOneAndTwo in arrayColumnOneAndTwo:
            if columnOneAndTwo == ballAdjacentColumn:
                return 1
        return 0
    elif numberAdjacentColumn == 2:
        arrayColumnTwoAndThree = [2,3,5,6,8,9,11,12,14,15,17,18,20,21,23,24,26,27,29,30,32,33,35,36]
        for columnTwoAndThree in arrayColumnTwoAndThree:
            if columnTwoAndThree == ballAdjacentColumn:
                return 1
        return 0
    else:
        print "Error Invalid Choice"
#   End of Adjacent Column Function
#==============================================================================================================
#   Prompts user for betting amount
print"Lets Play Roulette:\nHow much would you like to bet (Whole Dollars):"
bet = input()
#   Prompts user for type of bet, Roulette has inside and outside bets
print "What type of bet would you like to make:\nI)nside bet:\nO)utSide bet:"
betType = raw_input()
#   Checks for type of bet being made, Inside or Outside
if betType.upper() == 'I':
    print "What type of inside bet would you like to make:"
    #   Types of inside bets
    print "1)Straight up bet:\n2)Split bet:\n3)Street bet\n4)Corner bet\n5)Six line bet:"
    insideBetType = input()
    #   Checks to see what type of inside bet is being made by user
    if insideBetType == 1:
        print "Straight Up:"
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeStraight = bet * StraightUp()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeStraight == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeStraight
    elif insideBetType == 2:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeSplit = bet * Split()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeSplit == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeSplit
    elif insideBetType == 3:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeStreet = bet * Street()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeStreet == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeStreet
    elif insideBetType == 4:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeCorner = bet * Corner()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeCorner == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeCorner
    elif insideBetType == 5:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeSixLine = bet * SixLine()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeSixLine == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeSixLine
    else:
        print "Error not a valid selection"
# End of Inside Bet Options
elif betType.upper() == 'O':
    print "What type of outside bet would you like to make:"
    #   Types of outside bets possible
    print "1)Color bet:\n2)Even or odd bet:\n3)High or low bet:\n4)Dozen bet:\n5)Adjacent dozen bet:\n6)Column bet:"
    print "7)Adjacent column bet:"
    outsideBetType = input();
    #   Checks to see what Type of outside bet is being made by user
    if outsideBetType == 1:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeColor = bet * Color()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeColor == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeColor
    elif outsideBetType == 2:
        print "Even/Odd"
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeEvenOrOdd = bet * EvenOrOdd()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeEvenOrOdd == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeEvenOrOdd
    elif outsideBetType == 3:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeHighOrLow = bet * HighOrLow()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeHighOrLow == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeHighOrLow
    elif outsideBetType == 4:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeDozen = bet * Dozen()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeDozen == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeDozen
    elif outsideBetType == 5:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeAdjacentDozen = bet * AdjacentDozen()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeAdjacentDozen == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeAdjacentDozen
    elif outsideBetType == 6:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeColumn = bet * Column()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeColumn == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeColumn
    elif outsideBetType == 7:
        #   Calculates outcome of bet, function call will return 0 or an int
        outComeAdjacentColumn = bet * AdjacentColumn()
        #   Checks to see if user lost or won bet, if user won displays amount won
        if outComeAdjacentColumn == 0:
            print "You lose, Sorry."
        else:
            print "You Win: "
            print outComeAdjacentColumn
    else:
        print "Error not a valid selection"
else:
    print "Error selection not valid"

