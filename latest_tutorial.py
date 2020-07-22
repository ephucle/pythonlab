from reader import feed

def main():
    """Download and print the latest tutorial from Real Python"""
    tutorial = feed.get_article(0)
    print(tutorial)

if __name__ == "__main__":
    main()
