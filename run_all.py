import glob, os
from nbformat import read, write
from nbclient import NotebookClient

os.makedirs("executed", exist_ok=True)

for path in glob.glob("notebooks/*.ipynb"):
    print(f"▶ Executing {path} …")
    nb = read(path, as_version=4)
    client = NotebookClient(nb, timeout=600, kernel_name="python3")
    client.execute()
    out_path = os.path.join("executed", os.path.basename(path))
    write(nb, out_path)
print("✅ All notebooks executed.")