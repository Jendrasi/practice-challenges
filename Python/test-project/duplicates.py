# remove duplicates
items = [8, 4, 0, 3, 6, 1, 7, 5, 3, 6, 2, 8, 7, 0, 9, 5, 4, 3, 2]

def unique(items: list):
    uniqueItems = []
    for item in items:
        if item not in uniqueItems:
            uniqueItems.append(item)
    return uniqueItems
            
print(unique(items))