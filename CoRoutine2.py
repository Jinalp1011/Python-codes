def searcher():
    import time
    #some 4 seconds time consuming task
    book = "This is a book on Python coding done by Jinal Panchal"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in book")
        else:
            print("Text is not in the book")

search = searcher()
next(search)
search.send("Jinal")
input("press any key")
search.send("Python")
search.close()