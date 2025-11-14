thondef choose_format(quality: str, file_format: str) -> str:
    """
    Translate quality + format into yt-dlp format selector.
    """
    if quality == "best":
        return f"bestvideo+bestaudio/best.{file_format}"

    return f"bestvideo[height={quality}]+bestaudio/best.{file_format}"