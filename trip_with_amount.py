from django_saga import saga

trip_planning_state = "Planning"
car_booking_state = "Not Booked"
room_booking_state = "Not Booked"
flight_booking_state = "Not Booked"
total_amount = 0

print("\n============ Trip Planing Current state ==================\n")
print(trip_planning_state)
print(f"Total Amount = {total_amount} \n")


def book_car():
    global car_booking_state
    amount = 0
    car_booking_state = "Car Booked"
    # trip_booking_state = "Car Booked"
    print("\n=========== book car ================\n")
    print(car_booking_state)
    pay = 500
    amount += pay
    print(f"Car booking charge = {pay}")
    print(f"Amount = {amount}")
    return {"amount": amount}


def book_room(amount):
    global room_booking_state
    room_booking_state = "Room Booked"
    pay = 1500
    amount += pay
    print("\n=========== book room ================\n")
    print(room_booking_state)
    print(f"Room booking charge = {pay}")
    print(f"Amount = {amount}")
    return {"amount": amount}


def book_flight(amount):
    print("\n=========== book flight ================\n")
    global trip_planning_state, flight_booking_state, total_amount
    pay = 10000
    amount += pay
    total_amount = amount
    flight_booking_state = "Flight Booked"
    trip_planning_state = "Trip planed"
    print(flight_booking_state)
    print(f"Flight booking charge = {pay}")
    print(f"Amount = {amount}")


def cancel_car(amount):
    global car_booking_state
    pay = 500
    amount -= pay
    car_booking_state = "Car Cancelled"
    print("\n=========== cancel car ================\n")
    print(car_booking_state)
    print(f"Car booking charge = {pay}")
    print(f"Amount = {amount}")


def cancel_room(amount):
    global room_booking_state
    pay = 1500
    amount -= pay
    room_booking_state = "Room Cancelled"
    print("\n=========== cancel room ================\n")
    print(room_booking_state)
    print(f"Room booking charge = {pay}")
    print(f"Amount = {amount}")


def cancel_flight(amount):
    global trip_planning_state, flight_booking_state
    pay = 10000
    amount -= pay
    flight_booking_state = "Room Cancelled"
    trip_planning_state = "Trip not planed"
    print("\n=========== cancel flight ================\n")
    print(flight_booking_state)
    print(f"Flight booking charge = {pay}")
    print(f"Amount = {amount}")


try:
    saga.SagaBuilder.create() \
        .action(book_car, cancel_car) \
        .action(book_room, cancel_room) \
        .action(book_flight, cancel_flight) \
        .build() \
        .execute()
except:
    pass

print("\n============ Trip Planing Current state ==================\n")
print(trip_planning_state)
print(f"Total Amount = {total_amount} \n")
