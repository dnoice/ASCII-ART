#!/bin/bash

# Function to display error messages
error_exit() {
    echo "❌ Error: $1"
    exit 1
}

# Install Python3 and pip
echo "🔄 Installing Python3 and pip..."
sudo apt update || error_exit "Failed to update package lists."
sudo apt install -y python3 python3-pip || error_exit "Failed to install Python3 or pip."

# Install dependencies from requirements.txt
if [ -f "./src/requirements.txt" ]; then
    echo "🔄 Installing dependencies from requirements.txt..."
    pip3 install -r ./src/requirements.txt || error_exit "Failed to install required dependencies."
else
    error_exit "requirements.txt not found in ./src/."
fi

# Move `main.sh` to the current working directory
if [ -f "./src/main.sh" ]; then
    echo "🔄 Moving 'main.sh' to the current directory..."
    mv ./src/main.sh ./ || error_exit "Failed to move 'main.sh'."
else
    error_exit "'main.sh' not found in ./src/."
fi

echo "✅ Installation complete. Run './main.sh' to begin."
exit 0
