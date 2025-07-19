#Leetcode - class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # col increse -> row increase -> col decrease -> row decrease
        res = []

        left_bound, top_bound = 0, 0
        right_bound, bottom_bound = len(matrix[0]) - 1, len(matrix) - 1

        while top_bound <= bottom_bound and left_bound <= right_bound:

            #left -> right
            for i in range(left_bound, right_bound + 1):
                res.append(matrix[top_bound][i])
            top_bound += 1

            #top -> bottom
            #If column is not available then traversal will not happen
            for i in range(top_bound, bottom_bound + 1):
                res.append(matrix[i][right_bound])
            right_bound -= 1

            #right -> left
            #Checking if we have any row left if not without this if condition traversal will still happen.
            if top_bound <= bottom_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[bottom_bound][i])
                bottom_bound -= 1

            #bottom -> top
            if left_bound <= right_bound:
                for i in range(bottom_bound, top_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1

        return res

      




        

#define left, right, top, down bounds and traverse as requested in question left->right then top->bottom then right->left and then bottom->top after each traversal increase or decrease the bounds respectively. Keep boundy conditions in mind(whether it is possible to traverse - do we have valid rows or columns available)
