# valorant-stretched-resolution

A Python tool to enable stretched resolution in Valorant via command line.

## Features
- Set a custom stretched resolution for Valorant.
- Works across Windows systems.
- No need to modify game files manually.
- Can be installed and run as a pip package.
- Supports command-line interface for easy configuration.

## Prerequisites
- A Windows-based PC.
- A monitor and GPU that support custom resolutions.
- Python 3.6+ installed on your system.

## Installation

### Option 1: Install via pip
To install the package directly from GitHub, run:

```bash
pip install git+https://github.com/nikoxdios/valorant-stretched-resolution.git
```

### Option 2: Manual Installation
1. Download or clone the repository:
    ```bash
    git clone https://github.com/nikoxdios/valorant-stretched-resolution.git
    ```
2. Navigate to the downloaded folder:
    ```bash
    cd valorant-stretched-resolution
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once installed, you can run the script directly via the command line using the following format:

```bash
vstretched -x 1024 -y 768
```

Replace `1024` and `768` with your desired resolution.

### Parameters
- `-x` : Width of the resolution.
- `-y` : Height of the resolution.

### Example:
```bash
vstretched -x 1280 -y 720
```

This will automatically update the necessary configuration files in Valorant to use the desired stretched resolution.

## Troubleshooting
If you encounter any issues:
- Verify that your GPU drivers are up-to-date.
- Ensure that your monitor supports the desired resolution.
- Make sure you are using the correct command-line arguments.
- Run the script as an administrator if you experience permission issues.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements. You can help add new features, improve documentation, or fix bugs.

## License
This project is licensed under the GNU General Public License v3.0 License. See the [LICENSE](LICENSE) file for details.
```
