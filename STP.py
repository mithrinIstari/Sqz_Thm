#Squeeze Theorem#

import turtle
import math
import matplotlib.pyplot as plt
import numpy as np
from colorama import init, Fore, Back

def main():
    init()
    print("Hello!")
    answ = str(input("Do you want to learn about the Squeeze Theorem? Type 'yes' to continue: "))
    if answ.lower() == 'yes':
        squeeze()
        
    else:
        print("Goodbye.")
        return

def squeeze(): #beginning fx introduce idea
    sq1 = "The Squeeze Theorem can help find difficult limits."
    sq2 = "Suppose you are asked to find the following limit: "
    sq3 = "lim x -> 0 for g(x) = x * sin(1/x)"
    sq4 = "You might recall a useful multiplication rule for this limit."
    sq5 = "To use this rule, each limit must exist."

    print(Fore.CYAN + '\n' + sq1 + '\n' + '\n' + Back.WHITE + sq2 + Back.RESET + '\n' + '\n' + sq3 + '\n' + '\n' + sq4 + '\n' + sq5 + '\n')

    while(True):
        wake1 = str(input(Fore.WHITE + "Does lim x -> 0 of x and lim x -> 0 of sin(1/x) exist? Type 'yes', 'no', or '?': " ))
        if wake1.lower() == "yes":
            print(Fore.RED + '\n' + "Incorrect." + '\n')
            break
        elif wake1.lower() == "no":
            print(Fore.RED + '\n' + "Correct." + '\n')
            break
        elif wake1.lower() == "?":
            print(Fore.RED + '\n' + "Let's see..." + '\n')
            break
        else:
            print(Fore.WHITE + '\n' + "Invalid answer." + '\n')
            continue
    limSin()
        
# limit of sin(1/x) #
def limSin():
    entstr = "Press 'enter' to view the graph of g(x) = sin(1/x)."
    entstr1 = "Use the graph to find the limit of g(x)."
    entstr2 = "After viewing the graph, close the window to continue"
    ls1 = "We see that the limit of x -> 0 for sin(1/x) does not exist." + '\n'+ "The values of sin(1/x) oscillate between 1 and -1 infinitely often as x approaches 0."
    ls2 = "So, we can't use the multiplication rule for this limit."

    input(Fore.WHITE + entstr + '\n')
    print('\n' + Back.WHITE + entstr1 + Back.RESET)
    print(Fore.YELLOW + '\n' + ls1 + '\n')
    print('\n' + Fore.WHITE + entstr2 + '\n')
    
    x = np.linspace(-np.pi, np.pi, 500)   # sets up 500 points, between pi and -pi
    y = np.sin((1/x))      # the function to graph

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    ax1.spines['left'].set_position('center')
    ax1.spines['bottom'].set_position('center')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    plt.plot(x, y, 'b-', label = " g(x) = sin(1/x) ")   #plots w/ label
    plt.legend(loc = "upper left")

    plt.show()  #displays 
    input('\n' + Fore.WHITE + "Press 'enter' to continue. ")
    print('\n' + Fore.GREEN + ls2 + '\n')    
    whatIsSqueeze()
    
