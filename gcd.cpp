#include<iostream>
using namespace std;

int main(){

    int a, b;
    cin>>a>>b;

    while(b!=0){
        int temp = b;
        b = a%b;
        a = temp;
    }
    int final = a;
    cout<<"The gcd is "<<final<<endl;

    return 0;
}