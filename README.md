# bandite.eu — static site

Static website for **BANDITE** (artivism collective), hosted on GitHub Pages and served at [bandite.eu](https://bandite.eu).

Rebuilt as a clean, dependency-free static site from the former WordPress site (`lebandite.wordpress.com`).

## Structure

```
index.html, about.html, …   generated HTML pages
assets/css/style.css        styles
assets/js/main.js           mobile nav + slideshows
assets/img/                 optimised images
assets/docs/                press PDFs
CNAME                       custom domain (bandite.eu)
.nojekyll                   disable Jekyll processing
build.py                    page generator (content lives here)
bandite.WordPress.*.xml     original WordPress export (archive)
```

## Editing content

All text content lives in **`build.py`**. To change a page, edit the relevant block
and regenerate:

```bash
python3 build.py
```

This rewrites the `.html` files in place. Commit and push — GitHub Pages redeploys automatically.

Images are referenced from `assets/img/`. To add one, drop the file there and reference it in `build.py`.

## Hosting

- **GitHub Pages**, deployed from the `main` branch (root).
- Custom domain `bandite.eu` (+ `www.bandite.eu`) configured via DNS at the registrar; see repo Settings → Pages.
- HTTPS enforced.

## Credits

Photos by Mauro Ujetto. © BANDITE — Valentina Bosio & Simona Sala.
