def is_prime(arr):
    n = len(arr)
    
    for i in arr:
        if i == 2:
            print("True")
            continue
        for j in (2, i):
            if i % j == 0:
                print("False")
                break
            else:
                print("True")
                break
        else:
            print("True")

array = [2, 12, 3, 24]

is_prime(array)
