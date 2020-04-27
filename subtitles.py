from youtube_transcript_api import YouTubeTranscriptApi, _errors


def get_subtitles(video_id, source_languages=['en', ], output_language='ru', proxies=None, cookies=None, verbose=False):
    transcript_list = YouTubeTranscriptApi.list_transcripts(
        video_id, proxies=proxies, cookies=cookies)
    transcript = None
    try:
        transcript = transcript_list.find_manually_created_transcript(
            [output_language])
    except _errors.NoTranscriptFound:
        if verbose:
            print("Info: No output language manually created transcripts found!")

    if transcript is None:
        try:
            transcript = transcript_list.find_manually_created_transcript(
                source_languages)
        except _errors.NoTranscriptFound:
            print("Error: No source language manually created transcripts found!")
            # all_transcripts = YouTubeTranscriptApi.get_transcripts(video_id)
            # all_langs = list(
            #     map(lambda x: [x.language_code, x.language], all_transcripts))
            # print("Error: No transcripts found! Available transcripts languages: ",
            #       '\n'.join(all_langs))
            return None

    # Youtube-translated transcript
    translated_transcript = None
    if (transcript.is_translatable):
        translated_transcript = transcript.translate(output_language)
    else:
        print("Failed. Transcript is not translatable!")
        return None

    return translated_transcript
