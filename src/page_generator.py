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

def generate_page(from_path:str, template_path:str, dest_path:str, basepath:str):
    print(f"Generating page form {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        file = f.read()
    with open(template_path) as t:
        template = t.read()

    html_string = markdown_to_html_node(file).to_html()
    title = extract_title(file)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    page = page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    
    dirs = os.path.dirname(dest_path)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print("Necessary directories created")
    with open(dest_path, "w") as dest:
        dest.write(page)

def generate_pages_recursive(dir_path_content:str, template_path:str, dest_dir_path:str, basepath:str):
    if not os.path.exists(dir_path_content):
        raise Exception(f"Source path ({dir_path_content}) doesn't exist")
    
    contents = os.listdir(dir_path_content)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        print(f"Created {dest_dir_path}")
    
    for thing in contents:
        new_source = os.path.join(dir_path_content, thing)
        new_destiny = os.path.join(dest_dir_path, thing)
        if os.path.isfile(new_source):
            new_destiny = new_destiny[:-3] + ".html"
            generate_page(new_source, template_path, new_destiny, basepath)
            print(f"Generated html from {new_source} and located in {new_destiny}")
        else:
            generate_pages_recursive(new_source, template_path, new_destiny, basepath)
        
    
