# Advanced Python Programming - CaN Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
    ...
"""


from threading import Thread
from requests import get

class DownloadThread(Thread):

    """ 
        Thread that will connect to specified URL and download the file.
    """

    number_of_threads = 0

    def __init__(self, url, file_name):
        super().__init__()
        # establish specific thread name
        DownloadThread.number_of_threads += 1
        self.name = 'DownloadThread-' + str(DownloadThread.number_of_threads)
        # establish url and file name
        self.url = url
        self.file_name = file_name

    def run(self):
        print(f'{self.name} started...')
        self.connectAndDownload(self.url, self.file_name)
    
    # override the method when the thread is finished
    def join(self):
        print(f'{self.name} finished...')
        super().join()

    def connectAndDownload(self, url, file_name):
        
        # connect to url and download file
        # save file to specified location
        try:
            
            resp = get(url)

            if resp.status_code == 200:

                # its mandatory to open the file in binary mode
                # as resp.content is in bytes
                with open(file_name, 'wb') as f:
                    f.write(resp.content)
                    print(f'File {file_name} downloaded successfully from {url}')
            else:
                print(f'ERROR: response code {resp.status_code} while downloading file from {url}')

        except Exception as e:
            print(f'ERROR: {e} while downloading file from {url}')

class DecryptThread(Thread):
    pass

def launchDownloadThreads(fileUrls):
    
    """
        Launches a 'DowloadThread' thread for each file and waits to be downloaded.
    """

    # create a list of threads
    threads = []

    for fu in fileUrls.values():
        # create thread and add it to the list
        print(f'\tCreating thread for url: {fu[0]} and file: {fu[1]}')
        thread = DownloadThread(fu[0], fu[1])
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

def launchDecryptThreads(fileUrls):
    pass

def main(): 

    # define file and urls 
    fileUrls = {
                'dt1': ('https://advancedpython.000webhostapp.com/s1.txt', 's1_enc.txt'), 
                'dt2': ('https://advancedpython.000webhostapp.com/s2.txt', 's2_enc.txt'), 
                'dt3': ('https://advancedpython.000webhostapp.com/s3.txt', 's3_enc.txt')
            }
    
    # launch and wait to finish for DownloadThreads
    launchDownloadThreads(fileUrls)

    # launch and wait to finish for DecryptThreads
    launchDecryptThreads(fileUrls)


if __name__ == '__main__':
    main()