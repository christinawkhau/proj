import os
import sys

def run_command(command):
    print(f"\n🔧 Running: {command}\n")
    os.system(f"python manage.py {command}")
    print("\n✅ Done.\n")

def main():
    while True:
        print("=== Django Product Data Manager ===")
        print("1. Download product data from DummyJSON")
        print("2. Filter and clean downloaded data")
        print("3. Import filtered data into the database")
        print("4. Export product data from the database")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            run_command("download_products")
        elif choice == "2":
            run_command("filter_products")
        elif choice == "3":
            run_command("import_products")
        elif choice == "4":
            run_command("export_products")
        elif choice == "5":
            print("👋 Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
