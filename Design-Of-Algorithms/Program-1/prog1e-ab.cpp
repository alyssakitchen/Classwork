#include <iostream>
using namespace std;

int main(){
	int size = 15;
    int inputList[size] = {0, 0, 0, 0, 4, 6, 2, 7, 9, 4, 7, 3, 8, 3, 2}; //Best Case
    //int inputList[size] = {3, 2, 1, 4, 4, 6, 2, 7, 9, 4, 7, 3, 8, 3, 2}; //Worst Case
	int currentIndex = 0;
	int occurrence = 0;
	int targetElement = 5;
	int n;
	cout << "Enter the value of n for the number of occurrences: ";
	cin >> n;

	for(int i=0; i<size; i++){
		if(inputList[currentIndex] == targetElement)
			occurrence++;
		
		if(occurrence == n){
			cout << "Occurrence " << n << " of the number " << targetElement << " is at index " << currentIndex << "." << endl;
            occurrence++;
        }
		currentIndex++;
	}

	if(occurrence < n)
		cout << "There are not " << n << " occurrences of the number " << targetElement << " in the list." << endl;

	return 0;
}