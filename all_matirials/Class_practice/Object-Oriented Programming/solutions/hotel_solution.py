import random


class Guest:
    id = 0

    def __init__(self, name):
        self.name = name
        Guest.id += 1
        self.id = Guest.id

    def __str__(self):
        return f'{self.id}, {self.name}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Guest) and self.id == other.id


class Room:
    def __init__(self, name, price, max_guests):
        self.name = name
        self.price = price
        self.max_guests = max_guests
        self.guests = []

    def __str__(self):
        st = f'{self.name}, {self.price} NIS\n'
        if self.is_empty():
            st += '\tNo guests yet\n'
        else:
            for guest in self.guests:
                st += '\t' + str(guest) + '\n'
        return st

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Room) and \
            self.name == other.name and self.price == other.price

    def is_full(self):
        return len(self.guests) == self.max_guests

    def is_empty(self):
        return len(self.guests) == 0

    def has_guest(self, guest):
        return guest in self.guests

    def add_guest(self, guest):
        if self.is_full() or self.has_guest(guest):
            return False
        self.guests.append(guest)
        return True


class Hotel:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        self.rooms = []

    def __str__(self):
        st = f'{self.name} with {self.stars} stars, {self.count_guest()} guests\n'
        for room in self.rooms:
            st += str(room)
        return st

    def create_rooms(self, rooms_details):
        for item in rooms_details:
            self.rooms.append(Room(item[0], item[1], item[2]))

    def has_guest(self, guest):
        for room in self.rooms:
            if room.has_guest(guest):
                return True
        return False

    def book(self, guest, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room.add_guest(guest)
        return False

    def count_guest(self):
        guests_num = 0
        for room in self.rooms:
            guests_num += len(room.guests)
        return guests_num


def main():
    rooms_details = [
        ['Basic', 600, 3],
        ['Deluxe', 625.5, 2],
        ['Studio', 850.9, 4],
        ['Suite', 1280, 2]
    ]
    hotel = Hotel('Dan Eilat', 5)
    hotel.create_rooms(rooms_details)
    guests = ['Ron', 'Keren', 'Moshe', 'Yael', 'Taly', 'Kobi']
    for guest_name in guests:
        guest = Guest(guest_name)
        rnd_room = random.randint(0, len(rooms_details) - 1)
        room_name = rooms_details[rnd_room][0]
        if hotel.book(guest, room_name):
            print(f'Welcome {guest.name} to room {room_name}')
        else:
            print(f'We are sorry {guest.name} room {room_name} not available')
    print('\nHotel:')
    print(hotel)


if __name__ == '__main__':
    main()
