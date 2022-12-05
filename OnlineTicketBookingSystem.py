# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:50:50 2022

@author: chris
"""
seat=[]
def menu():
    print("-------------------------------------------------------------")
    print("              Online Ticket Booking           ")
    print("-------------------------------------------------------------")
    print("1.Booking")
    print("2.Cancellation")
    print("3.Display")
    print("4.Exit")
    print("-------------------------------------------------------------")

loop=True

while loop: 
    menu()
    menu_inp=int(input("Enter Option:"))
    if menu_inp==1:
        print(" ")
        print("-------------------------------------------------------------")
        seat_sel=int(input("Enter Seat Number:"))
        print(" ")
        print("-------------------------------------------------------------")
        if seat_sel in seat:
            print("-------------------------------------------------------------")
            print("SEAT UNAVAILABLE")
            print("-------------------------------------------------------------")
        else:
            seat.append(seat_sel)
    elif menu_inp==2:
        print(" ")
        print("-------------------------------------------------------------")
        seat_del=int(input("Enter seat for cancellation:"))
        print(" ")
        print("-------------------------------------------------------------")
        seat.remove(seat_del)
    elif menu_inp==3:
        print(" ")
        print("-------------------------------------------------------------")
        print("Seat booked:",seat)
        print("-------------------------------------------------------------")
    elif menu_inp==4:
        loop=False