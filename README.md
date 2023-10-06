# File Creator

### About Me 

My name is Hadrian Hu and I am a SIL SIE at General Motors, Canada. I created this application to save time when creating file extension types outside of the regular Windows context menu, since development often requires more than ```.txt``` files. I hope you find this application useful and if you have any questions, please feel free to reach out to me at ```hadrian.hu@gmail.com```. 

## Overview

File Creator is a simple yet powerful utility that allows users to quickly create files with any desired extension. With the rise of various file types and the need to quickly scaffold out new files, there was a distinct need for a tool that streamlines the file creation process, eliminating the repetitive task of navigating through file explorers and manually defining extensions.

**Why was it created?**
In many professions and tasks, users find themselves repeatedly creating files of specific types. This manual process can be tedious and error-prone, especially when dealing with multiple file extensions. File Creator seeks to address this problem, providing an intuitive interface to define and create files efficiently.

**Motivation**
The motivation behind File Creator stems from personal experiences and the broader community's feedback. We identified a repetitive task that could be optimized and aimed to create a solution that boosts productivity and ensures consistency in file creation.

## Installation

### Prerequisites

- Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org/downloads/).
- It's recommended to have `pip` installed. It usually comes with the Python installation.

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your_username/file-creator.git
   cd file-creator
   ```
2. **Install the dependencies:**

    ```
    pip install -r requirements.txt
    ```

    Note: The above step assumes you have a `requirements.txt` file. If not, install necessary libraries as required.

3. **Generate Executable** :

    If you wish to generate a standalone executable:

   First, install `PyInstaller`:

    ```
    pip install pyinstaller
    ```

    **Generate the executable:** 

    ```
    pyinstaller --onefile your_script_name.py 
    ```
    
4. **Run the application:**
   
   If using the python script: 

   ```
   python ./src/CreateNewFile.py
   ```

    If using the executable:

    ```./dist/CreateNewFile.exe
    ./dist/CreatNewFile.exe
    ```

### Contribution 

We welcome contributions from the community. Please refer to the [contributing guidelines](CONTRIBUTING.md) for more details. The repo is located at <https://github.com/hadrianhu888/CreateNewFile.git>
