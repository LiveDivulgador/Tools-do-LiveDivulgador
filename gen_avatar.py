from tqdm import tqdm
import numpy as np
import pandas as pd
import cv2
import requests
import shutil
import os
import random

DIR = os.path.abspath(os.path.dirname("."))

images_path = []

# Dataset com os nomes de todos o streamers
df = pd.read_csv("streamers_mod.csv", usecols=["Nome", "Avatar", "Twitter"])

for name, avatar, tt in zip(df["Nome"], df["Avatar"], df["Twitter"]):
        
        img_name = name+".jpg"
        url = avatar
        fout = os.path.join(DIR, "imgs", img_name)
        
        images_path.append(fout)

        # Só fazer download se houver Twitter
        if not isinstance(tt, float):

            # Só fazer download se ainda não houver a imagem
            if not os.path.exists(fout):

                r = requests.get(url, stream=True)

                if r.status_code == 200:

                    # Isto para que o tamanho do download não seja 0
                    r.raw.decode_content = True

                    with open(fout, "wb") as fw:
                        # Escrever a imagem no disco
                        shutil.copyfileobj(r.raw, fw)
        else:
            images_path.pop()


black_img = np.zeros((300, 300, 3))

random_img = np.random.randint(0, len(images_path)-1, size=(300, 300, 3))


for i in tqdm(range(black_img.shape[0])):
    for j in np.arange(0, black_img.shape[1]):
        for z in np.arange(0, black_img.shape[2]):
        
            random_val = random_img[i][j][z]

            img = cv2.imread(images_path[random_val])

            black_img[i][j][z] = img[i][j][z]


cv2.imwrite("avatar.jpg", black_img)