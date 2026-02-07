print(5 > 5)
print(67 == 55)
print(10 - 2 + 4 < 9)





temperature_astana = 15
temperature_dubai = 27
if temperature_dubai > temperature_astana: 
  print("Dubai is hotter than Astana") #prints based on condition
else:
  print("Astana is hotter than Dubai") 





print(bool("Hello")) #there is a value thus it returns True
print(bool())
print(bool(0))  #0 is not a value thus false
print(bool(15))





x = False
print(isinstance(x, bool))





def myFunction() :
    g = 2 > 1
    return g

if myFunction():
  print("YES!")
else:
  print("NO!")