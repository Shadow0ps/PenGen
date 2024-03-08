## This script prompts the user to enter the target directory path where the sample files will be generated. 
## It then creates ten sample text files (`target_file1.txt` to `target_file10.txt`) within the specified directory. 
## Each file contains basic information such as the filename and a sample content message.
## For simplicity sake these are txt files but you can generate anything you want by modifying the script accordingly.
## Eventually I will probably provide some docx templates. Feel free to submit your own.
import os

def generate_sample_files(target_directory):
    """Generate sample files with basic information."""
    try:
        # Create the target directory if it doesn't exist
        os.makedirs(target_directory, exist_ok=True)
        
        # Generate sample files with basic information
        for i in range(1, 11):
            filename = f"target_file{i}.txt"
            filepath = os.path.join(target_directory, filename)
            with open(filepath, "w") as file:
                file.write(f"Sample content for {filename}\n")
                file.write("This is a sample file generated for demonstration purposes.\n")
                file.write("You can customize the content as needed.\n")
                file.write(f"File number: {i}\n")
            print(f"Sample file generated: {filepath}")
    except OSError as e:
        print(f"Error: {e}")

def main():
    target_directory = input("Enter the target directory path to generate sample files: ").strip()
    generate_sample_files(target_directory)

if __name__ == "__main__":
    main()

