import json
from youtube_dl import YoutubeDL
_ydl = YoutubeDL()


def ydl(url: str):
    _formats_mp4 = []
    _formats_webm = []
    _error = {
        "url": url,
        "error": "Someting is Wrong",
    }
    _ydl.add_default_info_extractors()
    try:
        info = _ydl.extract_info(
            url=url, download=False)
    except Exception as e:
        return _error
    try:
        if "formats" in info:
            for i in range(0, len(info['formats'])):
                if "mp4" in info['formats'][i]['ext']:
                    _formats_mp4.append(info['formats'][i])
                if "webm" in info['formats'][i]['ext']:
                    _formats_webm.append(info['formats'][i])
        else:
            for i in range(0, len(info['entries'][0]['formats'])):
                if "mp4" in info['entries'][0]['formats'][i]['ext']:
                    _formats_mp4.append(info['entries'][0]['formats'][i])
                if "webm" in info['entries'][0]['formats'][i]['ext']:
                    _formats_webm.append(info['entries'][0]['formats'][i])
    except:
        return info

    _json_ = {
        'title': info['title'],
        'url': url,
        'mp4': _formats_mp4,
        'webm': _formats_webm,
    }

    if 'thumbnail' in info:
        _json_.update({'thumbnail': info['thumbnail']})

    else:
        pass

    return _json_
