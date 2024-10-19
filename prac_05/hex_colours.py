COLOUR_CODES = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceBlue": "	#f0f8ff",
                "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                "antique white": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

colour_name = input("Enter the colour name: ").lower()
while colour_name != "":
    print(f"The colour code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter the colour name: ").lower()