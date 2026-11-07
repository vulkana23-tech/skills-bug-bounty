import urllib.request
import zipfile
import pathlib
import os
import shutil

def main():
    url = "https://github.com/bee-san/RustScan/releases/download/2.4.1/x86_64-windows-rustscan.exe.zip"
    temp_zip = pathlib.Path(os.environ["TEMP"]) / "rustscan.zip"
    extract_dir = pathlib.Path(os.environ["TEMP"]) / "rustscan_extract"
    dest_dir = pathlib.Path.home() / ".cargo" / "bin"
    dest_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp, open(temp_zip, "wb") as f:
        shutil.copyfileobj(resp, f)

    print("Extracting...")
    with zipfile.ZipFile(temp_zip, "r") as z:
        z.extractall(extract_dir)

    found = False
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            if file.endswith(".exe"):
                src_exe = pathlib.Path(root) / file
                dst_exe = dest_dir / "rustscan.exe"
                shutil.copy2(src_exe, dst_exe)
                # Also copy to workspace bin/
                workspace_bin = pathlib.Path("bin")
                workspace_bin.mkdir(exist_ok=True)
                shutil.copy2(src_exe, workspace_bin / "rustscan.exe")
                print(f"Installed {dst_exe} successfully!")
                found = True
                break

    if not found:
        print("No .exe found in zip!")

    try:
        temp_zip.unlink(missing_ok=True)
        shutil.rmtree(extract_dir, ignore_errors=True)
    except Exception:
        pass

if __name__ == "__main__":
    main()

