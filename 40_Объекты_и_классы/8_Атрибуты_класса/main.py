class Comment:
    total_comments = 0  # Атрибут класса

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1


# При создании экземпляра класса, значение атрибут класса изменяется
first_comment = Comment("First comment")
print(Comment.total_comments)   # 1

second_comment = Comment("Scond comment")
print(Comment.total_comments)   # 2


# Атрибут класса не является собственным атрибутом экземплярова класса
print(first_comment.__dict__)   # {'text': 'First comment', 'votes_qty': 0}


# Атрибуты класса унаследуются экземплярами классов
print(first_comment.total_comments)  # 2


# Нельзя из экземпляра класса изменить значение атрибута класса
first_comment.total_comments = 10
print(first_comment.__dict__)
# {'text': 'First comment', 'votes_qty': 0, 'total_comments': 10}}
# Мы просто создали собственный атрибут для экземпляра класса

print(Comment.total_comments)   # 2
print(first_comment.total_comments)  # 10

# Изменять атрибут класса можно только на уровне класса
Comment.total_comments = 20
print(Comment.total_comments)   # 20
print(first_comment.total_comments)  # 20
