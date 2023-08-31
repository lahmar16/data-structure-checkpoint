def dot_product(v1, v2):
    R = 0
    for i in range(len(v1)):
        R += v1[i] * v2[i]
    return R

def check_orthogonal_with_function():
    n = int(input("Enter the number of pairs of vectors: "))
    
    for _ in range(n):
        v1 = list(map(float, input("Enter the first vector values separated by spaces: ").split()))
        v2 = list(map(float, input("Enter the second vector values separated by spaces: ").split()))
        
        R = dot_product(v1, v2)
        
        if R == 0:
            print("Vectors are orthogonal.")
        else:
            print("Vectors are not orthogonal.")