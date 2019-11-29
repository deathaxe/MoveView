# Move View

Plugin for Sublime Text to move views within a group.

![Animation](https://user-images.githubusercontent.com/16542113/69913166-7579e880-1434-11ea-92c8-80c04a0d632e.gif)

It is heavily inspired by [MoveTab](https://github.com/SublimeText/MoveTab).

It is written from scratch in order to...

1. introduce a wording (Move View) which better fits into Sublime Text's ecosystem as there are related functions like `Menu > View > Move File To Group` for instance.
2. introduce new commands `move_to_neighboring_index` and `move_to_index`, which sound and behave like the built-in `move_to_neighbouring_group` and `move_to_group` commands.
3. enable `move_to_index` to list all open files of the current group as a possible destination to move the active view to.


## Usage

A view can be moved via Command Palette with:

- Move View: To Positon
- Move View: To The Left
- Move View: To The Right
- Move View: To First Position
- Move View: To Last Position

A view can be moved via keyboard with:

- Linux/Windows: <kbd>CTRL + Shift + Page up</kbd> and <kbd>CTRL + Shift + Page down</kbd>
- MacOS: <kbd>Command + Alt + Shift + Left</kbd> and <kbd>Command + Alt + Shift + Right</kbd>


## Requirements

Sublime Text 3.

## Installation

Use the Package Control.

	Command palette > Package Control: Install Package

Alternatively, simply clone this repository into the Packages directory.

	Preferences > Browse Packages...

## License

Licensed under the [MIT License](http://www.opensource.org/licenses/mit-license.php)
