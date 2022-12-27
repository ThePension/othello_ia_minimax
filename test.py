if __name__ == "__main__":
    scores = [
            [5, 4, 3, 3, 3, 3, 3, 4, 5],
            [4, 4, 2, 2, 2, 2, 2, 4, 4],
            [3, 2, 1, 1, 1, 1, 1, 2, 3],
            [3, 2, 1, 1, 1, 1, 1, 2, 3],
            [3, 2, 1, 1, 1, 1, 1, 2, 3],
            [4, 4, 2, 2, 2, 2, 2, 4, 4],
            [5, 4, 3, 3, 3, 3, 3, 4, 5],
        ]
    
    # Get the sum of the squared scores
    sum = 0
    
    for row in scores:
        for cell in row:
            sum += cell ** 2
            
    print(sum)
    