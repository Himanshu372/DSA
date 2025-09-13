import os
from pathlib import Path

def change_artifact_name(root: str): 
    for (curr_dir, dirs, files) in os.walk(root):
        # path = Path(curr_dir)
        if curr_dir.startswith("."):
            return
        # os.rename(curr_dir, split_and_rename(curr_dir))
        for file in files:
            if file.startswith("."):
                continue
            # print(curr_dir + "/" + file.lower())
            os.rename(curr_dir + "/" + file, curr_dir + "/" + file.lower())
        for dir in dirs:
            if dir.startswith("."):
                continue
            # print(curr_dir + "/" + dir.lower())
            # print(join(root, dir))
            os.rename(curr_dir + "/" + dir, curr_dir + "/" + dir.lower())
            change_artifact_name(join(root, dir))
    return
        
# def split_and_rename(artifact: str) -> str:
#     parts = str.rsplit(artifact, "/", 1)
#     if len(parts) == 2:
#         return parts[0] + "/" + parts[1].lower()
#     elif len(parts) == 1:
#         return parts[0].lower()
    
def join(*artifacts) -> str: 
    return "/".join(artifacts)

if __name__ == "__main__":
    print("====Started====")
    change_artifact_name(os.getcwd())
    print("====Ended====")