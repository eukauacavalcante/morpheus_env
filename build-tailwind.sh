#!/bin/bash
# build-tailwind.sh
source venv/bin/activate
venv/bin/tailwind -i ./static/css/input.css -o ./static/css/styles.css --minify
echo "✅ CSS do Tailwind atualizado!"
