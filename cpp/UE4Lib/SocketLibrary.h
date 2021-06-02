#pragma once

namespace YJ
{
    // create and connect server(in_IP, in_Port, out_socket)
    int CreateAndConnect(char IPAddress[256], int Htons, void *&Socket);

    // set socket  non-blocking mode, return 0, if success
    int Ioctlsocket(void * Socket)
    
    // receive message(in_Socket, in_data, in_length, in_flag(default 0)); return the fact length of message received
    int ReceiveMSG(void *Socket, char* Data, int Num, int Flags=0);

    // send mesage(in_Socket, in_data, in_flag,(default 0))；return the fact length of message sended
    int SendMSG(void * Socket, char *Data, int Num, int Flags);

    // close Socket
    int CloseSocket(void *Socket); 
}
