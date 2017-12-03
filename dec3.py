import math

index = int(input("Enter index:\n")) # Index given in assignment

# Find dimensions of minimum oddnumbered n*n matrix (needs a center element)
dim = math.ceil(math.sqrt(index))
if (dim % 2 == 0):
    dim += 1
print("Requires ", dim, "*", dim, " matrix")

maxElements = dim * dim # maximum elements in the matrix
print("Max elements: ", maxElements)

maxSteps = dim - 1 # Worst case is equal to the N-1:
                   # On both dimensions you must traverse to the center
                   # (I.E. N/2) and account for (N % 2 != 0)
print("Max steps: ", maxSteps)

# Find the closest outer corner
primaryDist = (maxElements - index) % (dim -1)
alternateDist = dim - primaryDist # If index is across the center of its edge
                                  # use the other corner instead
dist = min(primaryDist, alternateDist) 

distTotal = maxSteps - dist # Because one dimension has a fixed distance
                            # (I.E. from edge to center), only the distance
                            # from the corner to the index is needed.
                            # Subtract from worst case.
print("Requires ", distTotal, " steps")
