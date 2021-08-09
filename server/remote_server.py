import os
from datetime import date


class RemoteServerOperation:
    def __init__(self, sftp_connection):
        self.sftp = sftp_connection

    @staticmethod
    def formatting_date():
        today = date.today()
        date_str = str(today)
        date_split = date_str.split('-')
        return "".join(date_split)

    def copy_file_from_remote(self, localdir, remotedir):
        try:
            # check local directory exists
            if os.path.exists(localdir):

                # check remote directory exist
                if self.sftp.isdir(remotedir):
                    # list all the files and dir in remote
                    files_list = self.sftp.listdir(remotedir)

                    # check if file in not empty
                    if len(files_list) != 0:
                        for file in files_list:
                            file = file.split('_')
                            # check current date file in remote file list
                            if self.formatting_date() in file:
                                file_name = '_'.join(file)
                                # join local file path
                                local_file_path = os.path.join(localdir, file_name)

                                # Check file already exists in local
                                if os.path.exists(local_file_path):
                                    # remove file
                                    os.remove(local_file_path)
                                    # create file in local
                                    with open(local_file_path, 'w') as file:
                                        pass
                                    self.sftp.get(remotepath=f'{remotedir}/{file_name}',
                                                  localpath=f'{localdir}\\{file_name}',
                                                  preserve_mtime=True)
                                    print(
                                        f"Copy file from remote successful. [REMOTE_PATH] - {remotedir}. [FILE_NAME] - {file_name}.")
                                else:
                                    # create file in local
                                    with open(local_file_path, 'w') as file:
                                        pass
                                    self.sftp.get(remotepath=f'{remotedir}/{file_name}',
                                                  localpath=f'{localdir}\\{file_name}',
                                                  preserve_mtime=True)
                                    print(
                                        f"Copy file from remote successful. [REMOTE_PATH] - {remotedir}. [FILE_NAME] - {file_name}.")
                    else:
                        print("File list is empty")
                else:
                    print("Remote directory not exists")
            else:
                # create local directory if not exists
                os.mkdir(localdir)
                self.copy_file_from_remote(localdir, remotedir)

        except Exception as e:
            from traceback import print_exc
            print_exc()
            print(e)
