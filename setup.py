import os
import subprocess
from src.utils import paths

# Step 0: Download conda
# subprocess.run(
#     "wget https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh", shell=True, check=True)

# Step 1: Setup SadTalker
subprocess.run(
    ["git", "clone", "https://github.com/Zz-ww/SadTalker-Video-Lip-Sync"])
os.chdir(paths.base_path / "SadTalker-Video-Lip-Sync")

# Define the commands
commands = [
    "gdown https://drive.google.com/uc\\?id\\=1TB0QWxiGtagEbdwDIpIVeQftKtDBj8Q5",
    "rm -rf checkpoints",
    "unzip checkpoints.zip",
    "rm checkpoints.zip",
]

# Execute the commands
for command in commands:
    subprocess.run(command, shell=True, check=True)

os.chdir(paths.base_path)


# Step 4: Clone the wav2lip-HD repository
subprocess.run(["git", "clone", "https://github.com/indianajson/wav2lip-HD"])
basePath = str(paths.base_path / "wav2lip-HD")
os.chdir(basePath)
wav2lipFolderName = 'Wav2Lip-master'
gfpganFolderName = 'GFPGAN-master'
wav2lipPath = basePath + '/' + wav2lipFolderName
gfpganPath = basePath + '/' + gfpganFolderName

# Step 5: Download additional files
subprocess.run(["wget", "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth",
               "-O", f"{wav2lipPath}/face_detection/detection/sfd/s3fd.pth"])
subprocess.run(["gdown", "https://drive.google.com/uc?id=1fQtBSYEyuai9MjBOF8j7zZ4oQ9W2N64q",
               "--output", f"{wav2lipPath}/checkpoints/"])
subprocess.run(["wget", "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth",
               "-P", f"{gfpganFolderName}/experiments/pretrained_models"])

# Step 6: Install requirements
os.chdir(basePath)
subprocess.run(["pip3", "install", "-r", "requirements.txt"])
subprocess.run(["pip3", "install", "-U", "librosa==0.8.1"])
subprocess.run(["mkdir", "inputs"])

# Step 7: Setup GFPGAN
os.chdir(gfpganFolderName)
subprocess.run(["python3", "setup.py", "develop"])

# Step 8: Clone basicsr repository
subprocess.run(["git", "clone", "https://github.com/Sanawar21/basicsr.git"])

# Step 9: Install facexlib
os.chdir(basePath)
subprocess.run(["pip3", "install", "facexlib"])


os.chdir(paths.base_path)
subprocess.run(["pip3", "install", "-r", "requirements.txt"])
