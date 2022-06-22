import base64
import glob

HTML_TEMPLATE = "index1.html"
HTML_OUTPUT = "index.html"


def encode_files():
    images = {}
    for fn in glob.glob("images\\*.png"):
        print(f"Encoding ... {fn=}")
        n = fn.replace("\\", "/")
        b64 = base64.b64encode(open(fn, "rb").read()).decode('utf-8')
        images[n] = "data:image/png;base64,"+b64
        #filename = Path(fn)
        #fn2 = filename.with_suffix('.png')
    print("Encoded {} images".format(len(images)))
    return images


files = encode_files()

s = open(HTML_TEMPLATE, encoding="utf-8").read()

for fn in files.keys():
    print(f"Replacing {fn}")
    s = s.replace(fn, files[fn])

open(HTML_OUTPUT, "w", encoding="utf-8").write(s)
