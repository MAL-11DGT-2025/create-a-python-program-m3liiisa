book = input('What is the first book of the bible? ?\na) Genesis\nb) Exodus\nc) Numbers\nd) Leviticus\n>>')
correct = ['a', 'a)', 'Genesis', 'genesis', 'a) genesis']
incorrect = ['b', 'b)', 'exodus', 'b) exodus', 'c', 'c)', 'numbers', 'c)numbers', 'd', 'd)', 'leviticus', 'd) leviticus' ]

if book.lower().strip() in correct:
    print('That is correct')
elif book.lower().strip() in incorrect:
    print('That is incorrect')
else:
    print('Invalid')

