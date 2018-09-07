
# def docdownloader():
#     file1 = drive.CreateFile()
#     file1.SetContentFile(C:\Users\hpadmin\PycharmProjects\Application_Writer)
#     file1.Upload()

# from pydrive.drive import GoogleDrive

from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.


from pydrive.drive import GoogleDrive
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello World!') # Set content of the file from given string.
file1.Upload()
