from textnode import TextNode, TextType
import os
import shutil

def cloner(source:str, destiny:str):
    if not os.path.exists(source):
        raise Exception(f"Source path ({source}) doesn't exist")
    if os.path.exists(destiny):
        shutil.rmtree(destiny)
    
    contents = os.listdir(source)
    os.mkdir(destiny)
    print(f"Created {destiny}")
    
    for thing in contents:
        new_source = os.path.join(source, thing)
        new_destiny = os.path.join(destiny, thing)
        if os.path.isfile(new_source):
            shutil.copy(new_source, new_destiny)
            print(f"Copied {new_source} to {new_destiny}")
        else:
            cloner(new_source,new_destiny)
        





def main():
    cloner(source="static", destiny="public")


main()