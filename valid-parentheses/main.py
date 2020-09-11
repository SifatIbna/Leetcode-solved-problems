class Solution:
    def isValid(self, s: str) -> bool:

        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        bracket_map = {"(": ")", "[": "]", "{": "}"}

        stack = []

        for val in s:

            if val in closing:

                # print('first'+val and brackets[len(brackets)-1] in first)
                # print('second'+val and brackets[len(brackets)-1] in second)
                # print('third'+val and brackets[len(brackets)-1] in third)

                if stack and val == bracket_map[stack[-1]]:
                    stack.pop()
                else:
                    return False

            elif val in opening:
                stack.append(val)

        return len(stack) == 0
