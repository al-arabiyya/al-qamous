# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd al_qamous/al_qamous/static/ui
```

To generate the styles:

```console
npm install
cd al_qamous/al_qamous/static/al_qamous
npx @tailwindcss/cli -i ../static/al_qamous/css/al_qamous.css -o ../static/al_qamous/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
