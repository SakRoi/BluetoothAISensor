#include <stdio.h>
#include <math.h>

int main()
{
    double A1[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int input[3] = {1, 2, 3};
    float weights[3][10] = {{-0.6, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -0.10},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10}};
    float biases[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

    for (int i = 0; i < 10; i++){ //dot production of a matrix
        int col_sum = 0;
        for (int j = 0; j < 3; j++) {
            col_sum += input[j] * weights[j][i];
        }
        A1[i] = col_sum;
    }

    for (int j = 0; j < 10; j++){ //adding biases to the output
        A1[j] += biases[j];
    }

    for (int i = 0; i < 10; i++){ //ReLU, if A1[i] is bigger than zero, keep it, else make it 0
        A1[i] = (A1[i] > 0) ? A1[i] : 0; 
    }

    for (int i = 0; i < 10; i++){ //dot production of a matrix
        int col_sum = 0;
        for (int j = 0; j < 3; j++) {
            col_sum += input[j] * weights[j][i];
        }
        A1[i] = col_sum;
    }

    for (int j = 0; j < 10; j++){ //adding biases to the output
        A1[j] += biases[j];
    }

    for (int j = 0; j < 10; j++){
        printf("A1: %f\n", A1[j]);
    }

    double A2[6] = {0, 0, 0, 0, 0, 0};
    float weights2[10][6] = {{0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6},
                            {0.1, 0.2, 0.3, 0.4, 0.5, 0.6}};

    float biases2[6] = {1, 1, 1, 1, 1, 1};
    
    for (int i = 0; i < 6; i++){ //dot production of a matrix
        int col_sum = 0;
        for (int j = 0; j < 10; j++) {
            col_sum += A1[j] * weights2[j][i];
        }
        A2[i] = col_sum;
    }

    for (int i = 0; i < 6; i++){ //adding biases to the output
        A2[i] += biases2[i];
    }

    for (int i = 0; i < 6; i++){
        printf("A2: %f\n", A2[i]);
    }

    double output[6];
    double expSum = 0;

    for (int i = 0; i < 6; i++){
        double exponential = exp(A2[i]);
        output[i] = exponential;
        expSum += exponential;
    }

    for (int i = 0; i < 6; i++){
        double softMax = output[i];
        softMax = softMax/expSum;
        printf("softMax: %f\n", softMax);
        output[i] = softMax;
        printf("Output: %f\n", output[i]);
    }

}