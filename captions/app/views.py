import os
from flask import Blueprint, request, jsonify, current_app
from .extensions import db
from .models import Video, Caption
from .utils import download_video, transcribe_video

bp = Blueprint("captions", __name__)


@bp.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.get_json() or {}
    video_url = data.get("video_url")
    language = data.get("language", "en")
    if not video_url:
        return jsonify({"error": "video_url required"}), 400

    video = Video(url=video_url)
    db.session.add(video)
    db.session.commit()

    video_path = download_video(
        video_url, current_app.config["UPLOAD_FOLDER"], str(video.id)
    )
    vtt_content = transcribe_video(video_path, language)

    caption_dir = os.path.join(current_app.config["UPLOAD_FOLDER"], "captions")
    os.makedirs(caption_dir, exist_ok=True)
    vtt_path = os.path.join(caption_dir, f"{video.id}_{language}.vtt")
    with open(vtt_path, "w") as f:
        f.write(vtt_content)

    caption = Caption(video_id=video.id, language=language, path=vtt_path)
    db.session.add(caption)
    db.session.commit()

    return (
        jsonify({"video_id": video.id, "caption_id": caption.id, "vtt_path": vtt_path}),
        201,
    )
