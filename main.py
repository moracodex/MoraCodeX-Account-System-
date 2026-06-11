import random    #    ]
import string    #    ] =>>> import
import time      #    ]
import os 
punctuation = string.punctuation      #    ]
lowercase   = string.ascii_lowercase  #    ]
uppercase   = string.ascii_uppercase  #    ] =>  random leters
digits      = string.digits           #    ]

punctuation_user = False  #    ]
lowercase_user   = False  #    ]
uppercase_user   = False  #    ] => deta letters user
digits_user      = False  #    ]
coin_user  = 15
email_user = "@gmail.com"

loop_name  =  []        #    ]
loop_age   =  []        #    ] = > loop information
loop_email =  []        #    ]
loop_password = []      #    ]

def show_brand():  # define Show brand
    brand = """
  __  __  ____  _____            _____  ____  _____  ______  __   __

 |  \/  |/ __ \|  __ \     /\    / ____|/ __ \|  __ \|  ____| \ \ / /
 | \  / | |  | | |__) |   /  \  | |    | |  | | |  | | |__     \ V / 
 | |\/| | |  | |  _  /   / /\ \ | |    | |  | | |  | |  __|     > <  
 | |  | | |__| | | \ \  / ____ \| |____| |__| | |__| | |____   / . \ 
 |_|  |_|\____/|_|  \_\/_/    \_\\______|\____/|_____/|______|/_/ \_\ 

    """
    print(brand)
    print("=" * 69)
    print("   OFFICIAL PROJECT BY: MORACODEX CORPORATION")
    print("   AUTHORIZED BY: CEO MORA (THE PROFESSIONAL)")
    print("   STATUS: ACTIVE | VERSION: 1.0.0")
    print("=" * 69)
    print("\n") # defin Moracodex


def creat_accaunt():  # creat accaunt
    global punctuation_user, lowercase_user, uppercase_user, digits_user, coin_user

    print("Welcome to our app ")

    while True:  # loop  start by user
        accaunt = input("Please, Enter 'Start' becouse creat accaunt: ").lower()

        if accaunt == "start":
            user_info = {
                "name": None,
                "age": None,
                "email": None,
                "password": None,
            }
            os.system("clear") # تنظيف الشاشه ( مسح الشاشه)
            break
        else:
            print("!"*10 +  "\nfrist! creat acaunt!\n" + "!"*10)

    while True:  # loop name
        name = input("Enter your name: ")

        if name:
            if name not in loop_name:
                user_info["name"] = name
                loop_name.append(name)
                print("condetaion....")
                time.sleep(1)
                os.system("clear")
                break
            else:
                print('='*10 + "\nPlease CHange  this name\n" + "="*10)
        else:
            print("=" * 10 + "\nPlease, Enter your name\n")

    while True:  # loop age
        try:
            user_info['age']  = int(input("Enter your age: "))

            if user_info['age'] >= 15:  # لو العمر أكبر من أو يساوي 15
                print("condetion....")
                time.sleep(1)
                print('='*10 + "\nsuccess!\n" + '='*10)
                os.system('clear') 
                break  # اخرج من اللوب وكمل باقي البرنامج


            else:

                print("=" * 10 + "\nNo,Enter your age >= 15\n" + "=" * 10)

        except ValueError:
            print("=" * 15 + "\nPlease enter number not letters or others\n" + "=" * 15)

    while True:  # loop email
        email = input("Enter your email: ")

        if email.endswith("@gmail.com"):
            if email not in loop_email:
                loop_email.append(email)
                user_info['email'] = email
                print("Condetion....")
                time.sleep(1)
                print("=" * 10 + "\nYou email success!\n" + "=" * 10)
                os.system('clear') #  المترجم : يا كمبيوتر , الككمبيوتر : نعم , المترجم : امر من رئيس الجمهوريه بمسع الشاشه , الكمبيوتر....تم
                break
            else:
                print('='*10 + "\nPlease change this email\n"+ '='*10)
        else:
            print(
                "=" * 10
                + "\nPlease enter an email address ending with @gmail.com\n"
                + "=" * 10
            )

    while True:  # loop passwerd
        password = input("Enter pasword strongth: ")
        try_again = input("Try again, Enter pasword strongth: ")
        punctuation_user = False
        lowercase_user = False
        uppercase_user = False
        digits_user = False

        if password == try_again:

            for letter in password:
                 if letter in punctuation:
                       punctuation_user = True
                 if letter in lowercase:
                         lowercase_user = True
                 if letter in uppercase:
                     uppercase_user = True
                 if letter in digits:
                      digits_user = True

            if punctuation_user and lowercase_user and uppercase_user and digits_user:
                    if password not in loop_password:
                           loop_password.append(password)
                           user_info['password'] = password
                           print("condation....")
                           time.sleep(1)

                           print(f"\nSuccess! Your password '{user_info['password']}' is now strong. Please save it securely!" )    

                           os.system("clear")
                           break
                    else:
                          print('='*10 + "\nPlease, Change this password\n" + '='*10)


            else:
                      print("=" * 10 + "Hlep" + "=" * 10)
                      print(
              "Your password must include uppercase, lowercase, and symbols to ensure maximum security. "
                 )
                      print("=" * 20)
        else:
            print("="*10 + "\nPlrase, Correct this password\n"+'='*10)


    # condetion
    print("\nSaving your data to MORACODE DATABASE...")
    time.sleep(1)
    print("Securing your password...")
    time.sleep(1)
    print("Securing your email......")
    time.sleep(1)
    print("Generating your wallet...")
    time.sleep(1.5)
    print("\nDONE! ✅")

    # Massge end successe!
    print("\n" + "★ " * 20)
    print(f"   WELCOME TO THE FAMILY, {user_info['name'].upper()}!")
    print("   Your account has been officially activated.")
    print("   Now, you are a member of MORACODE CORPORATION.")
    print(f"   We’ve added {coin_user} Coins to your wallet as a gift! 🎁")
    print("★ " * 20)
    print("\n   SYSTEM STATUS: ALL SYSTEMS GO! 🚀")
    print("   Ready to start your first challenge?")
    print("=" * 40) # creat accaunt

show_brand()
creat_accaunt()
