def cetakgambar(n):
    for i in range(n):
        for a in range(n):
            if i == 0 or i == n-1 or i%2 == 0 or a == 0 or a == n-1:
                print("*", end="  ")
            else:
                print ("=", end = "  ")
        print()
    
cetakgambar(5)