# WARNING : THE CODE DOES NOT SOLVE THE PROBLEM
# I NEVER COMPLETED THIS QUESTION

def create_grid(n):
    grid = []
    for i in range(n):
        grid.append([])
        for j in range(n):
            grid[i].append('.')
    return(grid)

def check_x(a, b):
    if (a == '.' or b == '.'):
        return(True)
    else:
        return(a == 'x' or b =='x' )

def check_plus(a, b):
    if(a == '.' or b == '.'):
        return (True)
    else:
        return(a=='+' or b=='+')

def valid_grid(n, grid):
    for h_i in range (n):
        for w_i in range (n):
            for h_j in range (n):
                for w_j in range (n):
                    if ((w_j == w_i and not h_j == h_i) or (not w_j == w_i and h_j == h_i)):
                        if (not check_plus(grid[h_i][w_i], grid[h_j][w_j])):
                            #print(1)
                            return(False)
                    elif(w_i+h_i == w_j+h_j and (w_i != w_j or h_i != h_j)):
                        if(not check_x(grid[h_i][w_i], grid[h_j][w_j])):
                            #print(grid[h_i][w_i])
                            #print(grid[h_j][w_j])
                            #print(2)
                            return(False)
    return(True)


num_prob = int(input())
for i in range (1, num_prob + 1):
    dim, to_follow = [int(s) for s in input().split(" ")]
    prob_grid = create_grid(dim)
    for j in range (to_follow):
        element, pos_y, pos_x = [str(s) for s in input().split(" ")]
        prob_grid[int(pos_y) - 1][int(pos_x) - 1] = element
    print(valid_grid(dim, prob_grid))
    print(prob_grid)
    #print(prob_grid[0][0])
    #print("Case #{}: The grid is {}*{}, and there are {} instructions left".format(i,dim,dim,to_follow))