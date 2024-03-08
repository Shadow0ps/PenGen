import os
from datetime import datetime

def create_folders(test, subtype, target_directory):
    """Create folders and subfolders based on the provided structure."""
    folder_structure = {
        "Application Penetration Test": [
            "Scoping_Documents",
            "Reconnaissance",
            "Vulnerability_Assessment",
            "Exploitation",
            "Post_Exploitation",
            "Reports/Draft",
            "Reports/Final",
            "Screenshots"
        ],
        "Network Penetration Test": [
            "Internal",
            "External"
        ],
        "Cloud Security Penetration Test": [
            "Scoping_Documents",
            "Reconnaissance",
            "Vulnerability_Assessment",
            "Exploitation",
            "Post_Exploitation",
            "Reports/Draft",
            "Reports/Final",
            "Screenshots"
        ],
        "Red Team Testing": [
            "Scenario_Planning",
            "Execution",
            "Reports/Draft",
            "Reports/Final"
        ],
        "Social Engineering Testing": [
            "Phishing_Campaigns",
            "Physical_Social_Engineering",
            "Reports/Draft",
            "Reports/Final"
        ],
        "Kubernetes Penetration Testing": [
            "Scoping_Documents",
            "Reconnaissance",
            "Vulnerability_Assessment",
            "Exploitation",
            "Post_Exploitation",
            "Reports/Draft",
            "Reports/Final",
            "Screenshots"
        ]
    }
    
    selected_folders = folder_structure.get(test, [])
    if not selected_folders:
        print(f"No folder structure defined for {test}.")
        return
    
    # Create target directory if it doesn't exist
    os.makedirs(target_directory, exist_ok=True)
    
    # Create folders and subfolders
    test_folder = os.path.join(target_directory, test.replace(" ", "_"))
    os.makedirs(test_folder, exist_ok=True)
    if subtype:
        subtype_folder = os.path.join(test_folder, subtype.replace(" ", "_"))
        os.makedirs(subtype_folder, exist_ok=True)
        for folder in selected_folders:
            folder_path = os.path.join(subtype_folder, folder)
            os.makedirs(folder_path, exist_ok=True)
    else:
        for folder in selected_folders:
            folder_path = os.path.join(test_folder, folder)
            os.makedirs(folder_path, exist_ok=True)
    print("Folders and subfolders created successfully.")

def print_banner():
    """Print ASCII banner."""
    banner = r"""
    ______          _____              _   _               _               __  
    | ___ \        |  __ \            | | | |             (_)             /  | 
    | |_/ /__ _ __ | |  \/ ___ _ __   | | | | ___ _ __ ___ _  ___  _ __   `| | 
    |  __/ _ \ '_ \| | __ / _ \ '_ \  | | | |/ _ \ '__/ __| |/ _ \| '_ \   | | 
    | | |  __/ | | | |_\ \  __/ | | | \ \_/ /  __/ |  \__ \ | (_) | | | | _| |_
    \_|  \___|_| |_|\____/\___|_| |_|  \___/ \___|_|  |___/_|\___/|_| |_| \___/
                                                                                                        
                                                                                                        
    """
    credits = "Developed by Shadow0pz and CONDITION.BLACK\nCopyright (c) 2024\nFree To Use or Modify."
    print(banner)
    print(credits)
    print()

def prompt_user_for_tests():
    """Prompt the user to select the type(s) of penetration testing."""
    tests = [
        "Application Penetration Test",
        "Network Penetration Test",
        "Cloud Security Penetration Test",
        "Red Team Testing",
        "Social Engineering Testing",
        "Kubernetes Penetration Testing"
    ]
    print("Select the type of penetration testing:")
    for i, test in enumerate(tests, start=1):
        print(f"{i}. {test}")
    while True:
        try:
            choice = input("Enter your choice (number): ")
            index = int(choice) - 1
            if 0 <= index < len(tests):
                return tests[index]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def prompt_user_for_subtype(test):
    """Prompt the user to select the subtype for the specified test."""
    subtypes = {
        "Network Penetration Test": [
            "Internal",
            "External"
        ],
        "Cloud Security Penetration Test": [
            "AWS",
            "Azure",
            "Google_Cloud",
            "Alibaba_Cloud",
            "Rackspace",
            "CoreWeave",
            "Lambda",
            "NVidia"
        ]
    }
    if test in subtypes:
        print(f"Select the subtype for {test}:")
        for i, subtype in enumerate(subtypes[test], start=1):
            print(f"{i}. {subtype}")
        while True:
            try:
                choice = input("Enter your choice (number): ")
                index = int(choice) - 1
                if 0 <= index < len(subtypes[test]):
                    return subtypes[test][index]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print(f"No subtypes defined for {test}.")
        return None

def main():
    # Print ASCII banner
    print_banner()
    
    # Prompt user for project details
    project_name = input("Enter the name of the project: ")
    customer = input("Enter the customer's name: ")
    start_date = datetime.now()
    end_date = input("Enter the end date of the project (YYYY-MM-DD): ")
    deliverable = input("Enter the deliverable of the project: ")
    scoping_document_collected = input("Have you collected the scoping document? (yes/no): ")
    authorization_collected = input("Have you collected the authorization and signed SOW? (yes/no): ")
    
    # Prompt user to select the type(s) of penetration testing
    test = prompt_user_for_tests()
    
    # Prompt user to select the subtype (if applicable)
    subtype = None
    if test in ["Network Penetration Test", "Cloud Security Penetration Test"]:
        subtype = prompt_user_for_subtype(test)
    
    # Set target directory
    target_directory = input("Enter the target directory path (leave blank for current directory): ").strip()
    if not target_directory:
        target_directory = os.getcwd()
    
    # Create folders and subfolders based on the selected test type and subtype
    create_folders(test, subtype, target_directory)

if __name__ == "__main__":
    main()