import os
import subprocess

# Path to the folder where your .drawio files are located
drawio_folder = r"C:\Users\muham\Downloads\FYP-Memorial\Requester\Requester"

# Path to the draw.io executable
drawio_executable = r"C:\Program Files\draw.io\draw.io.exe"

# Loop through all files in the directory
for filename in os.listdir(drawio_folder):
    if filename.endswith(".drawio"):
        input_file = os.path.join(drawio_folder, filename)
        output_file = os.path.join(drawio_folder, os.path.splitext(filename)[0] + ".png")

        # Call draw.io to export the file to PNG
        subprocess.run([drawio_executable, "--export", "--format", "png", "--output", output_file, input_file])

print("Conversion completed!")
