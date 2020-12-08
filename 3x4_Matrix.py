main_matrix = []

for row in range(3):
    nested_matrix = []
    for column in range(4):
        nested_matrix.append(column)
    main_matrix.append(nested_matrix)
    
print(main_matrix)