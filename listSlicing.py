# List Slicing
text = "This is Python Code."
slice_text1 = text[5:7]  # ending index not included.
slice_text2 = text[8 : len(text)]
slice_text3 = text[0:4]
slice_text4 = text[8:]
slice_text5 = text[:4]
slice_text6 = text[-5:-1]  # List allowed Negative Indexing.
print(slice_text1)
print(slice_text2)
print(slice_text3)
print(slice_text4)
print(slice_text5)
print(slice_text6)
