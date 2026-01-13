import requests

def find_deals():
    # Example logic: Your script finds a link
    new_deal = '<p><a href="AFFILIATE_URL">91% OFF: Chemical-Free Soap</a></p>\n'
    
    # Read the current website
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Insert the new deal at the top of the 'links' div
    updated_content = content.replace('<div id="links">', '<div id="links">\n' + new_deal)
    
    with open('index.html', 'w') as f:
        f.write(updated_content)

find_deals()
