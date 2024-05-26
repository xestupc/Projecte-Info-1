
class Console_Colors:

    # these are to be used in the console for colored text.
    
    # text styles
    CEND         = '\33[0m' # returning to normal text style and format
    CBOLD        = '\33[1m'
    CITALIC      = '\33[3m'
    CURL         = '\33[4m'
    CBLINK       = '\33[5m'
    CBLINK2      = '\33[6m'
    CSELECTED    = '\33[7m'

    # simple text color options
    CBLACK       = '\33[30m'
    CRED         = '\33[31m'
    CGREEN       = '\33[32m'
    CYELLOW      = '\33[33m'
    CBLUE        = '\33[34m'
    CVIOLET      = '\33[35m'
    CBEIGE       = '\33[36m'
    CWHITE       = '\33[37m'
   
    # background color with white text
    CBLACKBG     = '\33[40m'
    CREDBG       = '\33[41m'
    CGREENBG     = '\33[42m'
    CYELLOWBG    = '\33[43m'
    CBLUEBG      = '\33[44m'
    CVIOLETBG    = '\33[45m'
    CBEIGEBG     = '\33[46m'
    CWHITEBG     = '\33[47m'
   
    # slight variations of the simple colors
    CGREY        = '\33[90m'
    CRED2        = '\33[91m'
    CGREEN2      = '\33[92m'
    CYELLOW2     = '\33[93m'
    CBLUE2       = '\33[94m'
    CVIOLET2     = '\33[95m'
    CBEIGE2      = '\33[96m'
    CWHITE2      = '\33[97m'

    # background color with black text except for white on black
    CGREYBG      = '\33[100m'
    CREDBG2      = '\33[101m'
    CGREENBG2    = '\33[102m'
    CYELLOWBG2   = '\33[103m'
    CBLUEBG2     = '\33[104m'
    CVIOLETBG2   = '\33[105m'
    CBEIGEBG2    = '\33[106m'
    CWHITEBG2    = '\33[107m'

"""
print("The following are format text options: \n")
print(f"{Console_Colors.CEND       } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBOLD      } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CITALIC    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CURL       } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBLINK     } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBLINK2    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CSELECTED  } This is a printing test with every color in the class! {Console_Colors.CEND}")
print("\n\n\n" )

print("The following are simple text color options: \n")
print(f"{Console_Colors.CBLACK     } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CRED       } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CGREEN     } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CYELLOW    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBLUE      } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CVIOLET    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBEIGE     } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CWHITE     } This is a printing test with every color in the class! {Console_Colors.CEND}") 
print("\n\n\n")

print("The following are simple text background color options, all text is in white: \n")
print(f"{Console_Colors.CBLACKBG   } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CREDBG     } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CGREENBG   } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CYELLOWBG  } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBLUEBG    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CVIOLETBG  } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBEIGEBG   } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CWHITEBG   } This is a printing test with every color in the class! {Console_Colors.CEND}") 
print("\n\n\n")

print("The following are simple text color options. These are slight variations from the second one we've seen: \n")
print(f"{Console_Colors.CGREY      } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CRED2      } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CGREEN2    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CYELLOW2   } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBLUE2     } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CVIOLET2   } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CBEIGE2    } This is a printing test with every color in the class! {Console_Colors.CEND}")   
print(f"{Console_Colors.CWHITE2    } This is a printing test with every color in the class! {Console_Colors.CEND}") 
print("\n\n\n")

print("The following are simple text background color options, all text is in black except for white on black: \n")
print(f"{Console_Colors.CGREYBG    } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CREDBG2    } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CGREENBG2  } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CYELLOWBG2 } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CBLUEBG2   } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CVIOLETBG2 } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CBEIGEBG2  } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print(f"{Console_Colors.CWHITEBG2  } This is a printing test with every color in the class! {Console_Colors.CEND}")  
print("\n\n\n")
"""