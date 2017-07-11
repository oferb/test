from time import gmtime, strftime

with open(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".txt", "w") as text_file:
  text_file.write("bla bla bla bla")
