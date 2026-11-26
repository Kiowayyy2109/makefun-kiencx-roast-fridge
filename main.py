import os

LINE = "My smart fridge reorders milk the day I go on holiday, then texts me a photo of it expiring, like a roommate who plans my guilt in advance."

def main():
    assert len(LINE) == 139, f"line is {len(LINE)} chars, expected 139"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")

if __name__ == "__main__":
    main()
