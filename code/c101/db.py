import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
     
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9i_tpuSxSVNSWFnTO2YQq3eT-_ZVP9u12ShykzMJTnbU8KTk-YGc8q8C5n56MBf0TQlsFNC9z_Ckrc3wwAeGY-H6tibKOU7fi7MaVBQQ7lIz5zzBoAnlCq5p8H_-M1-UBFZ57I'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file uploaded correctly")

    main()