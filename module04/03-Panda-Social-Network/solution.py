class Panda():
    def __init__(self, panda_name, panda_email, panda_gender):
        self.panda_name = panda_name
        self.panda_email = panda_email
        self.panda_gender = panda_gender

    def name(self):
        return self.panda_name

    def email(self):
        return self.panda_email

    def gender(self):
        return self.panda_gender

    def isMale(self):
        return self.panda_gender == "male"

    def isFemale(self):
        return self.panda_gender == "female"

    def __str__(self):
        return self.panda_name + self.panda_email + self.panda_gender

    def __hash__(self):
        #return hash(self.panda_name) + hash(self.panda_email) + hash(self.panda_gender)
        return hash((self.panda_name, self.panda_email, self.panda_gender))
    def __eq__(self, other):
        return self.panda_name == other.panda_name and self.panda_email == other.panda_email and self.panda_gender == other.panda_gender


class PandaSocialNetwork():
    def __init__(self):
        self.social_network = []
        self.friend_list = dict()

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere
        else:
            self.social_network.append(panda)
            self.friend_list[panda] = []

    def has_panda(self, panda):
        return panda in self.social_network

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends()
        else:
            self.friend_list.get(panda1).append(panda2);
            self.friend_list.get(panda2).append(panda1);

    def are_friends(self, panda1, panda2):
        return panda2 in self.friend_list.get(panda1)

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.friend_list.get(panda)
        else:
            return False

    def connection_level(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            return 1
        elif (not self.has_panda(panda1)) or (not self.has_panda(panda2)):
            return False
