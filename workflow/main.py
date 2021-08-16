import paramiko
from server.remote_connect import RemoteServerConnection
from server.remote_server import RemoteServerOperation
from decouple import config


def main():
    # sftp server connection
    host = config("REMOTE_HOST")
    username = config("REMOTE_USERNAME")
    password = config("REMOTE_PASSWORD")
    try:
        with RemoteServerConnection(host=host, username=username, password=password) as sftp_connection:
            print("Server connection established")
            # remote server object
            remote_server = RemoteServerOperation(sftp_connection)
            # copy files from remote server directory
            remote_server.copy_file_from_remote(localdir='D:\\Divergent\\RPA\\dump', remotedir='/opt/dump')
    except paramiko.ssh_exception.SSHException as e:
        print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)


if __name__ == '__main__':
    main()
