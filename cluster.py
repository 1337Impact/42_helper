import webbrowser

url = 'https://meta.intra.42.fr/clusters'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome_path).open(url)