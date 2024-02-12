from dialog import SpeechCloudWS, Dialog
import logging
import json
import urllib.request
import asyncio

class DemoDescriptionDM(Dialog):

    async def main(self):

        await asyncio.sleep(36000000)   


    def on_receive_message(self, data):
        # dostane zpravu od js
        session = self.session_id # DM koukne na svoji session_id
        msg = json.loads(data) # nacte zpravu 
        topic = msg['topic'] # koukne na topic
        print('Webserver: Received WS message:', data)

        try:
            if(topic =='ASR_audio'):
                print("ASR audio came")
                #patientName = msg["lname"] + msg["fname"]
                url = msg["msg"]["uri"]
                record_id = msg["msg"]["id"]
                # with open(f"data/{session}/records/{record_id}.json", "w") as record_file:
                #     json.dump(msg, record_file)
                # urllib.request.urlretrieve(url, f"data/{session}/records/{record_id}.wav")
        except (ValueError):
            print('Webserver: Received WS message:', data)
        except (KeyError):
            print('Webserver: Received WS message:', data)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-10s %(message)s',level=logging.DEBUG)

    SpeechCloudWS.run(DemoDescriptionDM, address="0.0.0.0", port=8888, static_path='./static')