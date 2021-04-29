from data import *

result = bloodgrp("ras", "heltar", "lavanya", "brace", "ramya")

result.read_data(listt)

result.write_data(listt)

partial = input("Enter phone num to search:")

result.search_donor(partial)
