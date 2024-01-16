## CaNP-Project

This project involves combining elements of concurrent programming with network programming. The goal is to create diferent groups of threads that will do different tasks like: downloadl encrypted files from URLs, decrypt their content and combine them to save the final result.

## Description
This program performs tasks using different classes:

- DownloadThread: This class inherits from the Thread superclass and connects to a specific URL to download a file. In the program, there will be three instances of this class, one for each file to download.

- DecryptThread: This class is related to the Thread superclass and is used to transform the encrypted text from each file into readable text through the Caesar Algorithm. When instantiating this object, it is mandatory to pass the following arguments: the encrypted data, the offset for the algorithm, and the file name in which it will be dumped.

- Combiner: This class combines the files in the correct order into one file.

The first two classes are also related to other functions (```launchDownloadThreads``` and ```launchDecryptThreads```) that serve as a barrier for the next task, so it won't start until all the threads from the previous step have been completed.

## How to run? 

To run this project, ensure your are in the ```CaNP-project folder```, and follow the steps below:

``` 
    python3 main.py
```

This will generate a series of files: three of them are the original encrypted files (```s1_enc.txt```, ```s2_enc.txt``` and ```s3_enc.txt```), and the result of decrypting and combining them, which is called ```s_final.txt```.

The generated file can be compared with ```correct_file.txt```, which contains the expected output once the tasks are done correctly, with this command:

```
    diff s_final.txt correct_file.txt
```

If there is no output from the command it means that the program is correct.
