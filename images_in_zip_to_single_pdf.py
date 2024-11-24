import os
import shutil
from tkinter import Tk, filedialog
from PIL import Image
from zipfile import ZipFile


def convert_img_to_pdf_in_folder(folder_path):
    output_folder = os.path.join(folder_path, "pdf")
    done_folder = os.path.join(folder_path, "zip")
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(done_folder, exist_ok=True)

    zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip')]

    if not zip_files:
        print("There are no ZIP files in the specified folder.")
        return

    supported_extensions = ('.jpg', '.jpeg', '.bmp', '.png', '.webp')

    for zip_file_name in zip_files:
        zip_file_path = os.path.join(folder_path, zip_file_name)
        base_name = os.path.splitext(zip_file_name)[0]
        output_pdf_path = os.path.join(output_folder, f"{base_name}.pdf")

        print(f"ZIP file in process: {zip_file_name}")

        try:
            with ZipFile(zip_file_path, 'r') as zip_file:
                img_files = sorted(
                    [f for f in zip_file.namelist() if f.lower().endswith(
                        supported_extensions)],
                    key=lambda x: int(os.path.splitext(os.path.basename(x))[0])
                )

                images = []
                total_files = len(img_files)
                for idx, img_file in enumerate(img_files, start=1):
                    print(
                        f"  - Image file in process: {idx:03}/{total_files:03}\r", end="")
                    with zip_file.open(img_file) as file:
                        img = Image.open(file)
                        images.append(img.convert("RGB"))
                print("")

                if images:
                    first_image = images[0]
                    first_image.save(
                        output_pdf_path,
                        save_all=True,
                        append_images=images[1:]
                    )
                    print(f"  -> Created PDF: {output_pdf_path}")
                else:
                    print("  -> Image files not found. Skipping.")
                    continue

            shutil.move(zip_file_path, os.path.join(
                done_folder, zip_file_name))
            print(
                f"  -> ZIP file has been moved: {os.path.join(done_folder, zip_file_name)}")

        except Exception as e:
            print(f"  -> An error has occurred: {e}")
            continue


def main():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    folder_path = filedialog.askdirectory(title="Please select a directory.")

    if folder_path:
        try:
            convert_img_to_pdf_in_folder(folder_path)
        except Exception as e:
            print(f"An error has occurred: {e}")
    else:
        print("Directory not selected.")


if __name__ == "__main__":
    main()
