# python3

def parallel_processing(n, m, data):
    output = []
    time = 0
    t = [0] * n
    while data:
        for i in range(n):
            if t[i]==0:
                output.append((i,time))
                t[i]= data[0]-1
                data.pop(0)
                if not data:
                    break
            else:
                t[i] = t[i]-1
        time = time+1
    return output





        
            
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    x = list(map(int, input().split()))

    n = x[0]
    m = x[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i,j in result:
        print(i,j)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
