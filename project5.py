#Binary Search Algorithm
#Create a random list of numbers between 0 and 100 with a difference of 2 between each number. Ask the user for a number between 0 and 100 to check whether their number is in the list. The programme should work like this. The programme will half the list of numbers and see whether the users number matches the middle element in the list. If they do not match, the programme will check which half the number lies in, and eliminate the other half. The search then continues on the remaining half, again checking whether the middle element in that half is equal to the user’s number. This process keeps on going until the programme finds the users number, or until the size of the subarray is 0, which means the users number isn't in the list.
#
#If you are struggling with any of these, then feel free to message me, or just have a look online as there are plenty of solutions available on platforms such as youtube

#https://note.nkmk.me/en/python-random-shuffle/
import random
numbers = list(range(0,100,2))
print (numbers)

#xao tron numbers
random.shuffle(numbers)

print(numbers)

