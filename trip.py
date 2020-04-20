from django_saga import saga

trip_planning_state = "Planning"
car_booking_state = "Not Booked"
room_booking_state = "Not Booked"
flight_booking_state = "Not Booked"

print("\n============ Trip Planing Current state ==================\n")
print(trip_planning_state)


def book_car():
    global car_booking_state
    car_booking_state = "Car Booked"
    print("\n=========== book car ================\n")
    print(car_booking_state)


def book_room():
    global room_booking_state
    room_booking_state = "Room Booked"
    print("\n=========== book room ================\n")
    print(room_booking_state)


def book_flight():
    global trip_planning_state, flight_booking_state
    flight_booking_state = "Flight Booked"
    trip_planning_state = "Trip planed"
    print("\n=========== book flight ================\n")
    print(flight_booking_state)


def cancel_car():
    global car_booking_state
    car_booking_state = "Car Cancelled"
    print("\n=========== cancel car ================\n")
    print(car_booking_state)


def cancel_room():
    global room_booking_state
    room_booking_state = "Room Cancelled"
    print("\n=========== cancel room ================\n")
    print(room_booking_state)


def cancel_flight():
    global trip_planning_state, flight_booking_state
    flight_booking_state = "Flight Cancelled"
    trip_planning_state = "Trip not planed"
    print("\n=========== cancel flight ================\n")
    print(flight_booking_state)

try:
    saga.SagaBuilder.create().action(lambda: book_car(), lambda: cancel_car()) \
        .action(lambda: book_room(), lambda: cancel_room()) \
        .action(lambda: book_flight(), lambda: cancel_flight()) \
        .build() \
        .execute()
except:
    pass

print("\n============ Trip Planing Current state ==================\n")
print(trip_planning_state, "\n")
