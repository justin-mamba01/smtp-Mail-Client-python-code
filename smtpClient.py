from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    """
    SMTP Mail Client Implementation for NYU CS-GY 6843.
    Communicates with an SMTP server over standard TCP sockets using raw SMTP commands.
    
    Parameters:
        port (int): Port number for the local or remote SMTP server (default: 1025)
        mailserver (str): IP address or host string of the SMTP server (default: '127.0.0.1')
    """
    # Message content and end message delimiter according to RFC 5321 standards
    msg = "\r\n I love computer networking!"
    endmsg = "\r\n.\r\n"

    # Create a TCP IPv4 socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    # Connect to the target SMTP mail server using standard tuple format
    clientSocket.connect((mailserver, port))

    # Read server greeting message (e.g., 220 Service ready)
    recv = clientSocket.recv(1024).decode()

    # Send HELO command to identify client to the server
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command specifying email sender
    mailFrom = "MAIL FROM:<alice@example.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command specifying email recipient
    rcptTo = "RCPT TO:<bob@example.com>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command to inform server that message body follows
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Send message body followed by termination sequence (\r\n.\r\n)
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    
    # Receive response acknowledging receipt of full message body
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command to close SMTP session properly
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()

    # Close the TCP socket connection
    clientSocket.close()


if __name__ == '__main__':
    # Local test execution (defaults to 127.0.0.1:1025)
    smtp_client(1025, '127.0.0.1')