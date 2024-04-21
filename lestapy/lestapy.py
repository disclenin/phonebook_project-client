import socket

def main():
    host = 'localhost'
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        while True:
            print("\nOptions:")
            print("1. Add entry")
            print("2. Delete entry")
            print("3. Search entries")
            print("4. View entry")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '5':
                print("Exiting...")
                break

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            if choice == '1':
                phone_number = input("Enter phone number: ")
                note = input("Enter note: ")
                message = f"add {first_name} {last_name} {phone_number} {note}"
            elif choice == '2':
                message = f"delete {first_name} {last_name}"
            elif choice == '3':
                message = f"search {first_name} {last_name}"
            elif choice == '4':
                message = f"view {first_name} {last_name}"

            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print("Response from server:", response)

if __name__ == "__main__":
    main()

