input_string = "ПРаоап sdfJH Hjhjdh"

result_string = ''.join(filter(lambda x: not x.isupper(), input_string))

print(result_string)
