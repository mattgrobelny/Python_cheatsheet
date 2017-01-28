#options_present

while 1:
    print "Here are all the options of the program:"
    opts_dic = {"Car":"Your drive it", "Fox": "Forest creature", "Bat": "Use me for baseball"}
    for option in opts_dic:
        print option
    print ""
    print "Or type Exit to quit"
    selected_opt = raw_input("Select an options from the ones above:")
    if selected_opt == "Exit":
        print "\n Exiting... Have a nice day"
        break
    elif selected_opt in opts_dic.keys():
        print "\n#######################"
        print "You selected:", selected_opt
        print "This means:", opts_dic[selected_opt]
        print ""
    else:
        print "Your option is not valid select one from list"
        break
