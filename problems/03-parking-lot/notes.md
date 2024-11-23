# Parking Lot
## Problem
Design a low-level system for a parking lot that satisfies the following requirements:
- The parking lot should have multiple entrances and exits.
- A global display board should show the number of free parking spots of all types.
- The parking lot should have different types of parking spots (mini, compact, and large) that allow parking for motorbikes, cars, and trucks, respectively.
- The parking lot should have multiple floors.
- The admin should be able to add and remove entrances and exits.
- The parking attendant should be able to create parking tickets.
- The parking lot should support different parking strategies like nearest first or farthest first on te basis of floor number and id of the parking spot.
- The parking lot should support different means of payment.

Please provide a detailed low-level design for the parking lot system that can handle the above requirements. 
You should consider how the parking lot will handle incoming and outgoing vehicles, track parking spots, generate and process parking tickets, and manage payments. 
Additionally, you should consider how the system will communicate with the display board and handle different parking strategies.

## Use-Case Diagram
```mermaid
graph TD  
    Admin --> |Add/Remove| EntrancesExits
      
    ParkingLot --> Entrances  
    ParkingLot --> Exits
    ParkingLot --> ParkingSpots  
    ParkingLot --> GlobalDisplayBoard  
      
    ParkingSpots --> Mini  
    ParkingSpots --> Compact  
    ParkingSpots --> Large  
      
    Mini --> Bike  
    Compact --> Car  
    Large --> Truck
    
```
```mermaid
graph TD
    System --> |Generate| GeneratingTickets  
    System --> |Update| UpdatingDisplayBoard  
    System --> |Manage| ManagePayments
    
    ParkingAttendant --> |Create| ParkingTickets  
```

## Class Diagram
### Enum Classes
```mermaid
classDiagram  
    class ParkingSpotType {  
        <<enumeration>>  
        COMPACT  
        MINI  
        LARGE  
        DEFAULT  
    }  
  
    class PaymentMode {  
        <<enumeration>>  
        CASH  
        CARD  
    }
```

### Core Classes
```mermaid
classDiagram  
    class Entrance {  
        -name: str  
    }  
  
    class Exit {  
        -name: str  
    }  
  
    class DisplayBoard {  
        -counter: defaultdict  
        +update(parking_spot_type: ParkingSpotType, change: int)  
    }
    class ParkingSpot {  
        <<abstract>>  
        -id: str  
        -floor_num: int  
        -cost: int  
        -available: bool  
    }  
  
    ParkingSpot <|-- CompactParkingSpot  
    ParkingSpot <|-- MiniParkingSpot  
    ParkingSpot <|-- LargeParkingSpot  
  
    class CompactParkingSpot {  
        +CompactParkingSpot(floor_num: int)  
    }  
  
    class MiniParkingSpot {  
        +MiniParkingSpot(floor_num: int)  
    }  
  
    class LargeParkingSpot {  
        +LargeParkingSpot(floor_num: int)  
    } 
    class ParkingLot {  
        -name: str  
        -entrances: List[Entrance]  
        -exits: List[Exit]  
        -display_board: DisplayBoard  
        -parking_spots: Dict[ParkingSpotType, List[ParkingSpot]]  
        +add_entrance(entrance: Entrance)  
        +add_exit(exit: Exit)  
        +remove_entrance(entrance: Entrance)  
        +remove_exit(exit: Exit)  
        +add_parking_spot(parking_spot: ParkingSpot, parking_spot_type: ParkingSpotType)
    }  
  
    ParkingLot --> Entrance  
    ParkingLot --> Exit  
    ParkingLot --> DisplayBoard  
    ParkingLot --> ParkingSpot
    
    class Account {  
        <<abstract>>  
        -name: str  
        -email: str  
        -password: str  
    }  
  
    Account <|-- Admin  
    Account <|-- ParkingAttendant  
  
    class Admin {  
        -parking_lot: ParkingLot  
        +Admin(name: str, email: str, password: str, parking_lot: ParkingLot)  
    }  
  
    class ParkingAttendant {  
        +ParkingAttendant(name: str, email: str, password: str)  
    }  
  
    Admin --> ParkingLot
```
### Vehicle Group and Parking Ticket
```mermaid
classDiagram  
    class Vehicle {  
        <<abstract>>  
        -id: str  
        -parking_spot_type: ParkingSpotType  
    }  
  
    Vehicle <|-- MotorBike  
    Vehicle <|-- Car  
    Vehicle <|-- Truck  
  
    class MotorBike {  
        +MotorBike(id: str)  
    }  
  
    class Car {  
        +Car(id: str)  
    }  
  
    class Truck {  
        +Truck(id: str)  
    }

    class ParkingTicket {  
        -id: str  
        -vehicle: Vehicle  
        -parking_spot: ParkingSpot  
        -timestamp: datetime  
        -parking_attendant: ParkingAttendant  
        +ParkingTicket(vehicle: Vehicle, parking_spot: ParkingSpot, parking_attendant: ParkingAttendant)  
    }  
  
    ParkingTicket --> Vehicle  
    ParkingTicket --> ParkingSpot  
    ParkingTicket --> ParkingAttendant  
```

