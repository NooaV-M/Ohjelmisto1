airportdata = {}

def new_data_input():
    IACO_code=input("Enter IACO code: ")
    airport_name=input("Enter airport name: ")
    airportdata.update({IACO_code:airport_name})
    return

def airportinfo_get():
    IACO_code=input("Enter IACO code: ")
    if IACO_code in airportdata.keys():
        print(airportdata[IACO_code])
    else:
        print("Airport not found")

endprogram = False

def quit_program():
    print("Quitting program")
    return True

programoptions = {"enter new":new_data_input,
                  "fetch info":airportinfo_get,
                  "quit":quit_program}

while not endprogram:
    currentinput = input("Type \"enter new\" to enter new entry,\nType \"fetch info\" to fetch airport information\nor type \"quit\" to quit program:")
    if currentinput in programoptions.keys():
        endprogram = programoptions[currentinput]()