/*
A -> aBa
B -> bAb
B -> c

E -> TZ
T -> a
Z -> +TZ | e | R
R -> -TZ | e
*/

#include <iostream>
#include <string>
using namespace std;

bool belongs = true;
string word = "a+a+a";
int i = 0;
int TAM = word.size();

void E();
void Z();
void T();
void R();


int main() {
	if (word != "") {
		if (word[i] == 'a') E();
		else{
			cout << "Falso" << endl;
			belongs = false;
		}
		//if (i != word.size()) belongs = false;
	}
	else{
		cout << "Falso" << endl;
		belongs = false;
	}
	if (belongs) cout << "Pertenece" << endl;
	else cout << "No Pertenece" << endl;
	return 0;
}

void E(){
	T();
	Z();
}

void T(){
	if (word[i] == 'a'){
		Check(i);
	}
	else {
		cout << "Falso" << endl;
		belongs = false;
		return;
	}
}

void Z(){
	if (word[i] == '+'){
		i++;
		T();
		Z();
	}
	else {
		cout << "Falso" << endl;
		belongs = false;
		return;
	}
	if (word[i] == 'e') i++;
	else {
		cout << "Aqui Falso" << endl;
		belongs = false;
		return;
	}
	R();
}

void R(){
	if (word[i] == '-') i++;
	else {
		cout << "Falso" << endl;
		belongs = false;
		return;
	}
	T();
	Z();
	if (word[i] == 'e') i++;
	else {
		cout << "Falso" << endl;
		belongs = false;
		return;
	}
}

void Check(int i){
	if (word[i])
}
/*
void A(){
	if (word.size() - i < 3) {
		belongs = false;
		return;
	}
	// A -> a B a
	if (word[i] == 'a') i++;
	else {
		belongs = false;
		return;
	}
	B();
	if (word[i] == 'a') i++;
	else {
		belongs = false;
		return;
	}
}

void B(){
	// B -> c
	if (word[i] == 'c') {
		i++;
		return;
	}
	if (word.size() - i < 3) {
		belongs = false;
		return;
	}
	// B -> b A b
	if (word[i] == 'b') i++;
	else {
		belongs = false;
		return;
	}
	A();
	if (word[i] == 'b') i++;
	else {
		belongs = false;
		return;
	}
}*/
