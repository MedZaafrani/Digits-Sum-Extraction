import re

file_path = "C:/Users/moham/OneDrive/Bureau/STAGE/testTECH/document.txt"

def total_pairs_infile(file_path):
    total_pair = 0

    with open(file_path, "r",) as file:
        for line in file:
            #line.strip()
            numbers = re.findall(r'\d', line)  # Extract numbers

            if len(numbers) >= 1:  
                pair_numbers = int(numbers[0] + numbers[-1])  
            
            else:
                pair_numbers = 0  

            total_pair += pair_numbers  

    return total_pair


result = total_pairs_infile(file_path)
print(f"la somme de toutes les valeurs d'étalonnage est {result}")
