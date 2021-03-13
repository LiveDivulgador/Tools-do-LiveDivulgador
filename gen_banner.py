import pandas as pd
import shutil
import requests
import os
import time
import cv2

DIR = os.path.abspath(os.path.dirname("."))
BLACK_IMG = os.path.join(DIR, 'imgs', 'black.jpg')

def vconcat_resize(list_imgs, inter=cv2.INTER_CUBIC):
    # Encontrar a altura minimo
    w_min = min(img.shape[1] for img in list_imgs)

    # Redimensionar as imagens
    list_resize = [cv2.resize(img,
                              (w_min, int(img.shape[0] * w_min / img.shape[1])),
                              interpolation=inter) for img in list_imgs]

    return cv2.vconcat(list_resize)

def hconcat_resize(list_imgs, inter=cv2.INTER_CUBIC):
    # Encontrar a altura minimo
    
    h_min = min(img.shape[0] for img in list_imgs)

    # Redimensionar as imagens
    list_resize = [cv2.resize(img,
                              (int(img.shape[1] * h_min / img.shape[0]), h_min),
                              interpolation=inter) for img in list_imgs]

    return cv2.hconcat(list_resize)

def list_images(list_2d):
    new_list = []

    for paths in list_2d:
        row = []
        for path in paths:
            print(path)
            img =  cv2.imread(path)
            img = cv2.resize(img, (img.shape[0]-100, img.shape[1]-100))
            row.append(img)

        new_list.append(row)

    return new_list


def create_2Dlist(list_img, row_size):

    list_2d = []

    # Criar a lista 2D com os caminhos
    for i in range(0, len(list_img), row_size):
        row = []
        for j in range(i, i+row_size):
            if j > len(list_img)-1:
                row.insert(0, BLACK_IMG)
            
            else:
                row.append(list_img[j])
        
        list_2d.append(row)
    
    # Lista 2D com as imagens em cada linha
    images = list_images(list_2d)

    return images

def create_tile(list_img):
    # Numero de Elementos de cada linha
    row_size = 16

    # Retornar imagens numa lista com row_size colunas
    list_2d = create_2Dlist(list_img, row_size)

     # Transformar horizontalmente
    h_concat = [hconcat_resize(list_row) for list_row in list_2d]

    # Transoformar verticalmente
    v_concat  = vconcat_resize(h_concat)

    v_concat = cv2.resize(v_concat, (1800, 600), interpolation=cv2.INTER_CUBIC)

    print(v_concat.shape)

    # Guardar a Tile
    cv2.imwrite("banner.jpg", v_concat)
    

def main():

    # Dataset com os nomes de todos o streamers
    df = pd.read_csv("streamers_mod.csv", usecols=["Nome", "Avatar", "Twitter"])

    names = []

    names_walk = os.walk(os.path.join(DIR, "imgs")).__next__()[2]

    if len(names_walk) > 1:
        names = [os.path.join(DIR, "imgs", path) for path in names_walk if path != "black.jpg"]

    else:
        
        for name, avatar, tt in zip(df["Nome"], df["Avatar"], df["Twitter"]):
            
            img_name = name+".jpg"
            url = avatar
            fout = os.path.join(DIR, "imgs", img_name)
            
            names.append(fout)

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
                print(name)
                names.pop()

    create_tile(names)



if __name__ == "__main__":
    main()