# Evaluate arithmetic expressions with parentheses and normal precedence.
# Practice: AST nodes, recursion, operator functions, and exceptions.
import ast
import math
import operator


OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}
SIGNS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def evaluate_node(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        result = float(node.value)
    elif isinstance(node, ast.BinOp) and type(node.op) in OPERATIONS:
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        result = OPERATIONS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp) and type(node.op) in SIGNS:
        result = SIGNS[type(node.op)](evaluate_node(node.operand))
    else:
        raise ValueError("Use only numbers, parentheses, and + - * / // %.")
    if not math.isfinite(result):
        raise ValueError("Result is too large or is not finite.")
    return result


def calculate(expression):
    expression = expression.strip()
    if not expression:
        raise ValueError("Expression cannot be empty.")
    if len(expression) > 200:
        raise ValueError("Expression cannot exceed 200 characters.")
    try:
        # Inspect Python's syntax tree; never execute input with eval.
        tree = ast.parse(expression, mode="eval")
        if sum(1 for _ in ast.walk(tree)) > 80:
            raise ValueError("Expression has too many operations.")
        return evaluate_node(tree.body)
    except SyntaxError as error:
        raise ValueError("Enter a valid arithmetic expression.") from error
    except ZeroDivisionError as error:
        raise ValueError("Cannot divide by zero.") from error
    except (OverflowError, RecursionError) as error:
        raise ValueError("Expression is too large or too deeply nested.") from error


def main():
    print("Arithmetic Calculator - + - * / // %, parentheses, and decimal numbers.")
    print("Results use floating-point arithmetic.")
    while True:
        expression = input("Expression (q to quit): ").strip()
        if expression.lower() == "q":
            break
        try:
            print(f"Result: {calculate(expression):g}")
        except ValueError as error:
            print(f"Invalid expression: {error}")


if __name__ == "__main__":
    main()
