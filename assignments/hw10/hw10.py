
from face import Face
from graphics import Point, GraphWin

def fibonacci(num):
    a_start = 0
    b_end = 1
    if num == 0:
        return 0
    elif num == 1:
        return b_end
    else:
        index = 1
        while index != num:
            check = a_start + b_end
            a_start = b_end
            b_end = check
            index += 1
        return b_end

def double_investment(prin, rate):
    years = 0
    total = prin
    while total <= prin * 2:
        total += (total * (rate))
        years += 1
    return years



def syracuse(nums):
    list = [nums]
    while nums != 1:
        if nums % 2 == 0:
            nums = nums / 2
            list.append(int(nums))
        else:
            nums = 3 * (nums) + 1
            list.append(int(nums))
    return list


def get_all_primes(n):
    num = 1
    prime_list = []
    while num <= n:
        count = 0
        i = 2
        while i <= num // 2:
            if num % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and num != 1:
            prime_list.append(int("%d" % num))
        num = num + 1
    return prime_list

def goldbach(num):
    primes = get_all_primes(num)  # returns all prime numbers
    i,j = 0,0
    poss_1 = primes[i]
    poss_2 = primes[j]
    two_primes = []

    while poss_1 + poss_2 != num:
        if poss_2 == primes[-1]:
            i = j = i + 1
            poss_2 = primes[i]
            poss_1 = primes[i]
        else:
            j += 1
            poss_2 = primes[j]
    two_primes.append(poss_1)
    two_primes.append(poss_2)
    return two_primes




#commands for the face class
win = GraphWin('Face',500,500)

f = Face(win, Point(250,250), 100)
f.smile()
#f.wink()
#f.shock()
#win.getMouse()
