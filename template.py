from jinja2 import Environment, FileSystemLoader
#Quin template utilitzem
enviroment = Environment(loader=FileSystemLoader("Template/"))
template = enviroment.get_template("lamevaweb.html")
#Fitxer final on apliquem les dades i agafem la bade de html
file = open("lamevawebfinal.html","w")


#Variable que passem al template
info = {"titol":"La meva Vida"}
#Generem el contingut final
contingut = template.render(info)
#Escrivim el contingut a un fitxer html
file.write(contingut)