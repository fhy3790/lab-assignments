class Solution(object):
    def generateParenthesis(self, n):
        res = []  # 存放所有合法结果 / Храним все правильные комбинации

        def backtrack(cur, left, right):
            # cur: 当前括号字符串 / Текущая строка
            # left: 已经放了几个左括号 / Сколько '(' уже использовано
            # right: 已经放了几个右括号 / Сколько ')' уже использовано

            # 如果当前字符串长度等于 2*n，说明是一组完整答案
            # Если длина строки равна 2*n, значит получили готовый ответ
            if len(cur) == 2 * n:
                res.append(cur)
                return

            # 只要左括号数量还没到 n，就可以继续放左括号
            # Пока left < n, можно добавить '('
            if left < n:
                backtrack(cur + "(", left + 1, right)

            # 右括号只有在数量少于左括号时才能放
            # ')' можно добавить только если right < left
            if right < left:
                backtrack(cur + ")", left, right + 1)

        backtrack("", 0, 0)
        return res