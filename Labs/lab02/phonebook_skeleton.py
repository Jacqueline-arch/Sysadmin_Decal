#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        entry = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, 'a') as f: f.write(entry + "\n")
        
      
    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            with open(PHONEBOOK_ENTRIES, 'r') as f: print(f.read())
         

    elif sys.argv[1] == "lookup":
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, 'r') as output:
            for line in output:
                tmp = line.split()
                n = " ".join(tmp[0:len(tmp)-1])
                if name == n:
                    print(tmp[-1])

                
                    


    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'r+') as f:
            data = ''.join([i for i in f if not i.startswith(name)]) 
            # print(data)
            f.seek(0)                                                         
            f.write(data)                                                    
            f.truncate()

    elif sys.argv[1] == "clear":
        with open(PHONEBOOK_ENTRIES, 'w') as file: file.close()

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            print(lookup)


if __name__ == "__main__":
    main()
