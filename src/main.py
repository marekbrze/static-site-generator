from textnode import TextNode


def main():
    text_object = TextNode("Testowy", "NORMAL", "https://example.com")
    text_object2 = TextNode("Testowy", "NORMAL", "https://example.com")
    print(text_object, text_object2)
    print(text_object.__eq__(text_object2))


main()
