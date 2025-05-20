# Az első AI képgenerálásom Python használatával

### Telepítés
# 1)
# python -m venv my_env
# Futtatni rendszergazdaként: source my_env/bin/activate  # (Windows esetén: my_env\Scripts\activate)
#
# 2)
# pip install diffusers transformers accelerate torch
#
#   hiba esetén:
#   pip uninstall diffusers
#   pip install diffusers --upgrade
#
# 3)
# pip install transformers


### A kód

# Importáljuk a szükséges könyvtárakat:
# - A diffusers csomag biztosítja a Stable Diffusion modell kezelését.
# - A torch (PyTorch) segít a GPU vagy CPU kezelésében.
from diffusers import StableDiffusionPipeline  # A diffusions modellek kezelésére szolgáló eszköz
import torch  # PyTorch a számítási műveletekhez és GPU támogatáshoz

# Megadjuk a használni kívánt modell nevét.
# Ebben az esetben a "runwayml/stable-diffusion-v1-5" modellt fogjuk használni.
model = "runwayml/stable-diffusion-v1-5"

# Beállítjuk a helyi cache könyvtárat, ahová a modell súlyait letöltjük.
# Így nem kell minden futtatáskor újból letölteni azokat, ami csökkenti az internetes adatforgalmat.
cache_directory = "C:/model_cache"  
# Például Windows-on: "C:/model_cache", Linuxon: "/home/felhasználó/model_cache"

# Betöltjük az előre betanított modellt a megadott cache könyvtárral.
# A from_pretrained metódus automatikusan letölti a modell súlyait (ha még nem találja a cache-ben).
pipe = StableDiffusionPipeline.from_pretrained(model, cache_dir=cache_directory)

# Eldöntjük, hogy GPU-t vagy CPU-t használunk a számításokhoz.
# Ha elérhető a CUDA, akkor a GPU fogja gyorsítani a folyamatot,
# egyébként a CPU-t használjuk.
if torch.cuda.is_available():
    pipe.to("cuda")  # GPU használata, ha lehetséges
else:
    pipe.to("cpu")   # CPU használata, ha nincs GPU

#Oszthatóság 8-cal: A legtöbb diffúziós modell esetében a szélességnek és magasságnak olyan értéken kell lennie, ami 8-cal osztható (például 512, 768, 1024, stb.), mert a modell architektúrája ezt várja.
# Kép méret paraméterek változóban történő megadása
desired_height = 480  # Magasság, 8-cal osztható érték pl.:768
desired_width = 480   # Szélesség, 8-cal osztható érték pl.:768

# Seed érték megadása
seed_value = 54321  # Állítsd be egy tetszőleges számra
generator = torch.manual_seed(seed_value)

# Definiálunk egy függvényt, amely a megadott szöveg (prompt) alapján generál egy képet.
def generate_image(text_prompt, height, width, output_path="pai00010_generated_image.png"):
    # A pipe segítségével a megadott promptból generálódik egy kép,
    # melyből az első elemet választjuk (a pipe visszatér egy listával).
    image = pipe(text_prompt, height=height, width=width, generator=generator).images[0]
    
    # A generált képet elmentjük a megadott fájlba.
    image.save(output_path)
    
    # Visszatérünk a kép objektummal, hogy később meg tudjuk jeleníteni vagy tovább dolgozni vele.
    return image

# Például a függvény hívása:
# Itt adjuk meg, hogy milyen képet szeretnénk.
text = "An apple on the table."
generated_img = generate_image(text, desired_height, desired_width)

# Google drive és colab használata
#from google.colab import drive
#drive.mount('/content/drive')
#output_path = "/content/drive/MyDrive/pai00010_generated_image.png"
#generated_img.save(output_path)

# Megjelenítjük a generált képet egy külön ablakban.
generated_img.show()