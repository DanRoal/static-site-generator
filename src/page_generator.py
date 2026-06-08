from functions import *
import os

def extract_title(markdown:str):
    res = ""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if determine_block_tag(block, block_type) == "h1":
            return block[2:].strip()
    raise Exception("There was no title in provided markdown")

def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page form {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        file = f.read()
    with open(template_path) as t:
        template = t.read()

    html_string = markdown_to_html_node(file).to_html()
    title = extract_title(file)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    dirs = os.path.dirname(dest_path)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print("Necessary directories created")
    with open(dest_path, "w") as dest:
        dest.write(page)


    
