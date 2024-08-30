# from pytubefix import YouTube
# from pytubefix.cli import on_progress
# from pydub import AudioSegment
# import os

# def descargar_audio_youtube(url):
#     yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
#     video = yt.streams.filter(only_audio=True).first()
#     destino = "test_youtube_demo"
#     out_file = video.download(output_path=destino)
#     print(f"file is: {out_file}")
#     base, ext = os.path.splitext(out_file)

#     # Convertir a formato WAV usando pydub
#     audio = AudioSegment.from_file(out_file)
#     new_file = base + '.mp3'
#     audio.export(new_file, format='mp3')

#     # Opcional: Eliminar el archivo original descargado
#     os.remove(out_file)
#     print(new_file)

#     return new_file


# descargar_audio_youtube("https://www.youtube.com/watch?v=2yJgwwDcgV8")


from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=2yJgwwDcgV8"

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
           
ys = yt.streams.get_highest_resolution()

ys.download() # you will only get the request to authenticate once you download