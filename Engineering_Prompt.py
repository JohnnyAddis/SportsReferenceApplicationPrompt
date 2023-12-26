import pandas as pd
import json


def create_matrix(H2H):
    df = pd.DataFrame(H2H)

    matrix = pd.DataFrame(index=df.columns, columns=df.columns)
    
    for city in df.columns:
        for opponent in df.columns:
            if city!= opponent:
                wins = df[city][opponent]['W']
                losses = df[city][opponent]['L']
                matrix.at[city, opponent] = f"{wins}-{losses}"
            else:
                matrix.at[city, opponent] = "X"  # Marking same team matchups as 'X'


    matrix.to_html('head_to_head_matrix.html')
    return matrix

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function to execute the script
def main():
    file_path = input("Enter the path to the JSON file: ")
    try:
        data = read_json_file(file_path)
        matrix = create_matrix(data)
        print(matrix)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()