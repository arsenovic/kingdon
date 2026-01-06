#!/usr/bin/env python
"""Convert Jupyter notebooks to styled HTML for GitHub Pages."""

from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
from pathlib import Path

# HTML template wrapper that references external CSS
def wrap_with_template(body, title):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        {body}
        <footer>
            <p>Generated with Kingdon & nbconvert</p>
        </footer>
    </div>
</body>
</html>
"""
    return html

# Process all notebooks
def main():
    for nb_file in Path('.').glob('*.ipynb'):
        if nb_file.name == '.ipynb_checkpoints':
            continue
        
        print(f"Processing {nb_file.name}...")
        nb = nbformat.read(str(nb_file), as_version=4)
        
        # Get title from first markdown cell
        title = nb_file.stem.replace('_', ' ').title()
        for cell in nb.cells:
            if cell.cell_type == 'markdown' and cell.source.startswith('#'):
                title = cell.source.split('\n')[0].replace('#', '').strip()
                break
        
        try:
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': '.'}})
        except Exception as e:
            print(f"  Warning: {e}")
        
        exporter = HTMLExporter(
            template_name='classic',
            exclude_input=False,
            exclude_output_prompt=False
        )
        body, resources = exporter.from_notebook_node(nb)
        
        # Wrap with custom template
        html = wrap_with_template(body, title)
        
        html_file = nb_file.with_suffix('.html')
        with open(html_file, 'w') as f:
            f.write(html)
        
        print(f"  ✓ Converted to {html_file.name}")

    print("\n✓ All notebooks converted! (CSS linked from style.css)")

if __name__ == '__main__':
    main()
