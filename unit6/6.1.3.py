import tkinter as tk
from PIL import ImageTk, Image

def show_image():
    # Open and display the image
    image_path = r"C:\Users\Liam\PycharmProjects\pythonProject\venv\next_course\dog.jpg"
    image = Image.open(image_path)
    image.show()

def main():
    """Main function to run the program."""
    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Image Viewer")

    # Set the window size
    window.geometry("400x200")

    # Create a label with the question text
    question_label = tk.Label(window, text="Who is man's best friend?")
    question_label.pack()

    # Create a button to show the image
    button = tk.Button(window, text="Show Image", command=show_image)
    button.pack()

    # Run the main window loop
    window.mainloop()


if __name__ == '__main__':
    main()