# Squeeze Theorem def'n & graph of 3 fx
def whatIsSqueeze():
    w1 = "How can the Squeeze Theorem help us with this?"
    w2 = "The Squeeze Theorem: "
    w3 = "If f(x) <= g(x) <= h(x) for all x in an open interval that contains a (except possibilty at a)"
    w4 = "and the lim x -> a of f(x) = L = lim x -> a of h(x), then,"
    w5 = "the limit of x -> a of g(x) = L"
    w6 = "In other words, if you have two functions with the same limit, "
    w7 = "the function in the middle will also have the same limit."
    w8 = "Examine the graph of g(x) = x * sin(1/x) "
    w9 = "From the graph, we see that the lim x -> 0 of g(x) = x * sin(1/x) is unclear. " + '\n'
    w10 = "However, if we can find functions, f(x) and h(x), such that, f(x) <= g(x) <= h(x), and f(x) and h(x) = L, "
    w11 = "we can apply the Squeeze Theorem to find the limit of g(x)"
    s1 = "Consider, -1 <= sin (1/x) <= 1"
    s2 = "we saw this earlier from the graph of g(x) = sin(1/x))."
    s3 = "So, we can multiply this inequality by |x| to get:"
    s4 = " -|x| <= x * sin(1/x) <= |x|. Let's see f(x), g(x), and h(x)."
    s5 = "Press 'enter' to see the graphs of: "
    s6 = "f(x) = -|x|" + '\n' + "g(x) = x * sin(1/x)"
    s7 = "h(x) = |x|"
    s8 = "We can see from the graph that -|x| and |x| appear to 'squeeze' x * sin(1/x)."
    s9 = "Look at the graph and find the limits x -> 0 of -|x| and |x|"
    s10 = "Close the graph window after viewing to continue"

    print(Fore.CYAN + w1 )
    print(Fore.BLUE + '\n' + Back.YELLOW + w2 + '\n' + '\n' + w3 + '\n' + w4 + '\n' + w5 + '\n' + Back.RESET )
    print('\n' + Fore.MAGENTA + w6 + '\n' + w7 + '\n' + '\n') 
    print(Fore.RED + Back.WHITE + w8 + Back.RESET + '\n')
    input(Fore.WHITE + "Press 'enter' to view the graph of x * sin(1/x)" + '\n') 
    print(Fore.GREEN + '\n' + w9 + '\n' + w10 + '\n' + w11 + '\n')
    print('\n' + Fore.WHITE + "After viewing the graph, close the window to continue.")

    #graph f(x) for the function we need to find the limit for
    x = np.linspace(-np.pi/6, np.pi/6, 500)
    y = (x * np.sin(1/x))

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    
    ax2.spines['left'].set_position('zero')
    ax2.spines['bottom'].set_position('zero')
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.xaxis.set_ticks_position('bottom')
    ax2.yaxis.set_ticks_position('left') 

    plt.plot(x, y, 'b-', label = "f(x) = x * sin(1/x)") #plots w/ label
    plt.legend(loc = "upper left")
    plt.show() # shows graph

    print(Back.RESET)
    input(Fore.WHITE + "Press 'enter' to continue: ")
    print(Fore.CYAN + s1 + '\n' + '\n' + s2 + '\n')
    print(Fore.BLUE + s3 + '\n' + s4 + '\n')
    input(Fore.WHITE + s5 + '\n' + s6 + '\n' + s7 + '\n')
    print( '\n' + '\n' + Back.WHITE + Fore.RED + s9 + Back.RESET + '\n' + '\n' + s8 + Fore.MAGENTA + '\n' + Fore.WHITE + '\n' + s10)

    graphThree()

def graphThree():
    g1 = "The limit of x -> 0 of -|x| and |x| = 0."
    g2 = "x * sin(1/x) is between them,"
    g3 = "So, what is the limit of x -> 0 of x * sin(1/x)? "
    
    x = np.linspace(-np.pi/6, np.pi/6, 500)
    p = (x * np.sin(1/x))
    q = abs(x)
    r = - abs(x)

    fig3 = plt.figure()
    ax3 = fig3.add_subplot(1, 1, 1)
    ax3.spines['left'].set_position('zero')
    ax3.spines['bottom'].set_position('zero')
    ax3.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')
    ax3.xaxis.set_ticks_position('bottom')
    ax3.yaxis.set_ticks_position('left')
    ax3.set_ylim(-0.25, 0.25)

    plt.plot(x, p, 'b-', label = 'f(x) = -|x|')
    plt.plot(x, q, 'c-', label = 'g(x) = x * sin(1/x)')
    plt.plot(x, r, 'm-', label = 'h(x) = |x|')

    plt.legend(loc = "upper left")
    plt.show()
    
    Fore.WHITE
    
    ques = input(Fore.GREEN + '\n' + g1 + '\n'  + g2 + '\n' + '\n' + Fore.WHITE + g3 + '\n')
    # insert numeric test here # 
    while ques.isdigit() == True:
        if ques == "0":
            print('\n' + Fore.YELLOW + "That's correct!")
            print('\n' + 'Now you know what the Squeeze Theorem is!')
            return
        else:
            print('\n' + Fore.YELLOW + "Try again.")
            print('\n' + Fore.GREEN + g1 + '\n' + g2 + '\n')
            ques = input(Fore.WHITE + g3)
            continue
    while ques.isdigit() == False:
        ques = (Fore.WHITE + "Invalid answer. Please enter a number.")
    

main()
