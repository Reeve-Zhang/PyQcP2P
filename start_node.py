
import requests
def get_public_ip(): 
    try: 
        response = requests.get('https://api.ipify.org') 
        if response.status_code == 200: 
            return response.text 
        else: 
            return "Error: Unable to retrieve public IP address" 
    except Exception as e: 
        return f"Error: {e}" 
public_ip = get_public_ip() 




from pythonp2p import Node
HOST = "0.0.0.0"
PORT = 9999
FILE_PORT = 65433
ip = ""
if __name__ == "__main__":
    print(f"Starting node on {public_ip}:{PORT}")
    node = Node(HOST, PORT, FILE_PORT, public_ip)  # start the node
    node.start()
    while True:
        action = input("Connect to Node: Enter C \n Send Message: Enter M \n Add File: Enter A \n Get File list: Enter F \n Get File: Enter G \n")
        if action == "C":
            ip = input("Enter IP: ")
            node.connect_to(ip, 9999)
        elif action == "M":
            message = input("Enter Message: ")
            node.send_message(message)
        elif action == "A":
            file = input("Enter File Path: ")
            print(node.addfile(file))
        elif action == "F":
            print(node.getfilelist())
        elif action == "G":
            print(node.getfilelist())
            file = input("Enter File Hash: ")
            print(node.requestFile(file))
