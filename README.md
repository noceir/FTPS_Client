# FTPS_Client
## Secure FTP Client Script Documentation
This script demonstrates how to upload a file securely to an FTP server using FTPS (FTP over SSL/TLS) in Python.

- Prerequisites
    Python 3.x
    ftplib module (standard library)
- Usage :
    Ensure that the FTP server supports FTPS connections.
    Update the script with the appropriate FTP credentials and file paths:
    
        ftp_host: The hostname or IP address of the FTP server.
        ftp_username: The username for the FTP server.
        ftp_password: The password for the FTP server.
        local_file_path: The local file path of the file to upload.
        destination_directory: The destination directory on the FTP server.

    Run the script using a Python interpreter.
# Script Details
-The script follows these steps:

   Import the necessary modules:

        from ftplib import FTP_TLS: Import the FTP_TLS class from the ftplib module.
        
   Set the FTP credentials and file paths:
   
        ftp_host: Replace with the hostname or IP address of the FTP server.
        ftp_username: Replace with the username for the FTP server.
        ftp_password: Replace with the password for the FTP server.
        local_file_path: Replace with the local file path of the file to upload.
        destination_directory: Replace with the destination directory on the FTP server.
        
   Establish an FTPS connection:

        Create an instance of the FTP_TLS class with the ftp_host.
        Call the login method with ftp_username and ftp_password to authenticate.
        Call the prot_p method to activate the secure data connection using SSL/TLS.
        ![image](https://github.com/noceir/FTPS_Client/assets/134208026/39df0e63-44a8-41d3-b29b-aa443a02fb25)

        
   Upload the file:

        Change to the destination directory on the FTP server using the cwd method.
        Open the local file in binary mode using open with "rb" mode.
        Use the storbinary method to upload the file to the FTP server, specifying the file name and file object.
        
   Handle exceptions:

        Catch any exceptions that occur during the file upload process and print the error message.
        
Close the FTP connection:

Use the quit method to close the FTP connection.
Security Considerations
FTPS provides encryption for the data transmission between the client and the server, protecting it from eavesdropping.
Ensure that the FTP server supports FTPS and is properly configured for secure connections.
PS* this is tested on a hostinger hosting.
