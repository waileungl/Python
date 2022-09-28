class User:
    def __init__(self, firstName, lastName, email, age):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User already a member.")
        return self

    def spend_points(self, amount):
        if(amount > self.gold_card_points):
            print("Sorry! You don't have enough points.")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self


first_user = User('William', 'Liu', 'liuweiliang9606@hotmail.com', 26)
second_user = User('mike', 'kok', 'meiqi0204@hotmail.com', 24)

first_user.enroll().spend_points(50).display_info()

second_user.enroll().spend_points(2000).display_info()
