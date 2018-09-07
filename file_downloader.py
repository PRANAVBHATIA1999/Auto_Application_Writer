from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_to_drive(filename):
    # auth

    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile(credentials_file="mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("client_secrets.json")
    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({'title': filename})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentFile(filename)  # Set content of the file from given string.
    file1.Upload()
    drive_link = ''
    return drive_link
