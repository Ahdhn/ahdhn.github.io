def extract_bibtex_entries(bibtex_str):
    entries = {}
    current_key = None
    current_entry = ""

    for line in bibtex_str.splitlines():
        if line.startswith("@"):
            if current_key:
                entries[current_key] = current_entry.strip()
            current_key = line.split("{")[1].split(",")[0].strip()
            current_entry = line
        else:
            current_entry += "\n" + line
    if current_key:
        entries[current_key] = current_entry.strip()

    return entries

def create_html_from_bibtex(bibtex_file_path, output_html_file_path):
    with open(bibtex_file_path, 'r') as file:
        bibtex_str = file.read()

    bibtex_entries = extract_bibtex_entries(bibtex_str)

    html_content = "<html>\n<head>\n<title>Mahmoud Bibliography</title>\n</head>\n<body>\n"
    #for key in bibtex_entries:
    #    html_content += f'<li><a href="#{key}">{key}</a></li>\n'
    #html_content += "</ul>\n<hr>\n"

    for key, entry in bibtex_entries.items():
        html_content += f'<div id="{key}"><pre>{entry}</pre></div>\n<hr>\n'

    html_content += "</body>\n</html>"

    with open(output_html_file_path, 'w') as html_file:
        html_file.write(html_content)

# Example usage
create_html_from_bibtex('mahmoud.bib', 'mahmoud_bib.html')