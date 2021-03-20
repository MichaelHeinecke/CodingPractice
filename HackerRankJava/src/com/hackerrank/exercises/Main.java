package com.hackerrank.exercises;

import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    static final Scanner sc = new Scanner(System.in);

    // IO methods
    static int[][] readMatrixFromStdIn() {
        System.out.println("Enter size of matrix:");
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        int[][] matrix = new int[rows][cols];

        System.out.println("Enter matrix:");
        for (int[] row : matrix) {
            for (int idx = 0; idx < row.length; idx++) {
                row[idx] = sc.nextInt();
            }
        }

        return matrix;
    }

    static int readScalarFromStdIn() {
        System.out.println("Enter constant:");
        int constant = sc.nextInt();

        return constant;
    }

    static void printMatrix(int[][] matrix) {
        System.out.println("The result is:");
        for (int[] row : matrix) {
            System.out.println(Arrays.stream(row).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
        }
    }

    // Matrix calculation methods
    static int[][] sumMatrices(int[][] firstMatrix, int[][] secondMatrix) {
        int numRows = firstMatrix.length;
        int numCols = firstMatrix[0].length;
        int[][] result = new int[numRows][numCols];

        for (int rowIdx = 0; rowIdx < numRows; rowIdx++) {
            for (int colIdx = 0; colIdx < numCols; colIdx++) {
                result[rowIdx][colIdx] = firstMatrix[rowIdx][colIdx] + secondMatrix[rowIdx][colIdx];
            }
        }

        return result;
    }

    private static int[][] multiplyMatrixByScalar(int constant, int[][] matrix) {
        int numRows = matrix.length;
        int numCols = matrix[0].length;
        int[][] result = new int[numRows][numCols];

        for (int rowIdx = 0; rowIdx < numRows; rowIdx++) {
            for (int colIdx = 0; colIdx < numCols; colIdx++) {
                result[rowIdx][colIdx] = constant * matrix[rowIdx][colIdx];
            }
        }

        return result;
    }

    private static int[][] multiplyMatrixByMatrix(int[][] firstMatrix, int[][] secondMatrix) {
        int resultRows = firstMatrix.length;
        int resultColumns = secondMatrix[0].length;
        int[][] result = new int[resultRows][resultColumns];

        for (int row = 0; row < resultRows; row++) {
            for (int col = 0; col < result[row].length; col++) {
                result[row][col] = calculateDotProduct(firstMatrix, secondMatrix, row, col);
            }
        }

        return result;
    }

    private static int calculateDotProduct(int[][] firstMatrix, int[][] secondMatrix, int row, int col) {
        int dotProduct = 0;

        for (int i = 0; i < secondMatrix.length; i++) {
            dotProduct += firstMatrix[row][i] * secondMatrix[i][col];
        }

        return dotProduct;
    }

    // Compound matrix methods
    private static void addition() {
        int[][] firstMatrix = readMatrixFromStdIn();
        int[][] secondMatrix = readMatrixFromStdIn();

        if (firstMatrix.length != secondMatrix.length || firstMatrix[0].length != secondMatrix[0].length) {
            System.out.println("The operation cannot be performed.");
        } else {
            int[][] resultMatrix = sumMatrices(firstMatrix, secondMatrix);
            printMatrix(resultMatrix);
        }
    }

    private static void scalarMultiplication() {
        int[][] matrix = readMatrixFromStdIn();
        int scalar = readScalarFromStdIn();
        int[][] resultMatrix = multiplyMatrixByScalar(scalar, matrix);
        printMatrix(resultMatrix);
    }

    private static void matrixMultiplication() {
        int[][] firstMatrix = readMatrixFromStdIn();
        int[][] secondMatrix = readMatrixFromStdIn();

        // number of columns in firstMatrix must be equal to number of rows in second matrix
        if (firstMatrix[0].length != secondMatrix.length) {
            System.out.println("The operation cannot be performed.");
        } else {
            int[][] resultMatrix = multiplyMatrixByMatrix(firstMatrix, secondMatrix);
            printMatrix(resultMatrix);
        }
    }

    public static void main(String[] args) {

        operation: while (true) {

            System.out.println("1. Add matrices");
            System.out.println("2. Multiply matrix by a constant");
            System.out.println("3. Multiply matrices");
            System.out.println("0. Exit");
            System.out.println("Your choice:");
            int mode = sc.nextInt();

            switch (mode) {
                case 1:
                    addition();
                    break;
                case 2:
                    scalarMultiplication();
                    break;
                case 3:
                    matrixMultiplication();
                    break;
                case 4:
                    break operation;

            }
        }

        sc.close();
    }
}
