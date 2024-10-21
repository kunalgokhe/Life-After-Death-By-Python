# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Function to check placement of queen is SAFE
def isSafe(N,position):
    coord = np.array([[x, y] for x in range(N) for y in range(N)])
    pos=coord[position]
    unique_elements = list(set(map(tuple, pos)))
    pos = [list(item) for item in unique_elements]

    A=np.zeros([N,N])
    for i in pos:
        A[i[0],i[1]]=1
    flag=[]
    for p in pos:
        i=p[0]
        j=p[1]
        # Extract horizontal 
        h=A[i,:]
        # EXtract vertical
        v=A[:,j]
        # Extract diagonal
        if i==j:
            d1=np.diag(A)
        elif i>j:
            d1=np.diag(A,-(max([i,j])-min([i,j])))
        elif i<j:
            d1=np.diag(A,(max([i,j])-min([i,j])))    
        # Extract anti-diagonal    
        A1=np.fliplr(A.copy())
        nj = N-1-j
        if i == nj:
            d2 = np.diag(A1)
        elif i > nj:
            d2 = np.diag(A1,-(max([i,nj])-min([i,nj])))
        else:
            d2 = np.diag(A1,(max([i,nj])-min([i,nj])))
        flag.append((sum(v)+sum(h)+sum(d1)+sum(d2))==4)
    return sum(flag)

# Function for Genetic Algorithm
# Selection Function
def selection(pop,fitness):
    tournament_size = 5
    selected = []
    for _ in range(len(pop)):
        tournament = np.random.choice(len(pop), tournament_size, replace=False)
        best_individual = max(tournament, key=lambda idx: fitness[idx])
        selected.append(pop[best_individual])
    return selected

# Crossover Function
def crossover(parent1, parent2):
    # Single point crossover
    point = np.random.randint(1, N-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutate Function
def mutate(individual):
    # Mutate with a small probability
    for i in range(N):
        if np.random.rand() < mutationrate:
            individual[i] = np.random.randint(N*N)
    return individual

# Size of chessboard
N=6
# All possible coordinates of chessboard
coord = np.array([[x, y] for x in range(N) for y in range(N)])

# Define parameters
# Size of population
npop=5000
# No. of generation
ngeneration=500
# Mutation rate
mutationrate=0.02
# Generate Population
pop=[[np.random.randint(N*N) for i in range(N)] for i in range(npop)]
# Compute fitness
fitness=[isSafe(N,i) for i in pop]

# Main GA loop
for generation in range(ngeneration):
    # Selection
    selected_pop = selection(pop,fitness)
    # Crossover and produce new population
    new_pop = []
    for i in range(0, len(selected_pop), 2):
        parent1 = selected_pop[i]
        parent2 = selected_pop[i+1] if i+1 < len(selected_pop) else selected_pop[0]
        child1, child2 = crossover(parent1, parent2)
        new_pop.append(child1)
        new_pop.append(child2)
    # Mutation
    new_pop = [mutate(individual) for individual in new_pop]
    # Update population
    pop = new_pop[:npop]
    # Calculate new fitness
    fitness = [isSafe(N, i) for i in pop]
    # Check if solution found
    if np.max(fitness) == N:
        print(f"Solution found in generation {generation}")
        break

# Best solution
best_solution = pop[np.argmax(fitness)]
print(f"Best solution: \n{coord[best_solution]}\n Fitness: {np.max(fitness)}")

# Create Checkerboard
checkerboard = np.indices((N,N)).sum(axis=0)%2
plt.imshow(checkerboard,cmap='grey', interpolation='nearest')
plt.xticks([])
plt.yticks([])
# Plot location of queen
for row, col in coord[best_solution]:
    plt.plot(col, row, marker='*', color='red', markersize=12)
plt.title(f'{N}x{N} Checkerboard with a Queens Position')
# Show plot
plt.show()