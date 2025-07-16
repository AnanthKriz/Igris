import os
import time
import shutil
import tempfile
import platform
from pathlib import Path

# ==== CONFIG ====
MELT_DELAY = 5  # Seconds before self-delete
FAKE_PAYLOAD_NAME = "ghost_payload.tmp"

# ==== PAYLOAD SIMULATION ====
def run_payload():
    print(">> Executing in-memory payload...")
    temp_dir = tempfile.mkdtemp()
    fake_file = os.path.join(temp_dir, FAKE_PAYLOAD_NAME)
    with open(fake_file, "w") as f:
        f.write("This is fake RAM data. Do not save.")
    print(f">> Temporary file created at: {fake_file}")
    return temp_dir

# ==== HISTORY & TRACE CLEANER ====
def clean_history():
    print(">> Cleaning forensic traces...")
    user_home = str(Path.home())

    # Common shell histories
    histories = [
        os.path.join(user_home, ".bash_history"),
        os.path.join(user_home, ".zsh_history"),
        os.path.join(user_home, ".python_history")
    ]

    # Windows PowerShell history
    if platform.system() == "Windows":
        ps_history = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "Windows", "PowerShell", "PSReadLine", "ConsoleHost_history.txt")
        histories.append(ps_history)

    for hist in histories:
        try:
            if os.path.exists(hist):
                with open(hist, "w") as f:
                    f.write("# Oblivion: Trace Cleared\n")
                print(f">> Wiped: {hist}")
        except Exception as e:
            print(f">> Failed to wipe {hist}: {e}")

# ==== SELF-DELETE ====
def melt_self():
    print(f">> Melting in {MELT_DELAY} seconds...")
    time.sleep(MELT_DELAY)
    try:
        this_file = os.path.realpath(__file__)
        print(f">> Deleting self: {this_file}")
        os.remove(this_file)
    except Exception as e:
        print(f">> Melt failed: {e}")

# ==== MAIN ENTRY ====
if __name__ == "__main__":
    print("\n[ OBLIVION.EXE :: DEPLOYED ]")
    temp_path = run_payload()
    clean_history()
    try:
        shutil.rmtree(temp_path)
        print(f">> Removed temp directory: {temp_path}")
    except Exception as e:
        print(f">> Failed to clean temp folder: {e}")
    melt_self()
    print(">> Vanished. No trace left.\n")
