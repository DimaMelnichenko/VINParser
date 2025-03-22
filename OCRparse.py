import requests
import base64

def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    with open("save.png", "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    #print( image_base64 )

    payload = {'isOverlayRequired': overlay, 'apikey': api_key, 'language': language, 'OCREngine' : 2, 'scale': 'true',
               'base64Image': "data:image/png;base64," + str( image_base64 )
               }

    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.json()


def get_parsed_text():
    result = ocr_space_file("save.png", overlay=False, api_key='K88323205088957', language='eng')
    print( result )
    return result["ParsedResults"][0]["ParsedText"]


#get_parsed_text()