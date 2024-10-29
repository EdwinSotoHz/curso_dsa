from Node_sandbox import Node

Yady = Node("Le gustan las flores")
Giovany = Node("Le gustan las princesas",Yady)
Juan = Node("Es jefe de jefes",Giovany)

Giovany_data = Giovany.value
Yady_data = Yady.value

print(Giovany_data)
print(Yady_data)