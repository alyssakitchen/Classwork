/*
Name: Alyssa Kitchen
Title: Program 2 - Sorting
Due Date: 10/27/2023
Description: This program reads in the value of n from the user, then creates three arrays
(one random, one increasing, and one decreasing) of size 10^n. It then sorts those arrays 4
different ways for each array using Shell Sort, Insertion Sort, Selection Sort, and Bubble Sort,
then prints the results to a text file.
*/

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <chrono>
using namespace std;

//Array Generators
/*
Name: generateRandomArray()
Description: This function dynamically allocates an array and fills it in with integers
in a random order. It takes in the size of the array as a parameter and returns the filled
in array back to the main function.
*/
int* generateRandomArray(int size){
    srand(time(NULL));
    int* array = new int[size];

    for(int i=0; i<size; i++){
        array[i] = rand();
    }
    return array;
}
/*
Name: generateIncreasingArray()
Description: This function dynamically allocates an array and fills it in with integers
in an increasing order. It takes in the size of the array as a parameter and returns the filled
in array back to the main function.
*/
int* generateIncreasingArray(int size){
    int* array = new int[size];
    int i = 0;

    do{
        array[i] = rand() % 100 + 1;
        while(array[i] <= array[i-1]){
            array[i]++;
        }
        i++;
    }while(i < size);
    return array;
}

/*
Name: generateDecreasingArray()
Description: This function dynamically allocates an array and fills it in with integers
in a decreasing order. It takes in the size of the array as a parameter and returns the filled
in array back to the main function.
*/
int* generateDecreasingArray(int size){
    int* array = new int[size];
    int i = 0;
    do{
        array[i] = rand() % 100 + 1;
        while(i > 0 && array[i] >= array[i-1]){
            array[i]--;
        }
        i++;
    }while(i < size);
    return array;
}

//Sorting Algorithms
/*
Name: shellSort()
Description: This function uses shell sort, which applies insertion sort
to each of several interleaving sublists of a given list. It takes in the
array and the size of the array as parameters. It returns the integer
variable "time", which is the difference between the end time and start
time from the high_resolution_clock.
*/
int shellSort(int* array, int size){
    std::chrono::high_resolution_clock::time_point start, end;
    start = std::chrono::high_resolution_clock::now();
    
    int temp = 0;
    int j = 0;

    for(int interval=size/2; interval>0; interval=interval/2){
        for(int i=interval; i<size; i++){
            temp = array[i];
            j = i;
            while (j>=interval && array[j-interval] > temp){
                array[j] = array[j-interval];
                j = j - interval;
            }
            array[j] = temp;
        }
    }
    end = std::chrono::high_resolution_clock::now();
    int time = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    return time;
}

