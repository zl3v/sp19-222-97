// Name of program mainreturn.cpp
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{

    ofstream myfile;

    cout << "You have entered " << argc
         << " arguments:" << "\n";

    for (int i = 0; i < argc; ++i)
        cout << argv[i] << "\n";

    myfile.open("my_name.txt");
    myfile << argv[1];
    myfile.close();

    return 0;
}
