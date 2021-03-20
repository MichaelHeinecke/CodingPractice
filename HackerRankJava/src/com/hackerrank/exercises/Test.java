package com.hackerrank.exercises;

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Test {

    static final Scanner sc = new Scanner(System.in);

    static void printMatrix(double[][] matrix) {
        boolean isIntMatrix = true;

        intCheck:
        for (double[] row : matrix) {
            for (double d : row) {
                if (d % 1 != 0) {
                    isIntMatrix = false;
                    break intCheck;
                }
            }
        }

        System.out.println("The result is:");

        if (isIntMatrix) {
            for (double[] row : matrix) {
                System.out.println(Arrays.stream(row).mapToObj(d -> new DecimalFormat("#")
                        .format(d)).collect(Collectors.joining(" "))
                );
            }
        } else {
            for (double[] row : matrix) {
                System.out.println(Arrays.stream(row).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
            }
        }
    }

    private static double[][] transposeMatrixAlongHorizontalLine(double[][] matrix) {
        double[][] transposedMatrix = new double[matrix.length][matrix[0].length];

        for (int idx = matrix.length - 1, tIdx = 0; tIdx < transposedMatrix.length; idx--, tIdx++) {
            transposedMatrix[tIdx] = matrix[idx].clone();
        }

        return transposedMatrix;
    }

    private static double[][] transposeMatrixAlongVerticalLine(double[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] transposedMatrix = new double[rows][cols];

        for (int rowIdx = 0; rowIdx < rows; rowIdx++) {
            for (int colIdx = cols - 1, tColIdx = 0; tColIdx < cols; colIdx--, tColIdx++) {
                transposedMatrix[rowIdx][tColIdx] = matrix[rowIdx][colIdx];
            }
        }

        return transposedMatrix;
    }

    private static double[][] transposeMatrixAlongMainDiagonal(double[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] transposedMatrix = new double[cols][rows];

        for (int rowIdx = 0; rowIdx < rows; rowIdx++) {
            for (int colIdx = cols - 1, tColIdx = 0; tColIdx < cols; colIdx--, tColIdx++) {
                transposedMatrix[colIdx][rowIdx] = matrix[rowIdx][colIdx];
            }
        }

        return transposedMatrix;
    }

    private static double[][] transposeMatrixAlongSideDiagonal(double[][] matrix) {
        double temp = 0;
        for(int col = 0; col < matrix.length - 1; col++)
            for(int row = 0; row < matrix.length - 1 - col; row++){
                temp = matrix[row][col];
                matrix[row][col] = matrix[matrix.length - 1 - col][matrix.length - 1 - row];
                matrix[matrix.length - 1 - col][matrix.length - 1 - row] = temp;
            }

        return matrix;
    }

    public static void main(String[] args) {
        double[][] matrix = new double[][]{
                {1, 1, 1},
                {2, 2, 2},
                {-1, 3, 3}};

        double[][] transposedMatrix = transposeMatrixAlongMainDiagonal(matrix);
        printMatrix(transposedMatrix);

//        printMatrix(matrix);
    }
}
