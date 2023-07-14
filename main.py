class Even_numbers:
    def if_even(self, array, l, r):
        """Creating a empty array with zeros"""
        even_array = [0] * len(array)
        even_array[0] = (1 if array[0] % 2 == 0 else 0)

        """ increase 1 eveytime the interation got even number
            note the last element of new array has the total number of even number in array"""

        for i in range(1, len(array)):
            even_array[i] = even_array[i-1] + (1 if array[i] % 2 == 0 else 0)

        if l == 0:
            return even_array[r]
        return even_array[r] - even_array[l-1]

        """ return 0 if l starts with 0
            return last element - the range's first element --- hence we get the no of even elements in that range"""



array = list(map(int, input("enter array elements: ").split()))
q = int(input("enter number of query: "))
object = Even_numbers()

for i in range(q):
    l, r = map(int, input("enter l and r: ").split())

    print(object.if_even(array, l, r))












