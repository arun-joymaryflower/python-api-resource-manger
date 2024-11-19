import requests
import json

base_url = 'https://jsonplaceholder.typicode.com/posts'


def list_vms():
    response = requests.get(base_url)
    if response.status_code ==200:
        vms = response.json()
        for vm in vms[:25]:
            print(f"ID: {vm['id']}, Title: {vm['title']}")
        else:
            print("Not able to list virtual machines. Error: ", response.status_code)


def create_vm():
    title = input("Enter the title of the virtual machine: ")
    body = input("Enter the description: ")
    data = {"title":title, "body":body, "userID":1}
    response = requests.post(base_url, json=data)
    if response.status_code ==201:
        vm =response.json()
        print("New virtual machine created")
        print(f"ID: {vm['id']}, Title: {vm['title']}, Description: {vm['body']}")
    else:
        print("Failed to create the virtual machine! Error: ", response.status_code)


def update_vm():
    vm_id = input("Enter the id of the virtual machine to be updated: ")
    new_title = input ("Enter the new title of the virtual machine: ")
    new_body =  input("Enter the new description of the virtual machine: ")
    data ={"title": new_title, "body":new_body, "userID":1}
    response = requests.put(f"{base_url}/{vm_id}", json= data)
    if response.status_code == 200:
        vm=response.json
        print("Virtual machine updated")
        print(f"ID: {vm_id}, Title{vm['title']}, Description: {vm['body']}")
    else:
        print("Failed to update the virtual machine! Error: ", response.status_code)


def delete_vm():
    vm_id = input("Enter the id of the virtual machine you want to delete: ")
    response = requests.delete(f"{base_url}/{vm_id}")
    if response.status_code == 200:
        print(f"The virtual machine with ID {vm_id} is deleted")
    else:
        print("Unable to delete the virtual machine! Error: ", response.status_code)


def main():
    while True:
        print("/// CLOUD API RESOURCE MANAGER ///")
        print("1. List virtual machines")
        print("2. Create a new virtual machine")
        print("3. Modify an existing virtual machine")
        print("4. Delete a virtual machine")
        choice = input("Enter your choice:")
        if choice == "1":
            list_vms()
        elif choice == "2":
            create_vm()
        elif choice =="3":
            update_vm()
        elif choice== "4":
            delete_vm()
        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()






