import os
import re
import configparser
import argparse

def check_valid_input(key, value=None):
    try:
        return int(value)
    except ValueError:
        print(f"Invalid input for {key}. Please enter an integer.")
        return None

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Set Valorant resolution.")
    parser.add_argument('-x', type=int, help="Width of the resolution", required=True)
    parser.add_argument('-y', type=int, help="Height of the resolution", required=True)
    args = parser.parse_args()

    # Resolution from arguments
    width = check_valid_input("width", args.x)
    height = check_valid_input("height", args.y)

    if not width or not height:
        exit()

    print(f"Resolution: {width}x{height}")

    riot_local_machine = os.path.join(os.getenv('LOCALAPPDATA'), r"VALORANT\Saved\Config\Windows\RiotLocalMachine.ini")

    # Check if RiotLocalMachine.ini exists
    if not os.path.exists(riot_local_machine):
        print("RiotLocalMachine.ini not found.")
        exit()

    # Extract LastKnownUser from RiotLocalMachine.ini
    config = configparser.ConfigParser()
    config.read(riot_local_machine)

    user_id = config.get('UserInfo', 'LastKnownUser', fallback=None)  # Adjusted to 'UserInfo'
    if user_id:
        print(f"User ID found: {user_id}")
    else:
        print("No LastKnownUser found in RiotLocalMachine.ini.")
        exit()

    # Define the path to GameUserSettings.ini
    config_path = os.path.join(os.getenv('LOCALAPPDATA'), r"VALORANT\Saved\Config")
    user_dir = None

    # Use regex to match the user ID followed by an optional region suffix (e.g., -latam)
    user_id_pattern = f"^{re.escape(user_id)}(-[a-zA-Z]+)?$"  # Match the user ID with optional region suffix

    print("Checking user directories...")

    # Locate the user directory matching the user_id, regardless of the region suffix
    for dir_name in os.listdir(config_path):
        if os.path.isdir(os.path.join(config_path, dir_name)) and re.match(user_id_pattern, dir_name):
            user_dir = os.path.join(config_path, dir_name)
            print(f"User directory found: {user_dir}")
            break

    if not user_dir:
        print(f"No user directory found matching the user ID {user_id}.")
        exit()

    game_settings = os.path.join(user_dir, "Windows", "GameUserSettings.ini")

    # Check if GameUserSettings.ini exists
    if not os.path.exists(game_settings):
        print(f"GameUserSettings.ini not found in {user_dir}.")
        exit()

    # Variables to ensure existence of required keys
    keys = {
        "ResolutionSizeX": str(width),
        "ResolutionSizeY": str(height),
        "LastUserConfirmedResolutionSizeX": str(width),
        "LastUserConfirmedResolutionSizeY": str(height),
        "DesiredScreenWidth": str(width),
        "DesiredScreenHeight": str(height),
        "LastUserConfirmedDesiredScreenWidth": str(width),
        "LastUserConfirmedDesiredScreenHeight": str(height),
        "bShouldLetterbox": "False",
        "bLastConfirmedShouldLetterbox": "False",
        "FullscreenMode": "2",
    }

    excluded_sections = {"/Script/Engine.GameUserSettings", "ScalabilityGroups", "ShaderPipelineCache.CacheFile"}

    config = configparser.ConfigParser()
    config.read(game_settings)

    if "/Script/ShooterGame.ShooterGameUserSettings" not in config.sections():
        config.add_section("/Script/ShooterGame.ShooterGameUserSettings")

    for section in config.sections():
        if section in excluded_sections:
            continue

        for key, value in keys.items():
            config.set("/Script/ShooterGame.ShooterGameUserSettings", key, value)

    # Write updated settings back to GameUserSettings.ini
    with open(game_settings, 'w') as configfile:
        config.write(configfile)

    print("GameUserSettings.ini updated successfully.")

if __name__ == "__main__":
    main()
