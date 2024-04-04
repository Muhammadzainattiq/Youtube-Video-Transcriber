import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
st.set_page_config(page_title="yt video transcriber", page_icon="📝")
st.markdown("""
    <style>
        .header {
            font-size: 56px;
            color: #FDFEFF; /* Change the color as per your preference */
            background-color: #f50000;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* Add shadow effect */
        }
        .head {
            font-size: 16px;
            color: #FDFEFF; /* Change the color as per your preference */
            background-color: #f50000;
            text-align: left;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* Add shadow effect */
        }
        .response {
            font-size: 34px;
            color: red; /* Change the color as per your preference */
            text-align: left;
            margin-bottom: 20px;
        }
        
    </style>
""", unsafe_allow_html=True)
created_style = """
    color: #888888; /* Light gray color */
    font-size: 99px; /* Increased font size */
""" 

def extract_transcript(video_id):
    """Extracts the transcript from a YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for transcript in transcript_list:
            transcript_text_list = transcript.fetch()
            lang = transcript.language
            transcript_text = ""
            if transcript.language_code == 'en':
                for line in transcript_text_list:
                    transcript_text += " " + line["text"]
                return transcript_text
            elif transcript.is_translatable:
                english_transcript_list = transcript.translate('en').fetch()
                for line in english_transcript_list:
                    transcript_text += " " + line["text"]
                return transcript_text
        st.info("Transcript extraction failed. Please check the video URL.")
    except Exception as e:
        st.info(f"Error: {e}")

         


st.markdown("<p style='{}'>➡️created by 'Muhammad Zain Attiq'</p>".format(created_style), unsafe_allow_html=True)
st.markdown('<h1 class="header">Youtube Video Transcriber </h1>', unsafe_allow_html=True)
with st.expander("About the app..."):
    st.markdown('<h1 class="head">What the App Can Do: </h1>', unsafe_allow_html=True)
    st.write("The YouTube Video Transcriber extracts transcripts from YouTube videos. It automatically detects the language and translates non-English transcripts to English. Users can preview videos and access transcripts in real-time.")

    st.markdown('<h1 class="head">How to use this app: </h1>', unsafe_allow_html=True)
    st.markdown("""
    1. Input the YouTube video URL.
    2. Preview the video.
    3. Click "Get Summary" to extract the transcript.
    4. View and use the transcript for analysis, summarization, or accessibility purposes.

    Developed by Muhammad Zain Attiq, the app offers a simple yet powerful tool for extracting and utilizing video transcripts.""")


video_url = st.text_input("Enter the video link: ")

if video_url:
    video_id = video_url.split("=")[1]
    st.video(video_url)
submit = st.button("Get Transcript")
if submit:
    with st.spinner("Extracting Transcript..."):
        transcript = extract_transcript(video_id)
        st.markdown('<h1 class="response">Transcript: </h1>', unsafe_allow_html=True)
        st.write(transcript)
        st.write("__________________________________________________________________________________")