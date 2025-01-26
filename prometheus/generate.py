import json
import jinja2

with open('urls.json', "r") as f:
    data = json.load(f)
    
blackbox_urls = data.get("blackbox_urls", [])

template_file = "prometheus.j2"

with open(template_file, "r") as f:
    content_content = f.read()
    
template = jinja2.Template(content_content)

rendered_content = template.render(blackbox_urls=blackbox_urls)

output_file = "prometheus.yaml"

with open(output_file, "w") as f:
    f.write(rendered_content)
    
print("Generated file: ", output_file)



print(blackbox_urls)