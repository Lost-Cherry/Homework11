num_cats = 100
def simulate_cats_with_hats(num_cats):
    cats_with_hats_on = []
    # We want to walk around the circle num_cats times + 1
    for num in range(1, num_cats + 1):
        # Each time we walk around, we visit num_cats cats
        for cat in range(1, num_cats + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                # Remove or add hat depending on
                # whether the cat already has one
                if cats[cat]:
                    cats[cat] = False
                else:
                    cats[cat] = True

    # Add all number of each cat with a hat to list
    for cat in range(1, num_cats + 1):
        if cats[cat]:
            cats_with_hats_on.append(cat)

    # Return the resulting list
    return cats_with_hats_on

# Cats contains whether each cat already has a hat on,
# by default all are set to false since none have been visited
cats = [False] * (num_cats + 1)
print(simulate_cats_with_hats(100))
