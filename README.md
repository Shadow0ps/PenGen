![PenGen Logo](PenGen_logo.jpg)



## Description

PenGen V1 is part of a bigger project to build quick, easy tools to help get penetration testing projects off on the right foot quickly.
One of the biggest challenges in penetration testing is having adequate documentation that is organized and consistent. Developing processes can be difficult and following best practices is essential.
This project is aimed at helping those who wish to get a penetration testing engagement or Red Team engagement off the ground but lack the basic file/folder structures or those who wish to create a simple and repeatable folder base project structure and pull their templates or community templates into that folder structure.

The script asks some simple questions and then performs some very simple tasks.
Questions can be modified to suit your needs.
Folder structures and files can be customized to your needs and only the necessary folders and files are ever copied for the specified projects.

Pull requests are welcome. 
Complaints are not. 

If you don't like it, don't use it. 

If you do like it then please feel free to modify it and share your own folders/files/templates with the community.

This isn't meant to be the end all be all of pentest reporting tools. It's here to help keep you organized and get your project off to a quick start.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Describe how to install and set up the project. Include any prerequisites, dependencies, or configuration steps necessary.

```bash
# Example installation commands
git clone https://github.com/Shadow0ps/PenGen.git
cd PenGen
```

## Usage

Provide examples or instructions on how to use the project. Include code snippets, screenshots, or command-line examples if applicable.

```python
# Example usage code
python pen_gen.py
```

Follow the prompts like the example below:

```
    ______          _____              _   _               _               __  
    | ___ \        |  __ \            | | | |             (_)             /  | 
    | |_/ /__ _ __ | |  \/ ___ _ __   | | | | ___ _ __ ___ _  ___  _ __   `| | 
    |  __/ _ \ '_ \| | __ / _ \ '_ \  | | | |/ _ \ '__/ __| |/ _ \| '_ \   | | 
    | | |  __/ | | | |_\ \  __/ | | | \ \_/ /  __/ |  \__ \ | (_) | | | | _| |_
    \_|  \___|_| |_|\____/\___|_| |_|  \___/ \___|_|  |___/_|\___/|_| |_| \___/
                                                                                                        
                                                                                                        
    
Developed by Shadow0pz and CONDITION.BLACK
Copyright (c) 2024
Free To Use or Modify.

Enter the name of the project: Acme Pentest Project
Enter the customer's name: Acme Co. , Inc.
Enter the end date of the project (YYYY-MM-DD): 2024-03-01
Enter the deliverable of the project: Penetration Testing Report
Have you collected the scoping document? (yes/no): yes
Have you collected the authorization and signed SOW? (yes/no): yes
Select the type of penetration testing:
1. Application Penetration Test
2. Network Penetration Test
3. Cloud Security Penetration Test
4. Red Team Testing
5. Social Engineering Testing
6. Kubernetes Penetration Testing
Enter your choice (number): 3
Select the subtype for Cloud Security Penetration Test:
1. AWS
2. Azure
3. Google_Cloud
4. Alibaba_Cloud
5. Rackspace
6. CoreWeave
7. Lambda
8. NVidia
Enter your choice (number): 6
Enter the target directory path (leave blank for current directory): ./project1/
Folders and subfolders created successfully.
```

Additional Features:

You can override the default folder structure and provide your own by changing the rename_me_folder_generation_list.txt contents (instructions inside the file)
*Be sure to change the name of the file when you are done to folder_generation_list.txt and leave it in the root folder of the project.
** If you don't want to modify the folder structure in and just want to use the predefined ones in the script then just leave this file alone.

You can choose what files you wish to copy and where you wish to copy them to by modifying the file_target_list.txt (instructions inside the file)
This is a critical feature of this tool as it enables you to easily copy files of any type from a source folder into the corresponding folders you wish to have them in.
This ensures that the files you need are in the place you expect them to be in from the beginning without always having to copy a whole folder structure over or worse
risk copying files from an old project to a new one and exposing customer data. You can define ANY file type including executables, license files, report templates, etc.
*There is an optional sample file generator I included in the project called demo_file_gen.py which should be pretty self explanatory. You can use this to generate sample files.
**Feel free to extend this to suit your needs and be sure to share your tooling and examples here so we can improve the experience for everyone.



## Contributing

If you have a feature request please be specific about what it is and try to do it yourself if you can. If not then I'll do my best to help.
If you find a bug then please submit a pull request. This uses Python Native libraries only so it should be relatively bug free.
If you want to contribute then please be sure to submit well commented code along with an explanation of what the code does and why you feel it's helpful.
For contributions regarding file/folder/project structure please be as detailed as possible with the structure and why you feel it's helpful to others.

## License

This is licensed under the Unlicense. Do with it what you want but as with all things please be responsible and give credit where credit is due.
I'm a big proponent of the community and appreciate the contributions of others a great deal. Credit will always be given below to major contributors.
I can be found on X (Twitter) as @Shadow0pz
I hope you'll find this useful.
