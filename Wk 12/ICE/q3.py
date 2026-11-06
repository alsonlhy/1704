
# ### Q3: HTML

def extract_bold_texts(html_text):
    
    bolded = []


    # Splitting by '<b>' puts the relevant text segments at the front of each split
    parts = html_text.split("<b>")

    # Skip parts[0] because it is the text before the first <b>
    for part in parts[1:]:
        if "</b>" in part:
            content = part.split("</b>")[0]
            bolded.append(content)

    return bolded


