#paint area calc

def paint_calc (height, width, cover):
    res = (height * width)/ cover
    result = round(res)
    print(f"You'll need {result} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# catatan 
# round adalah modul untuk membulatkan bilangan 