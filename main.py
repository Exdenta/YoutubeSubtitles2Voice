import subtitles as st
from googletrans import Translator
import emoji

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=dEv99vxKjVI"
    video_id = "dEv99vxKjVI"

    transcript = st.get_subtitles(
        video_id, source_languages=['de', ], output_language='ru', proxies=None, cookies=None, verbose=True)
    transcript_data = transcript.fetch()
    subtitles = list(map(lambda x: x['text'], transcript_data))
    print(' '.join(subtitles))
