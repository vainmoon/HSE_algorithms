def tracer_decorator(func):
    stack_depth = 0

    def wrapper(*args, **kwargs):
        nonlocal stack_depth
        indent = "\t" * stack_depth
        print(indent + f"{func.__name__}({', '.join(map(str, args))})")
        stack_depth += 1
        result = func(*args, **kwargs)
        stack_depth -= 1
        print(indent + f"returned: {result}")
        return result

    return wrapper


@tracer_decorator
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


@tracer_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    factorial(5)
    print("_" * 100)
    fibonacci(5)
