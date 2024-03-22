def custom_random(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = (a * seed + c) % m
    return seed / m

def main():
    seed = int(input("Enter a seed value for random number generation: ") or 1234)
    num_values = int(input(f"Enter the number of values to draw randomly (default 1000): ") or 1000)
    num_fractions = max(2, min(int(input(f"Into how many fractions do you want to divide the interval (between 2 and 10, default 5): ") or 5, 10)))

    counters = [0] * num_fractions
    random_values = [custom_random(seed) for _ in range(num_values)]

    for value in random_values:
        counters[int(value * num_fractions)] += 1

    print("Counters' state:")
    for i, count in enumerate(counters):
        print(f"Fraction [{i/num_fractions:.2f}-{(i+1)/num_fractions:.2f}]: {count} occurrences")

if __name__ == "__main__":
    main()
