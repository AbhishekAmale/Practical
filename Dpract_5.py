# # Size of the board (N x N)
# N = 4  # Change N for different board sizes
# board = [[0] * N for _ in range(N)]

# # Function to print the board
# def print_board():
#     for i in range(N):
#         for j in range(N):
#             print("Q " if board[i][j] else ". ", end="")
#         print()

# # Function to check if placing a queen at (row, col) is safe
# def is_safe(row, col):
#     # Check column
#     for i in range(row):
#         if board[i][col]:
#             return False

#     # Check upper-left diagonal
#     i, j = row, col
#     while i >= 0 and j >= 0:
#         if board[i][j]:
#             return False
#         i -= 1
#         j -= 1

#     # Check upper-right diagonal
#     i, j = row, col
#     while i >= 0 and j < N:
#         if board[i][j]:
#             return False
#         i -= 1
#         j += 1

#     return True

# # Function to solve the N-Queens problem using backtracking
# def solve(row):
#     if row >= N:  # All queens are placed
#         return True

#     for col in range(N):
#         if is_safe(row, col):
#             board[row][col] = 1  # Place queen
#             if solve(row + 1):  # Move to the next row
#                 return True
#             board[row][col] = 0  # Backtrack

#     return False  # No solution in this configuration

# # Main logic to solve and print the solution
# board[0][0] = 1  # Place the first queen at (0, 0)
# if solve(1):  # Start solving from the second row
#     print(f"Solution for the {N}-Queens problem:")
#     print_board()
# else:
#     print("No solution exists.")


# N=int(input("Enter Board Size :"))
# board=[[0]*N for _ in range(N)]

# def is_safe(row,col):
#     for i in range (row):
#         if board[i][col]==1:
#             return False
#     i,j=row,col
#     while i>=0 and j>=0:                    #      \
#         if board[i][j]==1:                  #       \
#             return False                    #        \
#         i=i-1
#         j=j-1
#     i,j=row,col
#     while i>=0 and j<N: 
#         if board[i][j]==1:
#             return False                   #         /
#         i=i-1                              #        /
#         j=j+1                              #       /
            
#     return True

# def print_board():
#     for i in range(N):
#         for j in range(N):
#             print("Q" if board[i][j] else ".",end=" ")
#         print()
                
# def solve(row):
#     if row ==N:
#         return True
#     for col in range(N):
#         if is_safe(row,col):
#             board[row][col]=1
#             if solve(row+1):
#                 return True
#             board[row][col]=0
#     return False

# if solve(0):
#     print_board()
# else:
#     print("No solution exists.")