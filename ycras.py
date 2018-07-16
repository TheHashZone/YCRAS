#!/usr/bin/env python
import random
import os
import argparse
import sys

def sort():
    os.system("bash sort.sh")

def select():
    users = open("users.txt", "r")
    user = users.readlines()

    comments = open("comments.txt", "r")
    comment = comments.readlines()

    count = len(open("users.txt").readlines())

    line = random.randint(1, count)

    use = user[line]
    commen = comment[line]

    print "\nUser: " + use
    print "\nComment: " + commen

def clean():
    os.system("rm users.txt")
    os.system("rm comments.txt")
    os.system("rm html.txt")

def main(argv):
    parser = argparse.ArgumentParser(add_help = False, description = ('Download Youtube comments without using the Youtube API'))
    parser.add_argument('--help', '-h', action = 'help', default = argparse.SUPPRESS, help = 'Show this help message and exit')
    parser.add_argument('--youtubeid', '-y', help = 'ID of Youtube video for which to download the comments')

    def downloader():
        os.system("python downloader.py -y " + youtube_id + " -o html.txt")
    
    try:
        args = parser.parse_args(argv)

        youtube_id = args.youtubeid

        if not youtube_id:
            pass

        while True:
            print "What would you like to do?\n"
            print "1. Download & Sort"
            print "2. Randomly select comment"
            print "3. Clean"
            print "4. exit"
            print "5. help"

            choice = raw_input("Choose >> ")

            if choice == "1":
                youtube_id = raw_input("Input the YouTube ID: ")
                downloader()
                sort()
                print "Downloaded and sorted!"

            elif choice == "2":
                select()

            elif choice == "3":
                clean()

            elif choice == "4" or choice == "exit":
                break

            elif choice == "5":
                parser.print_usage()

            else:
                print "Invalid command!\n"

    except Exception as e:
        print('Error:', str(e))
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])