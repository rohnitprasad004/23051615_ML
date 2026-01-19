import os

folder_path = "textfiles"   # name of the folder where your .txt files are stored

for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)

        # Read text file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        print("="*40)
        print(f"📄 File: {file_name}")
        print(content)
        print("="*40)
