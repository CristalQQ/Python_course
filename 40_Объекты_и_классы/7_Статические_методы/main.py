# Статический метод - это метод, который связан с классом, а не с его экземплярами. Он не имеет доступа к атрибутам экземпляра или к самому экземпляру (через параметр self), и он не требует создания экземпляра класса для вызова.
# Для определения статического метода в классе используется декоратор @staticmethod.

class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"


my_comment = Comment("My comment")

# Статические методы доступны как атирибуты класса и как атирибуты экземпляра класса
m_1 = Comment.merge_comments("Thanks!", "Excellent.")
print(m_1)  # Thanks! Excellent.

# Статические методы доступны как атирибуты экземпляра класса
m_2 = my_comment.merge_comments("Greeat", "OK")
print(m_2)  # Greeat OK
