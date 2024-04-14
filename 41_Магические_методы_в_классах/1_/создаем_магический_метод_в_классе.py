class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    # Создаем магический метод __add__(сложение) для класса
    def __add__(self, other):
        return (f"{self.text} {other.text}",
                self.votes_qty + other.votes_qty)

    # Создаем магический метод __eq__(сравнение) для класса
    def __eq__(self, other):
        return bool(self.text == other.text and self.votes_qty == other.votes_qty)


first_comment = Comment("First comment")
first_comment.upvote()

second_comment = Comment("Second comment")
second_comment.upvote()


print(first_comment + second_comment)   # ('First comment Secodnd comment', 2)

print(first_comment == second_comment)  # False

# У класса object нет магического метода __add__ и он не наследуется подклассом Comment
print('Comment: ', dir(Comment))
print('')
# У класса object есть магический метод __eq__ и он наследуется подклассом Comment
print('object: ', dir(object))
