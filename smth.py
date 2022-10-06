import camelcase

c = camelcase.CamelCase()   
txt = "hello world this is a test" # so is and a are not capitalized 
print(c.hump(txt))
