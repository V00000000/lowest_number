class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        words = self.text.split()
        count = len(words)
        print(f"Word count: {count}")
        return count

    def save_text_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.text)
        print(f"Text saved to {filename}")

# Demo usage
text = "An example that violates a SOLID principle."
analyzer = TextAnalyzer(text)
analyzer.word_count()
analyzer.save_text_to_file("example.txt")
