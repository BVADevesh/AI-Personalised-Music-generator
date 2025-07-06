# app.py - CLI or entry point

from src import generator, personalization

def main():
    user_profile = {"mood": "relaxing", "genre": "lo-fi"}
    config = personalization.parse_user_input(user_profile)
    output = generator.generate_music(config, "music_vae_model")
    print(f"Music generated: {output}")

if __name__ == "__main__":
    main()
