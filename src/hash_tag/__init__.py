# Imports
from datetime import datetime
from flask import Blueprint, render_template, request
from src.utils import get_final_matrix

# Register Swagger Blueprint
hash_tag = Blueprint("hash_tag", __name__)


# Routes
@hash_tag.route("/hash-tags-generator", methods=["GET", "POST"])
def get_hash_tags():
    if request.method == "POST":
        f = request.files["hash-tag-file"]

        if f:
            hash_tag_matrix, sentences = get_final_matrix(file=f.stream)

        else:
            hash_tag_matrix = None
            sentences = None

        if not hash_tag_matrix:
            return render_template('pages/hash_tag.html')

        return render_template(
            'pages/hash_tag.html',
            hash_tag_matrix=hash_tag_matrix,
            file_name=f.filename,
            scan_date=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            sentences=sentences
        )

    return render_template('pages/hash_tag.html')
