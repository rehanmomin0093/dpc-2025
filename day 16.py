import math

def find_lcm(N, M):
    return (N * M) // math.gcd(N, M)


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(find_lcm(N, M))
