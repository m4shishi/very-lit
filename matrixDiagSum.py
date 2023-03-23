class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 2 and len(mat[0]) == 2:
            return mat[0][0] + mat[0][1] + mat[1][0] + mat[1][1]
        elif len(mat) == 1:
            return mat[0][0]

        sum = 0
        for i in range(len(mat)):
            if len(mat) % 2 == 0:
                sum += mat[i][i] + mat[i][len(mat) - 1 - i]
            else:
                sum += mat[i][i] + mat[i][len(mat) - 1 - i]
        if len(mat) % 2 != 0:
            sum = sum - mat[len(mat)//2][len(mat)//2]
        return sum
