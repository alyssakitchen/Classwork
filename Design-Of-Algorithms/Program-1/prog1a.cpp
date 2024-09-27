#include <iostream>
using namespace std;

int main(){
    int size = 15;
    int inputList[size] = {4, 8, 1, 1, 5, 1, 0, 5, 9, 0, 2, 0, 0, 3, 5};
	int currentIndex = 0;
	int occurrence = 0;
	int targetElement = 0; //test with targetElement = 0, 1, 2

	for(int i=0; i<size; i++){
		if(inputList[currentIndex] == targetElement)
			occurrence++;
		
		if(occurrence == 3){
			cout << "Occurrence 3 of the number " << targetElement << " is at index " << currentIndex << "." << endl;
            occurrence++;
        }
		currentIndex++;
	}

	if(occurrence < 3)
		cout << "There are not 3 occurrences of the number " << targetElement << " in the list." << endl;

	return 0;
}