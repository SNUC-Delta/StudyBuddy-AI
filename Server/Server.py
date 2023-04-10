# import asyncio
# import websockets


# # create handler for each connection

# async def handler(websocket):
#     while True:
#         data = await websocket.recv()
#         reply = f"Data recieved as:  {data}!"
#         print(reply)


# async def main():
#     print("Started!")
#     async with websockets.serve(handler, "localhost", 5000):
#         await asyncio.Future()
# asyncio.run(main())

import asyncio
import websockets
import wave
import struct

# create handler for each connection


async def handler(websocket):
    while True:
        data = await websocket.recv()
        print(data)
        # pprint.pprint(data)
        with open("data.bin", "wb") as f:
            f.write(data)
        channels = 1
        sample_width = 2  # 16-bit
        frame_rate = 44100
        n_frames = 200  # number of frames to write
        comptype = "NONE"
        compname = "not compressed"

        with wave.open("output.wav", "w") as wav_file:
            wav_file.setparams(
                (channels, sample_width, frame_rate, n_frames, comptype, compname))
            with open("data.bin", "rb") as bin_file:
                data = bin_file.read(2)
                while data:
                    # convert the 2 bytes to a signed 16-bit integer
                    sample = struct.unpack("<h", data)[0]
                    # write the sample to the WAV file
                    wav_file.writeframesraw(struct.pack("<h", sample))
                    data = bin_file.read(2)


async def main():
    print("Started!")
    async with websockets.serve(handler, "localhost", 5000):
        await asyncio.Future()
asyncio.run(main())
