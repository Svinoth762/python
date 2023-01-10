#PROGRAM TO FIND A HAPPY NUMBER
def is_happy_number(n):
  past=set()
  while n!=1:
        n=sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
print(is_happy_number(5))
print(is_happy_number(9))
print(is_happy_number(19))
