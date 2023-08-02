// 766. Toeplitz Matrix

// https://leetcode.com/problems/toeplitz-matrix/

bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    int r = matrixSize - 1, c = 0, num;
    for (int i = 0; i < matrixSize + (*matrixColSize); i++) {
        int flag = 0, r2 = r, c2 = c;
        while (r2 < matrixSize && c2 < (*matrixColSize)) {
            if (flag == 0) {
                num = matrix[r2][c2];
                flag = 1;
            }
            else if (matrix[r2][c2] != num) {
                return false;
            }
            r2++;
            c2++;
        }
        if (r != 0) {
            r--;
        }
        else {
            c++;
        }
    }
    return true;
}