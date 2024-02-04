import boto3

# Initialize the Amazon Transcribe client
transcribe = boto3.client('transcribe') 

# Define the audio file path and name
file_name = 'audio_file.wav'

# Start a transcription job
job = transcribe.start_transcription_job(
    TranscriptionJobName='TranscriptionJob',
    Media={'MediaFileUri': 's3://bucket/'+file_name}, 
    MediaFormat='wav',
    LanguageCode='en-US'
)

# Wait for the transcription job to complete
job = transcribe.get_transcription_job(TranscriptionJobName=job['TranscriptionJob']['TranscriptionJobName'])
while(job['TranscriptionJob']['TranscriptionJobStatus'] != 'COMPLETED'):
    job = transcribe.get_transcription_job(TranscriptionJobName=job['TranscriptionJob']['TranscriptionJobName'])

# Get the transcription results
results = transcribe.get_transcription_job(TranscriptionJobName=job['TranscriptionJob']['TranscriptionJobName'])['TranscriptionJob']['Transcript']['TranscriptFileUri']

# Print the transcription
print(results)