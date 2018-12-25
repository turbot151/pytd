import td
import sys

def help():
    print("pytd add [message]")
    print("pytd print")

def td_print(lst: list):
    if not lst:
        print("To-do list is empty")
        return
    
    print("To-do list:")
    [print(f"==> {msg}") for msg in lst]

def main():
    args = sys.argv[1:]
    if not args:
        help()
        return
   
    td.init() 
    if args[0] == "add":
        msg = args[1]
        if not msg:
            print("Empty message")
        else:
            td.write(msg)
    elif args[0] == "print":
        td_print(td.read())
    else:
        help()

if __name__ == "__main__":
    main()
