SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " SpongeBob SquarePants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud Family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    print(', '.join(cleaned_shows))

main()
