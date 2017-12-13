with open("input7.txt", "r") as f:
    programs = [p.strip() for p in f.readlines()]
    # Get all tower programs
    towers = [p for p in programs if "->" in p]
    # Each tower root is a candidate (strip away weight for comparability)
    candidates = set([t.split(" ")[0] for t in towers])
    branches = set()
    for t in towers:
        # Find all unique branches, account for whitespaces
        newBranchList = [x.strip() for x in t.split("->")[1].split(",")]
        branches = branches | set(newBranchList)
    # Find set of candidates that are not in the set of branches
    root = list(candidates-branches)[0]

print("Root program is: ", root)
f.close()
