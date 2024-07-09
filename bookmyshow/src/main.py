from datetime import datetime, date
from typing import List
from enum import Enum


class BMSService:
    def __init__(self):
        self.cinema_halls: List[CinemaHall] = []

    def get_movies(self, date: datetime, city: str):
        return []

    def get_cinema_halls(self, city: str):
        return self.cinema_halls


class CinemaHall:
    def __init__(self, id: str, name: str, address: str):
        self.id: str = id
        self.name: str = name
        self.address: str = address
        self.auditoriums: List[Auditorium] = []

    def get_movies(self, dates: List[datetime]) -> dict:
        return {}

    def get_shows(self, dates: List[datetime]) -> dict:
        return {}


class Address:
    def __init__(self, pincode: str, street: str, city: str, state: str, country: str):
        self.pincode: str = pincode
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.country: str = country


class Auditorium:
    def __init__(self, id: str, name: str):
        self.id: str = id
        self.name: str = name
        self.shows: List[Show] = []


class Show:
    def __init__(self, id, movie, start_time, end_time):
        self.id = id
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.seats: List[Seat] = []


class SeatType(Enum):
    DELUXE = 'DELUXE'
    VIP = 'VIP'
    ECONOMY = 'ECONOMY'
    OTEHR = 'OTHER'


class SeatStatus(Enum):
    BOOKED = 'BOOKED'
    AVAILABLE = 'AVAILABLE'


class Seat:
    def __init__(self, id: str, type: SeatType, status: SeatStatus):
        self.id: str = id
        self.type: SeatType = type
        self.status: SeatStatus = status


class Genre(Enum):
    HORROR = 'HORROR'
    ACTION = 'ACTION'
    ROMANTIC = 'ROMANTIC'
    SCI_FI = 'SCI_FI'
    OTHER = 'OTHER'


class Movie:
    def __init__(self, id: str, name: str, duration: int, language: str, release_date: date, genre: Genre):
        self.id: str = id
        self.name: str = name
        self.duration: int = duration
        self.language: str = language
        self.release_date: date = release_date
        self.genre: Genre = genre


class User:
    def __init__(self, id: str):
        self.id = id


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class SystemMember(User):
    def __init__(self, id: id, account, name: str, email: str, address: Address):
        super().__init__(id)
        self.account = account
        self.name = name
        self.email = email
        self.address = address


class BookingStatus(Enum):
    REQUESTED = 'REQUESTED'
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'


class PaymentStatus(Enum):
    REQUESTED = 'REQUESTED'
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    DECLINED = 'DECLINED'


class Payment:
    def __init__(self, amount: float, date: datetime, transaction_id: str, payment_status: PaymentStatus):
        self.amount = amount
        self.date = date
        self.transaction_id = transaction_id
        self.payment_status = payment_status


class Booking:
    def __init__(self, id: str, date: datetime, show: Show, auditorium: Auditorium, cinema_hall: CinemaHall,
                 booking_status: BookingStatus, amount: float, seats: List[Seat], payment):
        self.id = id
        self.date = date
        self.member = None
        self.show = show
        self.auditorium = auditorium
        self.cinema_hall = cinema_hall
        self.booking_status = booking_status
        self.amount = amount
        self.seats = seats
        self.payment = payment

    def set_member(self, member):
        self.member = member


class Member(SystemMember):
    def __init__(self, id):
        super().__init__(id)
        self.bookings = []

    def make_booking(self, booking: Booking):
        booking.set_member(self)
        pass

    def get_booking(self) -> List[Booking]:
        return self.bookings


class Admin(SystemMember):
    def add_movie(self, movie: Movie):
        pass

    def add_show(self, show: Show):
        pass


class Search:
    def search_movies_by_name(self, name: str):
        pass

    def search_movies_by_genre(self, genre: Genre):
        pass

    def search_movies_by_language(self, language: str):
        pass

    def search_movies_by_date(self, date: datetime):
        pass
