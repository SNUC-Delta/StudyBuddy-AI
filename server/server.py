import asyncio
import websockets
import wave
import struct
import uuid
import summarization
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
load_dotenv()

cloudinary.config(
    cloud_name="",
    api_key="",
    api_secret="",
    secure=True
)


async def sockHandler(webSocket):
    unID = uuid.uuid1()
    # Makes the Websocket Server stay alive for Audio Receival
    while True:
        try:
            data_chunk = await webSocket.recv()
            if data_chunk == "Done":
                break
        except websockets.ConnectionClosed:
            break
        with open(f"./dist/Bin/{unID}_data.bin", "ab+") as f:
            f.write(data_chunk)

    configDict = {
        "channelNumber": 1,
        "sampleWidth": 2,
        "frameRate": 44100,
        "noOfFrames": 200,
        "compType": "NONE",
        "compName": "not compressed"

    }

    with wave.open(f"./dist/Audio/{unID}_output.wav", "w") as wav_file:

        wav_file.setparams(
            (configDict["channelNumber"],
             configDict["sampleWidth"],
             configDict["frameRate"],
             configDict["noOfFrames"],
             configDict["compType"],
             configDict["compName"]))

        with open(f"./dist/Bin/{unID}_data.bin", "rb") as binFile:
            data_chunk = binFile.read(2)
            while data_chunk:
                # convert the 2 bytes to a signed 16-bit integer
                sample = struct.unpack("<h", data_chunk)[0]
                # write the sample to the WAV file
                wav_file.writeframesraw(struct.pack("<h", sample))
                data_chunk = binFile.read(2)
        summarization.summary(
            f"./dist/Audio/4b45207c-dab8-11ed-a574-00155ddfeb0b_output.wav", unID)
        cloudinary.uploader.upload(
            f"./dist/PDF/{unID}_pdf.pdf", public_id=f"{unID}_pdf")
        srcURL = cloudinary.CloudinaryResource(f"{unID}_pdf").build_url()
        await webSocket.send(srcURL)


async def main():
    print("[INFO] WEBSOCKET STARTED AT -- localhost:5000")
    async with websockets.serve(sockHandler, "localhost", 5000):
        await asyncio.Future()
asyncio.run(main())
