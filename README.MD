# minecraft-music-simulator

## What's this?

This is a little Python program that can extract music from your Minecraft installation and simulate the music behaviour just like it's in the game. I've tried to make it as configurable as possible.

Feel free to look around my spaghetti code and comment.

Feel free to contact me on Discord if you have any questions. My Discord is alex_#2171.

## Installation & Setup

```sh
git clone https://github.com/TheBrightSide/minecraft-music-simulator.git
cd minecraft-music-simulator
pip install -r requirements.txt
```
```sh
py extractor.py # Recommended version 1.16
py main.py
```

## Usage

- You can start the application from `main.py`
  ```sh
  py main.py
  ```
- You can extract the music files using `extractor.py` (recommended version: 1.16)
  ```sh
  py extractor.py
  ```
- You can configure the application from `options.json`
- `musicMapping.json` is the music files configuration.
- `leftover.json` (generated by the application) is a file that contains the current progression
