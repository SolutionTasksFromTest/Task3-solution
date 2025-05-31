def compute_f(n: int) -> int:
    f_prev2: int = 1 
    f_prev1: int = 3
    f_curr: int = 0

    if n == 0:
        return f_prev2
    if n == 1:
        return f_prev1

    for _ in range(2, n + 1):
        f_curr = 5 * f_prev1 + f_prev2
        f_prev2, f_prev1 = f_prev1, f_curr

    return f_curr


def main() -> None:
    n_target: int = 58
    result: int = compute_f(n_target)
    print(result)


if __name__ == "__main__":
    main()