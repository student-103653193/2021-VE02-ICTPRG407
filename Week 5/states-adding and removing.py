#adding stuf back into a list
states=["VIC","NSW","SA","WA","TAS","QLD"]
print(states)
#adding now act
states.append("ACT")
print(states)
#removing states
states.remove("NSW")
print(states)
#readd NSW
states.append("NSW")
#only removed first one in the list though so if for example 2 NSW
#will only remove the first NSW
#can use pop if u want to remove depending on number in the list
states.pop(3)
print(states)