### Parking Strategy Group
```mermaid
classDiagram  
    class ParkingStrategy {  
        <<abstract>>  
        +find_parking_spot(parking_lot: ParkingLot, parking_spot_type: ParkingSpotType)  
    }  
  
    ParkingStrategy <|-- NearestFirstParkingStrategy  
    ParkingStrategy <|-- FarthestFirstParkingStrategy  
  
    class NearestFirstParkingStrategy {  
        +find_parking_spot(parking_lot: ParkingLot, parking_spot_type: ParkingSpotType)  
    }  
  
    class FarthestFirstParkingStrategy {  
        +find_parking_spot(parking_lot: ParkingLot, parking_spot_type: ParkingSpotType)  
    }
```

### Services
```mermaid
classDiagram  
    class AdminService {  
        -admin: Admin  
        +add_entrance(name: str)  
        +add_exit(name: str)  
        +remove_entrance(entrance: Entrance)  
        +remove_exit(exit: Exit)  
    }  
  
    AdminService --> Admin  
    
    class ParkingAttendantService {  
        -parking_attendant: ParkingAttendant  
        +set_parking_attendant(parking_attendant: ParkingAttendant)  
        +create_parking_ticket(vehicle: Vehicle, parking_spot: ParkingSpot)  
    }  
  
    ParkingAttendantService --> ParkingAttendant  
    ParkingAttendantService --> ParkingTicket  

    class PaymentService {  
        +accept_cash(amount: int)  
        +accept_card(card_number: str, cvv: int, amount: int)  
    }  
  
    PaymentService --> Cash  
    PaymentService --> Card  
    
    class ParkingService {  
        -parking_lot: ParkingLot  
        -parking_strategy: ParkingStrategy  
        -parking_attendant_service: ParkingAttendantService  
        -payment_service: PaymentService  
        +entry(vehicle: Vehicle)  
        +exit(parking_ticket: ParkingTicket, vehicle: Vehicle)  
    }  
  
    ParkingService --> ParkingLot  
    ParkingService --> ParkingStrategy  
    ParkingService --> ParkingAttendantService  
    ParkingService --> PaymentService  
```

## Solving the Problem
- Set Up the Parking Lot:
  - Initialize ParkingLot, Entrance, Exit, DisplayBoard, and different types of ParkingSpot.
- Admin Operations:
  - Admin can add or remove entrances and exits using AdminService.
  - Admin can add parking spots to the parking lot.
- Vehicle Entry:
  - A vehicle arrives at the entrance.
  - Parking strategy (nearest or farthest first) finds an available parking spot.
  - Parking attendant creates a parking ticket.
  - Display board is updated to reflect the new status of parking spots.
- Vehicle Exit:
  - Vehicle presents the parking ticket.
  - System validates the ticket and the vehicle.
  - Parking spot is marked as available.
  - Display board is updated.
  - Payment is processed through PaymentService.
- Payment:
  - Payment can be made using cash or card.
  - PaymentService handles the payment transaction.
