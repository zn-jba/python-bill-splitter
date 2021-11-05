from random import choice


def main():
    friends = dict()

    try:
        num_friends = int(input("Enter the number of friends joining (including you):\n"))
        if num_friends <= 0:
            raise ValueError
    except ValueError:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for _ in range(num_friends):
            name = input()
            friends[name] = 0

        total_bill = int(input("\nEnter the total bill value:\n"))

        lucky_message = '\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n'
        has_lucky = input(lucky_message) == "Yes"

        if has_lucky:
            lucky_one = choice(list(friends.keys()))
            bill_per_person = round(total_bill / (len(friends.keys()) - 1), 2)
            friends = {person: bill_per_person if person != lucky_one else 0
                       for (person, _) in friends.items()}
            print(f"\n{lucky_one} is the lucky one!")
        else:
            bill_per_person = round(total_bill / len(friends.keys()), 2)
            friends = {person: bill_per_person for (person, _) in friends.items()}
            print("\nNo one is going to be lucky")

        print(f"\n{friends}")


if __name__ == "__main__":
    main()
