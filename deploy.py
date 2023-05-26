from ftplib import FTP_TLS

# FTP credentials
ftp_host = "ftp+domain"
ftp_username = "ftp_username"
ftp_password = "ftp_passwd"

# Local file path to upload
local_file_path = "C:\\Users\\path\\example.zip"
    
# Destination directory on the FTP server
destination_directory = "/public_html"


try:
    # Connect to the FTP server with TLS/SSL encryption
    ftp = FTP_TLS(ftp_host)
    ftp.login(ftp_username, ftp_password)
    ftp.prot_p()  # Activate secure data connection

    # Change to the destination directory
    ftp.cwd(destination_directory)

    # Open the local file in binary mode
    with open(local_file_path, "rb") as file:
        # Upload the file to the FTP server
        ftp.storbinary(f"STOR {file.name}", file)

    print("File upload successful.")

except Exception as e:
    print("Error occurred during file upload:", str(e))

finally:
    # Close the FTP connection
    if 'ftp' in locals() and ftp is not None:
        ftp.quit()
