nclude <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <fstream>
#include <time.h>

using namespace std;

ofstream manusFile;

void openFiles() {
    time_t timestamp = time(0);

    // Open file for EMG log
    if (manusFile.is_open()) {
        manusFile.close();
    }
    std::ostringstream manusFileString;
    manusFileString << "manus-" << timestamp << ".csv";
    manusFile.open(manusFileString.str(), std::ios::out);
    manusFile << "timestamp,deviceID,"
        << "wrist_imus_w,wrist_imus_x,wrist_imus_y,wrist_imus_z"
        << "thumb_imus_w,thumb_imus_x,thumb_imus_y,thumb_imus_z"
        << "thumb_MCP,thumb_IP,index_MCP,index_IP,middle_MCP,middle_IP,ring_MCP,ring_IP,pinky_MCP,pincy_IP"
        << std::endl;
}

int main(int args, char** argv)
{
    
    openFiles();
    cout << "ni mei" << endl;
    printf("bu bao cuo\n");
    return 0;

}
