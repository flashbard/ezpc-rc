from pynput.keyboard import Controller, Key
import subprocess

from profiles import ProfileRepository

profiles = ProfileRepository()
_keyboard = Controller()

# Collection of methods to handle inputs from the serial port


def _trigger_keyboard_operation(key, operation):
    if len(key) == 1:
        # Normal key
        operation(key)
    else:
        # Special key
        try:
            operation(Key[key])
        except KeyError as exc:
            # Invalid key
            print(exc)
            raise ValueError(f"Invalid key: {exc}")


def _execute_shortcut(keys):
    for key in keys:
        if isinstance(key, list):
            # We have a combo
            _execute_shortcut(key)
        else:
            _trigger_keyboard_operation(key, _keyboard.press)

    for key in reversed(keys):
        if not isinstance(key, list):
            _trigger_keyboard_operation(key, _keyboard.release)


def _get_key_map(data):
    try:
        return profiles.current["map"][data]
    except KeyError:
        pass

    return profiles.base["map"][data]


def handle_input(data):
    try:
        key_map = _get_key_map(data)

        if key_map["type"] == "key":
            _execute_shortcut(key_map["value"])
        elif key_map["type"] == "cmd":
            subprocess.Popen(key_map["value"], shell=True)
        elif key_map["type"] == "profile":
            profiles.load_next_profile()

        return f"{data}: {key_map}"
    except KeyError as exc:
        if data != "0":
            # Only print non-zero inputs -> zero captured when a key is held
            print(f"{data} is not mapped")
    except Exception as exc:
        print(exc)
