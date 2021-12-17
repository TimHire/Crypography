// NEED TO MAKE SURE TO DISABLE REAL-TIME SCANNING IN MCAFEE OTHERWISE THE PROGAM WILL NOT RUN

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>						// In order to get time(0) for the random seed
#include "Quadgrams.h"					// File containing the array of all the quadgram scores
#include "Trigrams.h"					// File containting the array of all the trigram scores 
extern double qgram[];					// Array with the quadgram scores
extern double trigrams[17576];			// Array with the trigram scores
#define getName(var) #var				// Stringizing Operator allowing for variable names to be printed as strings						// 


// Function declarations
void prepare(char text[], char ciphertext[]);
double cost(char text[], long len);
void substitution_swap(char text[], int len, int a, int b);
void sim_annealing(char text[], int len);
double accept_prob(double temp, double current_cost, double max_cost);
int get_random(int random1);
double random_0_1();



// Ciphertext input
char raw_ciphertext[] = "KHUPR PKDGZDUQhGKH.UVKH.KDGEHHQZDUQHGWLPHDQGDJDLQEXWVKHKDGUHIXVHGWREHOLHYHKHUVKHKDGGRQHHYHUBWKLQJULJKWDQGVKHNQHZVKHZRXOGEHUHZDUGHGIRUGRLQJVRZLWKWKHSURPRWLRQVRZKHQWKHSURPRWLRQZDVJLYHQWRKHUPDLQULYDOLWQRWRQOBVWXQJLWWKUHZKHUEHOLHIVBVWHPLQWRGLVDUUDBLWZDVKHUILUVWELJOHVVRQLQOLIHEXWQRWWKHODVWMRVKKDGVSHQWBHDUDQGBHDUDFFXPXODWLQJWKHLQIRUPDWLRQKHNQHZLWLQVLGHRXWDQGLIWKHUHZDVHYHUDQBRQHORRNLQJIRUDQHASHUWLQWKHILHOGMRVKZRXOGEHWKHRQHWRFDOOWKHSUREOHPZDVWKDWWKHUHZDVQRERGBLQWHUHVWHGLQWKHLQIRUPDWLRQEHVLGHVKLPDQGKHNQHZLWBHDUVRILQIRUPDWLRQSDLQVWDNLQJOBPHPRULCHGDQGVRUWHGZLWKQRWDVROHJLYLQJHYHQDQRXQFHRILQWHUHVWLQWKHWRSLFVRPHWLPHVWKDWVMXVWWKHZDBLWKDVWREHVXUHWKHUHZHUHSUREDEOBRWKHURSWLRQVEXWKHGLGQWOHWWKHPHQWHUKLVPLQGLWZDVGRQHDQGWKDWZDVWKDWLWZDVMXVWWKHZDBLWKDGWREHVSHQGLQJWLPHDWQDWLRQDOSDUNVFDQEHDQHAFLWLQJDGYHQWXUHEXWWKLVZDVQWWKHWBSHRIHAFLWHPHQWVKHZDVKRSLQJWRHASHULHQFHDVVKHFRQWHPSODWHGWKHVLWXDWLRQVKHIRXQGKHUVHOILQVKHNQHZVKHGJRWWHQKHUVHOILQDOLWWOHPRUHWKDQVKHEDUJDLQHGIRULWZDVQWRIWHQWKDWVKHIRXQGKHUVHOILQDWUHHVWDULQJGRZQDWDSDFNRIZROYHVWKDWZHUHORRNLQJWRPDNHKHUWKHLUQHAWPHDOVKHVDWLQWKHGDUNHQHGURRPZDLWLQJLWZDVQRZDVWDQGRIIKHKDGWKHSRZHUWRSXWKHULQWKHURRPEXWQRWWKHSRZHUWRPDNHKHUUHSHQWLWZDVQWIDLUDQGQRPDWWHUKRZORQJVKHKDGWRHQGXUHWKHGDUNQHVVVKHZRXOGQWFKDQJHKHUDWWLWXGHDWWKUHHBHDUVROGVDQGBVVWXEERUQSHUVRQDOLWBKDGDOUHDGBEORRPHGLQWRIXOOYLHZ";
//char ciphertext[] = "LQLWLDOOBWKHIDEOHVZHUHDGGUHVVHGWRDGXOWVDQGFRYHUHGUHOLJLRXVVRFLDODQGSROLWLFDOWKHPHVWKHBZHUHDOVRSXWWRXVHDVHWKLFDOJXLGHVDQGIURPWKHUHQDLVVDQFHRQZDUGVZHUHSDUWLFXODUOBXVHGIRUWKHHGXFDWLRQRIFKLOGUHQWKHLUHWKLFDOGLPHQVLRQZDVUHLQIRUFHGLQWKHDGXOWZRUOGWKURXJKGHSLFWLRQLQVFXOSWXUHSDLQWLQJDQGRWKHULOOXVWUDWLYHPHDQVDVZHOODVDGDSWDWLRQWRGUDPDDQGVRQJLQDGGLWLRQWKHUHKDYHEHHQUHLQWHUSUHWDWLRQVRIWKHPHDQLQJRIIDEOHVDQGFKDQJHVLQHPSKDVLVRYHUWLPH";
char ciphertext[4096];				// Empty array for the good ciphertext to be copied in during the prepare function


