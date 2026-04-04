class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # 用栈存数字 / Используем стек для хранения чисел

        for token in tokens:  # 遍历每个元素 / Проходим по каждому элементу
            if token in {"+", "-", "*", "/"}:  # 如果当前是运算符 / Если текущий элемент — оператор
                b = stack.pop()  # 先弹出第二个操作数 / Сначала извлекаем второй операнд
                a = stack.pop()  # 再弹出第一个操作数 / Затем извлекаем первый операнд

                if token == "+":
                    stack.append(a + b)  # 加法 / Сложение
                elif token == "-":
                    stack.append(a - b)  # 减法 / Вычитание
                elif token == "*":
                    stack.append(a * b)  # 乘法 / Умножение
                else:
                    stack.append(int(a / b))  # 除法，向 0 截断 / Деление с усечением к нулю
            else:
                stack.append(int(token))  # 如果是数字就入栈 / Если число, кладём его в стек

        return stack[-1]  # 栈顶就是最终结果 / Верхний элемент стека — итоговый ответ