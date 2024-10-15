#!/usr/bin/env python

import sys
import os
import logging
import subprocess

DataFileName = "usb.dat"

presses = []

normalKeys = {"04":"a", "05":"b", "06":"c", "07":"d", "08":"e", "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j", "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o", "13":"p", "14":"q", "15":"r", "16":"s", "17":"t", "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y", "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4", "22":"5", "23":"6","24":"7","25":"8","26":"9","27":"0","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\","32":"<NON>","33":";","34":"'","35":"<GA>","36":",","37":".","38":"/","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>","54":"/","55":"*","56":"-","57":"+","59":"1","5a":"2","5b":"3","5c":"4","5d":"5","5e":"6","5f":"7","60":"8","61":"9","62":"0","63":".","67":"="}

shiftKeys = {"04":"A", "05":"B", "06":"C", "07":"D", "08":"E", "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J", "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T", "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y", "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$", "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>","2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":":","34":"\"","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_pcap_file(pcapFilePath):
    try:
        subprocess.run(["tshark", "-r", pcapFilePath, "-T", "fields", "-e", "usb.capdata", "usb.data_len == 8"], check=True, stdout=open(DataFileName, "w"))
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running tshark: {e}")
        sys.exit(1)

def read_data_file():
    try:
        with open(DataFileName, "r") as f:
            for line in f:
                presses.append(line.strip())
    except IOError as e:
        logging.error(f"Error reading data file: {e}")
        sys.exit(1)

def process_presses():
    result = ""
    for press in presses:
        if not press:
            continue
        Bytes = press.split(":") if ':' in press else [press[i:i+2] for i in range(0, len(press), 2)]
        if Bytes[0] == "00":
            if Bytes[2] != "00" and normalKeys.get(Bytes[2]):
                result += normalKeys[Bytes[2]]
        elif int(Bytes[0], 16) & 0b10 or int(Bytes[0], 16) & 0b100000:  # shift key is pressed.
            if Bytes[2] != "00" and shiftKeys.get(Bytes[2]):
                result += shiftKeys[Bytes[2]]
        else:
            logging.warning(f"Unknown Key: {Bytes[0]}")
    return result

def main():
    setup_logging()
    
    if len(sys.argv) != 2:
        logging.error("Usage: python UsbKeyboardHacker.py data.pcap")
        logging.info("Tips: To use this python script, you must install tshark first.")
        logging.info("You can use `sudo apt-get install tshark` to install it")
        logging.info("Author: WangYihang <wangyihanger@gmail.com>")
        sys.exit(1)

    pcapFilePath = sys.argv[1]
    
    parse_pcap_file(pcapFilePath)
    read_data_file()
    
    result = process_presses()
    logging.info(f"Found: {result}")

    try:
        os.remove(DataFileName)
    except OSError as e:
        logging.error(f"Error removing temporary data file: {e}")

if __name__ == "__main__":
    main()
