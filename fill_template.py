from string import Template

d = {
    'gnbname': 'gHA00037',
    'subtitle': 'And this is the subtitle',
    'vlanid_oam':'2639',
    'oam_ipaddress':'10.188.132.145',
    'vlanid_traffic':'2638',
    'traffic_ipaddress':'10.178.132.145',
    'next_hop_oam':'10.188.132.150',
    'next_hop_traffic':'10.178.132.150'
}
template = "sitebasic.xml"
with open(template, 'r') as f:
    input_file_content = f.read()
    src = Template(input_file_content)
    result = src.substitute(d)
    
    print("---------template before fill-----------------------------------------")
    print(input_file_content)
    output_filename = template+ ".fill.xml"
    text_file = open(output_filename, "w")
    n = text_file.write(result)
    text_file.close()

with open(output_filename, 'r') as f:
    print("---------template after fill------------------------------------------------------------------------------------")
    print(f.read())