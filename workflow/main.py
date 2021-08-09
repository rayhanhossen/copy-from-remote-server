from server.remote_connect import RemoteServerConnection
from server.remote_server import RemoteServerOperation


def main():
    # sftp server connection
    sftp_connection = RemoteServerConnection().connect()
    # remote server object
    remote_server = RemoteServerOperation(sftp_connection)
    # copy files from remote server directory
    remote_server.copy_file_from_remote(localdir='D:\\Divergent\\RPA\\dump',
                                        remotedir='/opt/dump')
    sftp_connection.close()


if __name__ == '__main__':
    main()
