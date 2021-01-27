
PUZZLE_NAME = "spcyear"


import json 

with open('numbertemplate.json', 'r') as file:
	MAP_TEMPLATE = file.read()

with open('puzzletemplate.html', 'r') as file:
	HTML_TEMPLATE = file.read()

with open(PUZZLE_NAME + ".json") as json_file: 
	info = json.load(json_file) 

for i in range(len(info["answer"])):
	correctAnswerExit = "../../" + info["endpoint"]
	if (i < len(info["answer"])-1):
		correctAnswerExit = info["answer"][:i+1] + ".json"
	result = MAP_TEMPLATE
	result = result.replace("\"image\":\"..\\/", "\"image\":\"..\\/..\\/")
	
	
	for j in range(10):
		result = result.replace("$PH_" + str(j) + "$.json", "start" if (str(j) != str(info["answer"][i])) else correctAnswerExit)
	
	fileName = "start" if i == 0 else info["answer"][:i]
	
	result = result.replace("$PUZZLE_NAME$", PUZZLE_NAME)
	result = result.replace("$PROGRESS$", fileName)
	
	with open(PUZZLE_NAME + "/" + fileName + ".json", "w") as outputFile:
		outputFile.write(result)
	
	correctAnswerSoFar = ""
	for j, c in enumerate(info["answer"]):
		correctAnswerSoFar += ("_" if (j >= i) else c) + " "
	correctAnswerSoFar = correctAnswerSoFar[:-1]
	
	htmlResult = HTML_TEMPLATE.replace("$QUESTION$", info["question"])
	htmlResult = htmlResult.replace("$ANSWER$", correctAnswerSoFar)
	with open(PUZZLE_NAME + "/" + fileName + ".html", "w") as outputFile:
		outputFile.write(htmlResult)

