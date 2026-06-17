#overwritter
#developer: brazil_502
#version: 1.1

import os

# ANSI escape codes
GREEN = '\033[92m'
RESET = '\033[0m'

def display_status():
    print(f"\n{GREEN}--- Current Directory: {os.getcwd()} ---{RESET}")
    print(f"{GREEN}Contents:{RESET}", os.listdir())

def manager():
    print(f"{GREEN}--- File Manager & Overwriter ---{RESET}")
    
    while True:
        display_status()
        command = input(f"\n{GREEN}Commands: [cd] change, [ls] list, [view] read, [edit] overwrite, [exit] quit{RESET}\n> ").strip().lower()

        if command == 'cd':
            new_path = input(f"{GREEN}Enter path: {RESET}")
            try:
                os.chdir(new_path)
            except Exception as e:
                print(f"{GREEN}Error: {e}{RESET}")

        elif command == 'view':
            filename = input(f"{GREEN}Enter filename to view: {RESET}")
            if os.path.exists(filename):
                try:
                    with open(filename, 'r') as f:
                        print(f"\n--- {filename} Contents ---")
                        print(f.read())
                        print("-" * (len(filename) + 16))
                except Exception as e:
                    print(f"{GREEN}Could not read file: {e}{RESET}")
            else:
                print(f"{GREEN}File not found.{RESET}")

        elif command == 'edit':
            filename = input(f"{GREEN}Enter filename to overwrite: {RESET}")
            if os.path.exists(filename):
                new_content = input(f"{GREEN}Enter new content: {RESET}")
                with open(filename, 'w') as f:
                    f.write(new_content)
                print(f"{GREEN}Success!{RESET}")
            else:
                print(f"{GREEN}File not found.{RESET}")

        elif command == 'exit':
            break

if __name__ == "__main__":
    manager()
