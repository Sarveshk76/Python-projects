def TowerOfHanoi(n, A, B, C):
    if n == 1:
        print("Move disk 1 from source", A, "to destination", B)
        return
    TowerOfHanoi(n - 1, A, C, B)
    print("Move disk", n, "from source", A, "to destination", B)
    TowerOfHanoi(n - 1, C, B, A)
n = 4
TowerOfHanoi(n, 'A', 'B', 'C')