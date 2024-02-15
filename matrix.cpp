#include <iostream>
using namespace std;

int main() {

    int row1, column1;

    cout << "Number of Rows and Columns for 1st matrix: ";
    cin >> row1 >> column1;

    int matrix1[row1][column1];

    cout << "Enter the elements of 1st matrix: " << endl;
    for (int i = 0; i < row1; i++) {
        for (int j = 0; j < column1; j++) {
            cin >> matrix1[i][j];
        }
    }

    int row2, column2;

    cout << "Number of Rows and Columns for 2nd matrix: ";
    cin >> row2 >> column2;

    if (row2 != row1 || column2 != column1) {
        cout << "Matrix addition is not possible." << endl;
        return 1;
    }

    int matrix2[row2][column2];

    cout << "Enter the elements of 2nd matrix: " << endl;
    for (int i = 0; i < row2; i++) {
        for (int j = 0; j < column2; j++) {
            cin >> matrix2[i][j];
        }
    }

    int sumMatrix[row1][column1];

    cout << "Sum of the two matrices: " << endl;
    for (int i = 0; i < row1; i++) {
        for (int j = 0; j < column1; j++) {
            sumMatrix[i][j] = matrix1[i][j] + matrix2[i][j];
            cout << sumMatrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
