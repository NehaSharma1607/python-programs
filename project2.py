# if given no is 659 then the output should be 2.
# i.e., 6+5+9=20 and 2+0=2.
# the prohram should keep adding nos till only single digit is left.

class projectTwo:

    def sum(self):
        if self == 0:
            return 0
        elif self % 9 == 0:
            return 9
        else:
            return self % 9


p2 = projectTwo()
print(p2.sum(34534))