/*
Name: insertionSort()
Description: This function splits the array into a sorted part and an unsorted part
and makes comparisons then inserts a given value in the correct place.
It takes in the array and the size of the array as parameters. It returns
the integer variable "time", which is the difference between the end time
and start time from the high_resolution_clock.
*/
int insertionSort(int* array, int size){
    std::chrono::high_resolution_clock::time_point start, end;
    start = std::chrono::high_resolution_clock::now();

    int v = 0;
    int j = 0;

    for(int i=1; i<size; i++){
        v = array[i];
        j = i - 1;

        while(j >= 0 && array[j] > v){
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = v;
    }
    end = std::chrono::high_resolution_clock::now();
    int time = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    return time;
}

/*
Name: selectionSort
Description: This function splits the array into a sorted part and an unsorted
part. It iterates through the unsorted part of the array and selects the
smallest number, then places it in its correct place in the sorted array.
It takes in the array and the size of the array as parameters. It returns the
integer variable "time", which is the difference between the end time and start
time from the high_resolution_clock.
*/
int selectionSort(int* array, int size){
    std::chrono::high_resolution_clock::time_point start, end;
    start = std::chrono::high_resolution_clock::now();

    int min = 0;
    int temp = 0;
    for(int i=0; i<size-2; i++){
        min = i;
        for(int j=i+1; j<size-1; j++){
            if(array[j] < array[min]){
                min = j;
            }
        }
        temp = array[i];
        array[i] = array[min];
        array[min] = temp;
    }
    end = std::chrono::high_resolution_clock::now();
    int time = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    return time;
}

/*
Name: bubbleSort()
Description: This function iterates through the array one element at a time
and compares it to its adjacent element. If the first element is larger than
the second element, they swap places. Once it reaches the end of the array,
it goes back to the beginning and starts again. This loops until the array
is sorted. It takes in the array and the size of the array as parameters.
It returns the integer variable "time", which is the difference between the
end time and start time from the high_resolution_clock.
*/
int bubbleSort(int* array, int size){
    std::chrono::high_resolution_clock::time_point start, end;
    start = std::chrono::high_resolution_clock::now();

    int temp = 0;
    for(int i=0; i<size-2; i++){
        for(int j=0; j<size-2-i; j++){
            if(array[j+1] < array[j]){
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    end = std::chrono::high_resolution_clock::now();
    int time = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    return time;
}

int* storeArray(int* array, int size){
    int* newArray;
    for(int i=0; i<size; i++){
        newArray[i] = array[i];
    }

    return newArray;
}


//Main Function
/*
Name: main()
Description: This function assigns the size of the array based on the value
of n. It creates three arrays by calling the generate___Array functions and
assigns the return value of those functions to integer array variables.
It then calls the four sorting functions three times each, once sending it
the randomArray, once sending it the increasingArray, and once sending it
the decreasingArray. At the end of the function, it deallocates each of the
arrays and returns 0.
*/
int main(){
    int n;
    ofstream outFile;
    outFile.open("DoA-Program2-SortTimes", ios::app);

    cout << "What is the value of n you would like to use?" << endl;
    cin >> n;
    int size = pow(10, n);
    int* randomArray = generateRandomArray(size);
    int* increasingArray = generateIncreasingArray(size);
    int* decreasingArray = generateDecreasingArray(size);

    //The for loops after each sorting algorithm call revert the array back to its original, unsorted state.
    int* tempRand = storeArray(randomArray, size);
    int* tempDec = storeArray(decreasingArray, size);

    //Random Array
    outFile << "n = " << n << endl;
    outFile << "RANDOM ARRAY" << endl;
    outFile << "shell: " << shellSort(randomArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        randomArray[i] = tempRand[i];
    }
    outFile << "insertion: " << insertionSort(randomArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        randomArray[i] = tempRand[i];
    }
    outFile << "selection: " << selectionSort(randomArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        randomArray[i] = tempRand[i];
    }
    outFile << "bubble: " << bubbleSort(randomArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        randomArray[i] = tempRand[i];
    }

    //Increasing Array
    outFile << "\nINCREASING ARRAY" << endl;
    outFile << "shell: " << shellSort(increasingArray, size) << " microseconds." << endl;
    outFile << "insertion: " << insertionSort(increasingArray, size) << " microseconds." << endl;
    outFile << "selection: " << selectionSort(increasingArray, size) << " microseconds." << endl;
    outFile << "bubble: " << bubbleSort(increasingArray, size) << " microseconds." << endl;

    //Decreasing Array
    outFile << "\nDECREASING ARRAY" << endl;
    outFile << "shell: " << shellSort(decreasingArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        decreasingArray[i] = tempDec[i];
    }
    outFile << "insertion: " << insertionSort(decreasingArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        decreasingArray[i] = tempDec[i];
    }
    outFile << "selection: " << selectionSort(decreasingArray, size) << " microseconds." << endl;
    for(int i=0; i<size; i++){
        decreasingArray[i] = tempDec[i];
    }
    outFile << "bubble: " << bubbleSort(decreasingArray, size) << " microseconds." << endl << endl;
    for(int i=0; i<size; i++){
        decreasingArray[i] = tempDec[i];
    }
    
    delete [] randomArray;
    delete [] increasingArray;
    delete [] decreasingArray;
    delete [] tempRand;
    delete [] tempDec;

    return 0;
}