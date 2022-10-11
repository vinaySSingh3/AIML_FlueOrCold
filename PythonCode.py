import aiml

kernal = aiml.Kernel()
kernal.learn("std-startup.xml")
kernal.respond("LOAD AIML B")

print(">NoobBOT: Hi I am Noob Doctor what are your symptoms")
print(">NoobBOT: fever,aches,cold,pain,sore throat,sneezing,chills,headeches,weak,tired,vomiting,nausea,diarrhea")
while True:
    input_text = input(">Human: " )
    response = kernal.respond(input_text)
    print(">NoobBOT: "+ response)



