def cosine_similarity(v1, v2):
    if(len(v1) != len(v2)):
        return 0

    under1 = 0
    under2 = 0
    up = 0

    for i in range(len(v1)):
        under1 += v1[i]**2
        under2 += v2[i]**2
        up += v1[i] * v2[i]
    
    result = up / (under1**(1/2) * under2**(1/2))
    return result

def euclidean_similarity(v1, v2):
    if(len(v1) != len(v2)):
        return 0

    result = 0
    for i in range(len(v1)):
        result += (v1[i] - v2[i])**2
    result = result**(1/2)
    return result

def input_vector():
    v1 = []
    v2 = []

    print("Enter the first vector: ")
    response = input()
    response = response.split(" ")
    for i in range(len(response)):
        v1.append(int(response[i]))
    
    print("Enter the second vector: ")
    response = input()
    response = response.split(" ")
    for i in range(len(response)):
        v2.append(int(response[i]))
    
    return v1, v2


def main():
    run = True
    v1 = []
    v2 = []

    while run:
        print("1. Cosine similarity")
        print("2. Euclidean similarity")
        print("3. Exit")

        response = int(input("Enter your choice: "))
        
        if response == 1:
            v1, v2 = input_vector()
            print(cosine_similarity(v1, v2))
        elif response == 2:
            v1, v2 = input_vector()
            print(euclidean_similarity(v1, v2))
        elif response == 3:
            run = False
        else:
            print("Error: Invalid choice")
    
    return 0

if __name__ == "__main__":
    main()