from string import Template

d = {
    'title': 'This is the title',
    'subtitle': 'And this is the subtitle',
    'list': '\n'.join(['first', 'second', 'third'])
}

with open('template1.txt', 'r') as f:
    input_file_content = f.read()
    src = Template(input_file_content)
    result = src.substitute(d)
    
    print("---------template before fill----------------")
    print(input_file_content)

    text_file = open("template1_fill.txt", "w")
    n = text_file.write(result)
    text_file.close()

with open('template1_fill.txt', 'r') as f:
    print("---------template after fill-----------------")
    print(f.read())