# Notebook to HTML Workflow

Convert Jupyter notebooks to styled HTML for GitHub Pages.

## Files

- `*.ipynb` - Jupyter notebooks with Kingdon visualizations
- `convert.py` - Conversion script
- `style.css` - Shared stylesheet
- `*.html` - Generated HTML files

## Usage

Run the conversion script:

```bash
cd tmp
uv run --with nbconvert --with jupyter python convert.py
```

Or from the repo root:

```bash
uv run --with nbconvert --with jupyter tmp/convert.py
```

## What It Does

1. **Executes** each notebook to capture Ganja.js widget outputs
2. **Converts** to HTML using nbconvert
3. **Wraps** with a custom template that references `style.css`
4. **Outputs** styled HTML files ready for GitHub Pages

## Customization

Edit `style.css` to change the appearance. All HTML files automatically use the updated styles.

## Output

- `coords.html` - Coordinate systems
- `helix.html` - Helix visualization
- `kingdonFields.html` - Field visualizations
- `stasplit.html` - Spacetime algebra split

All are ready to host on GitHub Pages.