void main() {
	prepare(raw_ciphertext, ciphertext);
	int cipher_len = strlen(ciphertext);

	printf("The ciphertext has been correctly inputted - length: %d characters\n", cipher_len);
	printf("Initial quadgram score for %s: %.6f\n", getName(ciphertext), cost(ciphertext, cipher_len));

	sim_annealing(ciphertext, cipher_len);
}



void prepare(char rawtext[], char ciphertext[]) {
	if (strlen(rawtext) > 4096) {
		printf("The inputted cipher text is too long for the 4096 prepared ciphertext array");
		exit(1);
	}
	int good_char_count = 0;							// Allows for indexing in the empty array
	for (int i = 0; i < strlen(rawtext); i++) {
		if (isupper(rawtext[i])) {						// Need to copy to the prepared array
			ciphertext[good_char_count] = rawtext[i];
			good_char_count++;
		}
		else if (islower(rawtext[i])) {					// copy text - 32 to prepared array
			ciphertext[good_char_count] = rawtext[i] - 32;
			good_char_count++;
		}
	}
}

double cost(char text[], long len) {
	double score = 0;
	for (int i = 0; i < len - 3; i++) {
		int index = (text[i] - 65) * (26 * 26 * 26) + (text[i + 1] - 65) * (26 * 26) + (text[i + 2] - 65) * 26 + (text[i + 3] - 65);
		score += qgram[index];
	}
	/*for (int i = 0; i < len - 2; i++) {							// Cost method using trigrams
		int index = (text[i] - 65) * (26 * 26) + (text[i + 1] - 65) * 26 + (text[i + 2] - 65);
		score += trigrams[index];
	}*/
	return score / (len - 3);					// Normalises by the number of blocks calculated ==> larger divisor more bad accepted (currently ~10%)
}

void substitution_swap(char text[], int len, int a, int b) {					// Function to swap letters a and b in the text
	for (int i = 0; i < len; i++) {
		if (text[i] == a) {
			text[i] = b;
		}
		else if (text[i] == b) {
			text[i] = a;
		}
	}
}

void sim_annealing(char text[], int len) {	
	double t = 1;
	double focus = 0.99;						// How quickly the simulated annealing becomes stable
	double t_min = 0.00001;							// Ending point when the program returns the best value
	int iterations = 50;						// Number of iterations happening at each temperature
	int count = 0, prob_accept = 0;				// For keeping count of the total swaps and the times it has jumped around (accepted when worse cost)
			
	char* best_text = malloc(len + 1);			// Pointer to array to store the current best result --> dynamic memory allocation to cater for any ciphertext size
	double best_cost = cost(text, len);
	char* max_text = malloc(len + 1);
	double max_cost = cost(text, len);
	char* current_text = malloc(len + 1);
	double current_cost = cost(text, len);

	strncpy(best_text, text, len);							// For storing the best score recorded
	strncpy(max_text, text, len);							// For storing the local maximum
	strncpy(current_text, text, len);						// For storing the current test array

	srand(time(0));						// Seed the pseudo-random number generator with the compile time so different numbers each time
	double prob, random;
	int random1, random2;

	while (t > t_min) {
		for (int i = 0; i < iterations; i++) {
			random1 = (rand() % 26) + 65;
			random2 = get_random(random1);
			substitution_swap(current_text, len, random1, random2);				// Need to change the numbers to be random variables
			current_cost = cost(current_text, len);

			if (current_cost >= max_cost) {
				strncpy(max_text, current_text, len);
				max_cost = current_cost;
				if (current_cost >= best_cost) {
					strncpy(best_text, current_text, len);
					best_cost = current_cost;
				}
			}
			else {
				prob = accept_prob(t, current_cost, max_cost);
				random = random_0_1();
				
				if (prob > random) {											// Chance that will still be updated
					strncpy(max_text, current_text, len);
					max_cost = current_cost;
					prob_accept += 1;
				}
				else {
					strncpy(current_text, max_text, len);						// Need to copy back the old text into the current text to allow for a new change to be made
					current_cost = max_cost;
				}
			}
			count += 1;
		}
		t = focus * t;
	}
	printf("%d : %d ==>  final text: %.6f ::\n", count, prob_accept, best_cost);
	for (int k = 0; k < len; k++) {
		printf("%c", best_text[k]);
	}
	printf("\n");

	free(best_text);
	free(max_text);
	free(current_text);
}

double accept_prob(double temp, double current_cost, double max_cost) {
	double e = 2.71828182845904523536028747;
	double diff = current_cost - max_cost;						// Not sure if it is right to do best_cost - current_cost
	double diff_final = diff / temp;
	double exp = pow(e, diff_final);
	return exp;
}

int get_random(int random1) {
	int random2 = (rand() % 26) + 65;
	if (random2 == random1) {
		get_random(random1);
	}
	return random2;
}

double random_0_1() {
	return (double)rand() / (double)RAND_MAX;
}