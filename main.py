import os

print("Welcome to Face Authentication System")
print("1. Capture Face")
print("2. Train Model")
print("3. Authenticate")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    script_path = r'C:\Users\Archents1\Desktop\face recognition\src\captureface.py'
    os.system(f'python "{script_path}"')
    # os.system("C:\\Users\\Archents1\\Desktop\\face recognition\\src\\captureface.py")
elif choice == "2":
    script_path = r'C:\Users\Archents1\Desktop\face recognition\src\trainface.py'
    os.system(f'python "{script_path}"')
elif choice == "3":
    script_path = r'C:\Users\Archents1\Desktop\face recognition\src\auth.py'
    os.system(f'python "{script_path}"')
else:
    print("Invalid choice! Exiting.")
