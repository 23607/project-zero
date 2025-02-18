# Functions
def decorate_text(boring_txt, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 2} {boring_txt}{decoration * 2}")

# Main Routine
decorate_text("Programming is Fun!", "⭐")