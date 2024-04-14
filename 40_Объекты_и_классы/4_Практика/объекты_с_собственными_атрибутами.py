class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0


# Создание экземпляра класса Comment
my_comment = Comment("First comment")


# Собственные атрибуты экземпляра
print(my_comment.votes_qty)  # 0


# Добавляем значение атрибуту votes_qty с помощью метода upvote()
my_comment.upvote(10)
print(my_comment.votes_qty)  # 10

# Обнуляем атрибут votes_qty с помощью метода reset_votes_qty()
my_comment.reset_votes_qty()
print(my_comment.votes_qty)  # 0
