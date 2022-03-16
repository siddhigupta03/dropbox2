import os
import dropbox

class TransferData(object):
    def _init_(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        local_path = ""
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BC-pgFK6LIIVDE_4FwI_NHZY6qCwk5N8xg0Sxg06-u3LIVFWZelL4OKcCndcfNgLq01bxR3FzGIjpPtFVNZ04Y75IUCamSuw'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path: ")
    file_to = input("Enter the dropbox file path: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Transfered successfully.")

if __name__ == '__main__':
    main()