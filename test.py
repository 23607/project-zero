def decorate_text(boring_txt, decoration, lines):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 line). Emojis are recomended only for emphasised text"""

    middle = f"{decoration * 2} {boring_txt} {decoration * 2}"
    top_bottom = decoration * len(boring_txt)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom * lines / 2)
        print(middle)
        print(top_bottom * lines / 2)

# Main Routine goes here
decorate_text("a big title!", "⭐", 6)
print()
decorate_text("12345671234567", "⭐", 2)
print()
decorate_text("look at me!", "⭐", 1)