old_dict = {
    182300401: "John",
    182300402: "Anna",
    182300403: "Peter",
    182300404: "Linda",
    182300405: "Mary",
    182300406: "Tom",
    182300407: "Sam",
    182300408: "Jerry",
    182300409: "Sue",
    182300410: "Mike",
    182300411: "Lisa",
    182300412: "Ben",
    182300413: "Ann",
    182300414: "Tim",
    182300415: "Chris",
    182300416: "Lisa",
    182300417: "Tom",
    182300418: "Jerry",
    182300419: "Ann",
    182300420: "Mike",
}
new_dict = {}
for id in old_dict:
    if id % 2 == 0:
        new_dict[id] = old_dict[id]

print(new_dict)
