import pysftp
import paramiko
from decouple import config


class RemoteServerConnection:
    def __init__(self):
        self.host = config("REMOTE_HOST")
        self.username = config("REMOTE_USERNAME")
        self.password = config("REMOTE_PASSWORD")

    def connect(self):
        try:
            sftp = pysftp.Connection(host=self.host, username=self.username, password=self.password)
            print("SFTP server connected successfully")
            return sftp

        except paramiko.ssh_exception.SSHException as e:
            print(e)
