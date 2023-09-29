import re


def main():
    while True:
        # Prompt.
        expression = input("Digite a expressão: ")
        postfix = Postfix(expression)
        # Breaks the program if 'fim' is input.
        if expression == "fim":
            break
        # Executes the code.
        postfix.print()


# Helper function: check if a string is a valid float.
def is_float(string):
    try:
        float(string)
        result = True
    except ValueError:
        result = False
    return result


# Postfix expression converter class.
class Postfix:
    def __init__(self, raw):
        self.raw = raw

    # Transforms a raw string in a array of mathematical operators and operands.
    def get_parsed(self):
        # Partial operators and operands regEx.
        parsed = re.findall(r"(\b\d*[\.]?\d+\b|[\(\)\+\*\-\/\%])", self.raw)
        parsed_too = []
        # Final parsing logic.
        for i, value in enumerate(parsed):
            # Basic index predicates.
            last_i = i - 1
            not_first_i = i != 0
            not_second_i = i != 1
            last_valid_i = max(last_i, 0)
            # Logic to find last non parentesis value.
            if not_first_i:
                while parsed[last_valid_i] in ["(", ")"]:
                    if last_valid_i - 1 < 0:
                        break
                    last_valid_i -= 1
            # Basic unary check predicate.
            is_unary = value in ["+", "-"]
            # Number check predicate.
            is_last_float = is_float(parsed[last_valid_i])
            # Unary negative check predicates.
            is_last_unary_negative = not_first_i and parsed_too[-1] == "n"
            is_second_last_unary_negative = not_first_i and not_second_i and parsed_too[-2] == "n"
            # Exponential check predicate.
            is_second_last_exponential = not_first_i and not_second_i and parsed_too[-2] == "**"
            # Exponential from asterisk predicates.
            is_asterisk = value == "*"
            is_last_asterisk = parsed[last_i] == "*"
            # Integer division from forward slash predicates.
            is_fslash = value == "/"
            is_last_fslash = parsed[last_i] == "/"

            # Parsing special characters.
            if is_unary and not is_last_float:
                match value:
                    case "+":
                        parsed_too.append("p")
                    case "-":
                        parsed_too.append("n")
            elif is_asterisk and not_first_i and is_last_asterisk:
                parsed_too[-1] = "**"
            elif is_fslash and not_first_i and is_last_fslash:
                parsed_too[-1] = "//"
            # Dealing with negative exponents.
            elif is_float(value) and is_last_unary_negative and is_second_last_exponential:
                parsed_too[-1] = f"-{value}"
            # Dealing with double unary negatives.
            elif is_float(value) and is_last_unary_negative and is_second_last_unary_negative:
                parsed_too_second_last_i = len(parsed_too) - 2
                parsed_too = parsed_too[0:parsed_too_second_last_i]
                parsed_too.append(value)
            else:
                parsed_too.append(value)
        return parsed_too

    # Translates infix notation into postfix notation.
    def get_translation(self):
        # Precedence order definition.
        precedence = {
            "**": 4, "p": 3, "n": 3, "/": 2,
            "//": 2, "%": 2, "*": 2, "+": 1,
            "-": 1, "(": 0, ")": 0
        }
        # Stack and postfix result variables.
        stack = Stack([])
        postfix = []
        # Logic to order characters in postfix logic.
        for char in self.get_parsed():
            if is_float(char):
                postfix.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
            else:
                while stack and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)
        # Remove excess parentesis.
        stack = list(filter(lambda x: x != "(", stack))
        # Add postfix values that are still in the stack.
        while stack:
            postfix.append(stack.pop())
        # Join postfix in a string.
        return " ".join(postfix)

    # Solves a postfix expression to get a final numeric answer.
    def get_result(self):
        stack = Stack([])
        postfix = self.get_translation().split(" ")
        for value in postfix:
            if is_float(value):
                num_value = float(value)
                stack.append(num_value)
            elif value == "p":
                num_value = float(stack.pop())
                stack.append(num_value)
            elif value == "n":
                num_value = float(stack.pop())
                stack.append(num_value * -1)
            else:
                num2, num1 = [stack.pop(), stack.pop()]
                match value:
                    case "**":
                        stack.append(num1 ** num2)
                    case "/":
                        stack.append(num1 / num2)
                    case "//":
                        stack.append(num1 // num2)
                    case "%":
                        stack.append(num1 % num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
        return stack.pop()

    # Prints a value obtained from a postfix expression answer.
    def print(self):
        parsed_string = " ".join(self.get_parsed()).replace("n", "-").replace("p", "+")
        translation_string = self.get_translation().replace("n", "-").replace("p", "+")
        print(f"\nExpressão digitada: {parsed_string}")
        print(f"Expressão pós-fixa: {translation_string}")
        print(f"Resultado: {self.get_result()}\n")


# Stack class.
class Stack(list):
    def __init__(self, stack):
        self.stack = stack


main()
