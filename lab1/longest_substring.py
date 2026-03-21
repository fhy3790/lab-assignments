def lengthOfLongestSubstring(s):
    # 方法：滑动窗口 + 集合
    # Метод: скользящее окно + множество
    # 时间复杂度 / Сложность: O(n)

    seen = set()   # 当前窗口中的字符 / Символы текущего окна
    left = 0       # 左边界 / Левая граница
    max_len = 0    # 最大长度 / Максимальная длина

    for right in range(len(s)):
        # 如果当前字符重复，就缩小窗口
        # Если текущий символ повторяется, сужаем окно
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # 把当前字符加入窗口
        # Добавляем текущий символ в окно
        seen.add(s[right])

        # 更新最大长度
        # Обновляем максимальную длину
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))

#Я использовал метод скользящего окна.
# left и right задают границы текущей подстроки, а множество seen хранит символы внутри окна.
# Если текущий символ уже есть в окне, я сдвигаю левую границу и удаляю символы слева, пока дубликат не исчезнет.
# После этого обновляю максимальную длину.Сложность алгоритма — O(n).

#我用了滑动窗口。left 和 right 表示当前子串的左右边界，集合 seen 保存窗口中的字符。
# 右指针向右移动时，如果当前字符重复，就移动左指针并删除左边字符，直到窗口中没有重复字符。
# 然后更新最大长度。时间复杂度是 O(n)。