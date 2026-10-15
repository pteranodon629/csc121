def main():
    with open("alice.txt", "r", encoding='utf-8', errors='ignore') as f:
        contents = f.readlines()
    chapter1 = contents[52:271]
    with open("chapter1.txt", "w", encoding='utf-8') as f:
        f.writelines(chapter1)

if __name__ == "__main__":
    main()
