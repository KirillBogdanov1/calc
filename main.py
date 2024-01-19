from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#zn1")
    input_text2 = document.querySelector("#zn2")
    zn1 = input_text.value
    zn2 = input_text2.value
    output_div = document.querySelector("#output")
    output_div.innerText =int(zn1)+int(zn2) 
