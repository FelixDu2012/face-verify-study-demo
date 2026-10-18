import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def upload_face_image():
    target_file = "face.png"
    if os.path.exists(target_file):
        while True:
            print("Find face.png, do you want to reupload it? (y/n)")
            choice = input().strip().lower()
            if choice == "y":
                print("Reuploading...")
                break
            elif choice == "n":
                print("not reuploading.")
                return False
            else:
                print("invalid input, please enter y or n")
    else:
        print("face.png does not exist, start upload.")
    root = Tk()
    root.withdraw()
    while True:
        file_path = askopenfilename(title="Select image file")
        if not file_path:
            print("No file selected, try again.")
            continue
        if not os.path.isfile(file_path):
            print("File not found, please reselect.")
            continue
        try:
            if os.path.exists(target_file):
                os.remove(target_file)
            ext = os.path.splitext(file_path)[1].lower()
            if ext == ".png":
                with open(file_path, "rb") as f_src, open(target_file, "wb") as f_dst:
                    f_dst.write(f_src.read())
            else:
                img = Image.open(file_path)
                img.save(target_file, format="PNG")
            print("Upload success")
            return True
        except Exception as e:
            print(f"Failed to process file: {e}, please choose another image.")

if __name__ == "__main__":
    upload_face_image()
