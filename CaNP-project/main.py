# Advanced Python Programming - CaN Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
    Program that uses concurrent programming with threads to perform the following operations simultaneously:
    - Downloading 3 files from the internet using download threads (DownloadThread).
    - Decrypting the downloaded files using decryption threads (DecryptThread).
    - Combining the decrypted files in the correct order.

    This code demonstrates the use of concurrent programming in Python 
    and how it can be used in task involving input/output operations and simultaneous data processing.

"""

from threading import Thread, Lock
from requests import get

#---------------------------------------------
# TESTING
#---------------------------------------------

import random
from collections import Counter

#-------------------------------------------------------------------------------
# GLOBAL VARIABLES
#-------------------------------------------------------------------------------
# shared vareable between threads, so its necessary to use a lock
# when accessing it to save in memory each decoded file
# so each thread will have a lock to access this variable
global_decrypted_data = {}

#---------------------------------------------
# CLASSES
#---------------------------------------------
class DownloadThread(Thread):

    """ 
        Thread that will connect to specified URL and download the file.
    """

    number_of_threads = 0

    def __init__(self, url, file_name):
        super().__init__()
        # define specific thread name
        DownloadThread.number_of_threads += 1
        self.name = 'DownloadThread-' + str(DownloadThread.number_of_threads)
        # define url and file name
        self.url = url
        self.file_name = file_name

    def run(self):
        print(f'\t\t{self.name} started...')
        self.connectAndDownload(self.url, self.file_name)
    
    # override the method when the thread is finished
    def join(self):
        print(f'\t\t{self.name} finished...')
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
                    #print(f'\t\t{self.name}: File {file_name} downloaded successfully from {url}')
            else:
                print(f'\t\t{self.name}: ERROR: response code {resp.status_code} while downloading file from {url}')

        except Exception as e:
            print(f'\t\t{self.name}: ERROR: {e} while downloading file from {url}')

class DecryptThread(Thread):
    
    """
        Thread that will decrypt the file.
    """

    # count the number of threads
    number_of_threads = 0

    # define alphabet var globally as it will be used by all threads
    # as read only, so its not necessary to use a lock
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # define a lock to be used when accesing the shared variable
    lock = Lock()

    def __init__(self, file_name, offset, decrypted_data):
        super().__init__()
        # define specific thread name
        DecryptThread.number_of_threads += 1
        self.name = 'DecryptThread-' + str(DecryptThread.number_of_threads)
        # define file name and offset
        self.file_name = file_name
        self.offset = offset
        self.decrypted_data = decrypted_data
    
    def run(self):
        print(f'\t\t{self.name} started...')
        self.decryptText(self.file_name, self.offset)

    def join(self):
        print(f'\t\t{self.name} finished...')
        ##print(f'->Decrypted data from thread {self.name}: {self.decrypted_data}') ###{DecryptThread.decrypted_data}')
        super().join()

    def decryptText(self, file_name, offset):
        
        """
            Opens the file, reads the content and call the decryptCaesar function
            with the offset as parameter.
        """

        try:
            with open(file_name, 'r') as f:
                # read file content
                content = f.read()
                # decrypt content
                decrypted_content = self.decodeCaesarAlg(content, offset)
                
                ##print(f'\tDecrypted content from thread {self.name}: {decrypted_content}\n\n')

                # save decrypted content in shared variable
                # using lock to make sure one thread is accessing the variable at a time
                with DecryptThread.lock:
                    self.decrypted_data[file_name] = decrypted_content
                    ##print(f'\t\t{self.name}: Decrypted data successfully save with offset {offset}')
        
        except Exception as e:
            print(f'\t\t{self.name}: ERROR: {e} while decrypting file {file_name} with offset {offset}')
    

    def decodeCaesarAlg(self, content, offset):
        
        """
            Decodes the given text using Caesar algorithm with the given offset.
        """
       
        # define empty string to store decoded text
        result = ''
        
        # iterate through each character in text
        for c in content:
            # if character is not in alphabet, add it to decoded text
            if c not in DecryptThread.alphabet:
                result += c
            else:
                # find the index of the character in alphabet
                pos = DecryptThread.alphabet.index(c)
                # find the index of the character after offset is applied
                newpos = (pos - offset) % len(DecryptThread.alphabet)
                # find the character at the new index
                result += DecryptThread.alphabet[newpos]

        return result

class Combiner():

    """
        Combines the decrypted files in the correct order.
    """

    def __init__(self, decrypted_data, correct_order):
        self.decrypted_data = decrypted_data
        self.correct_order = correct_order

    def mergeFiles(self, combined_filename):
        """
            Open and write the data into the file in the correct order.
        """

        with open(combined_filename, 'w') as f:
            
            for file in self.correct_order:
                f.write(self.decrypted_data[file])
                f.write('\n')

        print(f'\n\tCombined text successfully saved to file {combined_filename}')

#---------------------------------------------
# FUNCTIONS TO LAUNCH THREADS
#---------------------------------------------
def launchDownloadThreads(fileUrls):
    
    """
        Launches a 'DowloadThread' thread for each file and waits to be downloaded.
    """

    # create a list of threads
    threads = []

    for fu in fileUrls.values():
        # create thread and add it to the list
        ##print(f'\tCreating DownloadThread for url: {fu[0]} and file: {fu[1]}')
        thread = DownloadThread(fu[0], fu[1])
        threads.append(thread)

    print()

    # start all threads
    for thread in threads:
        thread.start()

    print()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

def launchDecryptThreads(global_decrypted_data, filesToDecrypt, offset):
    
    """
        Launches a 'DecryptThread' thread for each file and waits to be decrypted.
    """

    ##decryptedNames = ['s1_enc.txt',' s2_enc.txt', 's3_enc.txt']

    # create a list of threads
    threads = []

    for ftd in filesToDecrypt:
        # create thread and add it to the list
        ##print(f'\tCreating DecryptThread for file: {ftd}')
        thread = DecryptThread(ftd, offset, global_decrypted_data)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    print()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

    print()

#---------------------------------------------
# MAIN
#---------------------------------------------
def main(): 

    # define file and urls 
    fileUrls = {
                'dt1': ('https://advancedpython.000webhostapp.com/s1.txt', 's1_enc.txt'), 
                'dt2': ('https://advancedpython.000webhostapp.com/s2.txt', 's2_enc.txt'), 
                'dt3': ('https://advancedpython.000webhostapp.com/s3.txt', 's3_enc.txt')
            }
    
    DECRYPTION_OFFSET = 8
    COMBINED_FILENAME = 's_final.txt'
    CORRECT_ORDER = ['s1_enc.txt', 's2_enc.txt', 's3_enc.txt']

    # launch and wait to finish for DownloadThreads
    launchDownloadThreads(fileUrls)

    # generate list with files names to merge later
    filesToDecrypt = [filename[1] for filename in fileUrls.values()]

    # shuffle the files to decrypt, to make it more interesting
    # this will make the threads to decrypt the files in a different order
    # than the correct one, so the combiner will have to sort them
    if Counter(filesToDecrypt) ==  Counter(CORRECT_ORDER): random.shuffle(filesToDecrypt)
    
    #print(f'\nFiles to decrypt with shuffle: {filesToDecrypt}\n')

    # launch and wait to finish for DecryptThreads
    launchDecryptThreads(global_decrypted_data, filesToDecrypt, DECRYPTION_OFFSET)

    # instantiate the combiner obj to merge the decrypted files in the correct order
    combiner = Combiner(global_decrypted_data, CORRECT_ORDER)
    combiner.mergeFiles(COMBINED_FILENAME)

if __name__ == '__main__':
    main()