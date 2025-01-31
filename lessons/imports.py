"""Examples of importing Python."""


from lessons import helpers
from lessons.helpers import powerful

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()
