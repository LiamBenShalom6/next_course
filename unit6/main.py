import file1
import file2

def main():
    greetingCard = file1.GreetingCard("liam", "lian")
    greetingCard.greeting_msg()
    birthdayCard = file2.BirthdayCard("liam", "lian", 18)
    birthdayCard.greeting_msg()



if __name__ == '__main__':
    main()