
#Download a log file
import requests
url = "https://raw.githubusercontent.com/maximlt/PythonScript/master/exercices/loganalysis/culvert_logfile.txt"
r = requests.get(url, allow_redirects=True)
open('log.txt', 'wb').write(r.content)

#Read a file and print it 
f = open("log.txt", "r")
print(f.read()) 

#Count the number of Culvert
def count_culvert():
    datafile = open('log.txt','r')
    count =0
    search = "Culvert_name"
    for line in datafile:
        if search in line:
            count+= 1
    return count
    
print("Number of culver is : ", count_culvert()) 

#Parsing the data
import pandas
culvert_data = {
    "branch": [],
    "name": [],
    "type": [],
    "diameter": [],
    "length": [],
    "manning": [],
    "upstream_chainage": [],
    "upstream_invert": []
}

def parsing_data():
	datafile = open('log.txt','r');
	for line in datafile :
		if "Culvert_params" in line:
			params = line.strip().split(" = ")[1].split(",")
			t, d, l, m, uc, ui = params
			culvert_data["type"].append(t)
			culvert_data["diameter"].append(d)
			culvert_data["length"].append(l)
			culvert_data["manning"].append(m)
			culvert_data["upstream_chainage"].append(uc)
			culvert_data["upstream_invert"].append(ui)
       
		if "Culvert_name" in line :
			name = line.strip().split(" = ")[1].strip("'")
			culvert_data["name"].append(name)
		if "Culvert_branch" in line :
			branch = line.strip().split(" = ")[1].strip("'")
			culvert_data["branch"].append(branch)
	df = pandas.DataFrame(culvert_data)
# Les données extraites sont enregistrées dans un fichier csv.
# index=False évite d'écrire l'index du DataFrame dans le fichier, celui-ci
# n'étant pas utile ici.
	df.to_csv("culvert_data.csv", index=False)
	
	
parsing_data()
