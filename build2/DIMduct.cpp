#include <string>
#include <windows.h>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[]){

    //https://stackoverflow.com/questions/15435994/how-do-i-open-an-exe-from-another-c-exe (#)
    // additional information #
    STARTUPINFO si;     
    PROCESS_INFORMATION pi;

    // set the size of the structures #
    ZeroMemory( &si, sizeof(si) );
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi) );

    // basicamente um comando pro terminal
    string arg = "\"./python/pythonw.exe\" DIMduct.py";
    // conversão de string pra char*
    char* tab2 = new char[arg.length()+1];
    strcpy (tab2, arg.c_str());

    // start the program up #
    CreateProcess( NULL,   // the path #
        tab2,            // Command line # // no VS Code aparece como um erro, mas o g++ compila assim
        NULL,           // Process handle not inheritable #
        NULL,           // Thread handle not inheritable #
        FALSE,          // Set handle inheritance to FALSE #
        0,              // No creation flags #
        NULL,           // Use parent's environment block #
        NULL,           // Use parent's starting directory #
        &si,            // Pointer to STARTUPINFO structure #
        &pi             // Pointer to PROCESS_INFORMATION structure (removed extra parentheses) #
        );
    // Close process and thread handles. #
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );

    return 0;
}