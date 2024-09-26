from test_framework import generic_test

""" 8.2 """


def evaluate(expression: str) -> int:
    """Evaluate RPN"""
    delimiter = ","
    operators = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "/": lambda y, x: x // y,
        "*": lambda y, x: x * y,
    }

    intermediate_results = []
    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(
                operators[token](intermediate_results.pop(), intermediate_results.pop())
            )
        else:
            intermediate_results.append(int(token))

    return intermediate_results[-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )
