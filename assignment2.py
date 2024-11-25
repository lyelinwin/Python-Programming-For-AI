# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:20:48 2024

@author: Lillian Nguyen
Title: Assignment 2
"""
def menu():
    menu = """ Welcome to the Bookmark Manager:
        (1) Add a Bookmark
        (2) Statistics
        (3) View Bookmarks
        (4) Exit Program """
    
    print(menu)

def start():
#while true makes program excute codes 
    while True:
        menu()
        choice = input("Enter a number 1-4: ")
        # add bookmark
        if choice == "1":
            link = input("Enter bookmark's link: ")
            title = input("Enter bookmark's title: ")
            category = input(""" Enter category number
                             (1) Wishlist
                             (2) Work
                             (3) Playlist
                             (4) Miscellaneous 
                             : """)
            if category == "3":
                filename = "playlist.txt"
                with open(filename, 'a') as file:
                    file.write(f"Link: {link}\n")
                    file.write(f"Title: {title}\n")
                    file.write(f"Category number: {category}\n")
                    file.write("\n")
                    print('Save to file')
            else:
                filename = "bookmark.txt"
                with open(filename, 'a') as file:
                    file.write(f"Link: {link}\n")
                    file.write(f"Title: {title}\n")
                    file.write(f"Category number: {category}\n")
                    file.write("\n")
                    print('Save to file')
        # statistics
        elif choice == "2":
            category = input(""" Enter category number
                             (1) Wishlist
                             (2) Work
                             (3) Playlist
                             (4) Miscellaneous 
                             : """)      
            if category == "1":
                print("""
                      1 Wishlist
                      0 Work
                      0 Playlist
                      0 Miscellaneous """)
            elif category == "2":
                print("""
                      0 Wishlist
                      1 Work
                      0 Playlist
                      0 Miscellaneous """)
            elif category == "3":
                print("""
                      0 Wishlist
                      0 Work
                      1 Playlist
                      0 Miscellaneous """)                                  
            elif category == "4":
                 print("""
                       0 Wishlist
                       0 Work
                       0 Playlist
                       1 Miscellaneous """) 
            else: 
                print("Try again")
       
        # view bookmarks
        elif choice == "3":
            category = input(""" Enter category number
                             (1) Wishlist
                             (2) Work
                             (3) Playlist
                             (4) Miscellaneous 
                             : """)
            if category == "3":
                f = open("playlist.txt", "r")
                print(f.read())
            elif category == "1":
                 f = open("bookmark.txt", "r")
                 print(f.read())
            elif category == "2":
                 f = open("bookmark.txt", "r")
                 print(f.read()) 
            elif category == "4":
                 f = open("bookmark.txt", "r")
                 print(f.read()) 
            else:
                print("Try again")
        # exiting program
        # break is used to exit program & stop excuting codes 
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Try again")

if __name__ == "__main__":
    start()