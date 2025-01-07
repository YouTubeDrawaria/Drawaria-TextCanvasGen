# Drawaria TextCanvasGen

Drawaria TextCanvasGen is a Python script that automates drawing text on the [Drawaria](https://drawaria.online/) canvas using Selenium and WebSocket commands. This tool allows you to programmatically draw text on the canvas and send drawing commands to the Drawaria WebSocket server.

## Features

- Automates text drawing on the Drawaria canvas.
- Supports sending custom drawing commands via WebSocket.
- Allows user input for dynamic text drawing.
- Works in private rooms on Drawaria.

## Prerequisites

- Python 3.x
- Selenium (`pip install selenium`)
- ChromeDriver (download from [here](https://sites.google.com/chromium.org/driver/))

## Installation

1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/yourusername/Drawaria-TextCanvasGen.git
   cd Drawaria-TextCanvasGen
   ```

2. Install the required Python packages.
   ```bash
   pip install selenium
   ```

3. Download ChromeDriver and ensure it matches your Chrome browser version. Place the `chromedriver.exe` in a known directory (e.g., `C:\SeleniumDrivers\`).

4. Update the `chrome_driver_path` variable in the script with the correct path to your `chromedriver.exe`.

## Usage

1. Run the script:
   ```bash
   python drawaria_textcanvasgen.py
   ```

2. Enter the text you want to draw on the canvas when prompted. The script will render the text on the Drawaria canvas.

3. Type `exit` to quit the program.

## Example

```bash
Write the text in the canvas OR exit to quit(Only works in private rooms): Hello, World!
```

This will draw "Hello, World!" on the Drawaria canvas.

## Notes

- The script is designed to work in private rooms on Drawaria.
- Ensure you have a stable internet connection while running the script.
- The script uses WebSocket to send drawing commands, which may require additional configuration for advanced use cases.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

Enjoy drawing with Drawaria TextCanvasGen! 🎨