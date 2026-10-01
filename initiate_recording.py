import sys
import subprocess

def initiate_memory_recording():
    # Use python implementation provided by framework
    try:
        from python_tools.tools import initiate_memory_recording
    except ImportError:
        print("Failed to import initiate_memory_recording")
        return
    initiate_memory_recording()
    print("Successfully initiated memory recording")

if __name__ == "__main__":
    initiate_memory_recording()
