#include "SocketLibray.h"
#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>

/* The steps involved in establishing a socket on the client side are as 
 * follows:

 * Create a socket with the socket() system call
 * Connect the socket to the address of the server using the connect() system 
 * call
 * Send and receive data. There are a number of ways to do this, but the 
 * simplest is to use the read() and write() system calls.
 */

/* The steps involved in establishing a socket on the server side are as 
 * follows:
 * Create a socket with the socket() system call
 * Bind the socket to an address using the bind() system call. For a server 
 * socket on the Internet, an address consists of a port number on the host 
 * machine.
 * Listen for connections with the listen() system call
 * Accept a connection with the accept() system call. This call typically 
 * blocks until a client connects with the server.
 * Send and receive data
 */


int socket(int domain, int type, int protocol);


