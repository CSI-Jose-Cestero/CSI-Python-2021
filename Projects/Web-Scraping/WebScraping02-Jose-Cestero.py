import requests
res = requests.get("https://www.gutenberg.org/files/67697/67697-0.txt")
res.raise_for_status()
playfile = open("Tales From A Dugout.text", "wb")
for chunk in res.iter_content(2000):
    playfile.write(chunk)
playfile.close()