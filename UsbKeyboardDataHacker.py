#!/usr/bin/env python

import sys
import os
import argparse
import pyshark
from config import KEY_MAPPINGS
import coloredlogs
import logging
import datetime

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

def parse_pcap_file(filepath):
    cap = pyshark.FileCapture(filepath)
    for packet in cap:
        if hasattr(packet, "DATA"):
            usbhid_data = packet.DATA.get_field("usbhid_data")
            usb_capdata = packet.DATA.get_field("usb_capdata")
            timestamp = float(packet.sniff_timestamp)
            for data in [usbhid_data, usb_capdata]:
                if data:
                    yield (timestamp, data)


def process_key(timestamp, press):
    items = [int(i, 16) for i in press.split(":")]
    if len(items) != 8:
        return
    modifier_keys, _, key1, _, _, _, _, _ = items
    """
    Bit Key 
        0 LEFT CTRL
        1 LEFT SHIFT
        2 LEFT ALT
        3 LEFT GUI 
        4 RIGHT CTRL
        5 RIGHT SHIFT
        6 RIGHT ALT
        7 RIGHT GUI 

    [1] https://www.usb.org/sites/default/files/documents/hid1_11.pdf
    """
    left_ctrl = (modifier_keys >> 0) & 0x01
    left_shift = (modifier_keys >> 1) & 0x01
    left_alt = (modifier_keys >> 2) & 0x01
    left_gui = (modifier_keys >> 3) & 0x01
    right_ctrl = (modifier_keys >> 4) & 0x01
    right_shift = (modifier_keys >> 5) & 0x01
    right_alt = (modifier_keys >> 6) & 0x01
    right_gui = (modifier_keys >> 7) & 0x01

    """
    10 Keyboard/Keypad Page (0x07)

    [2] https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
    """
    key1 = KEY_MAPPINGS.get(key1, ("", ""))[1 if (left_shift or right_shift) else 0]
    keys = [key1]
    if left_ctrl:
        keys.append("<LEFT_CTRL>")
    if left_shift:
        keys.append("<LEFT_SHIFT>")
    if left_alt:
        keys.append("<LEFT_ALT>")
    if left_gui:
        keys.append("<LEFT_GUI>")
    if right_ctrl:
        keys.append("<RIGHT_CTRL>")
    if right_shift:
        keys.append("<RIGHT_SHIFT>")
    if right_alt:
        keys.append("<RIGHT_ALT>")
    if right_gui:
        keys.append("<RIGHT_GUI>")
    keys.sort()
    pressed_modifiers = []
    if left_ctrl:
        pressed_modifiers.append("left_ctrl")
    if left_shift:
        pressed_modifiers.append("left_shift")
    if left_alt:
        pressed_modifiers.append("left_alt")
    if left_gui:
        pressed_modifiers.append("left_gui")
    if right_ctrl:
        pressed_modifiers.append("right_ctrl")
    if right_shift:
        pressed_modifiers.append("right_shift")
    if right_alt:
        pressed_modifiers.append("right_alt")
    if right_gui:
        pressed_modifiers.append("right_gui")
    
    modifiers_str = ", ".join(pressed_modifiers)
    formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
    logger.info(f"time={formatted_time}, key={repr(key1)}" + (f", modifiers={modifiers_str}" if modifiers_str else ""))
    return key1


def main():
    parser = argparse.ArgumentParser(description="UsbKeyboardDataHacker")
    parser.add_argument("--input", help="input pcap file path", required=True)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        logger.error(f"Input file does not exist: {args.input}")
        sys.exit(1)

    buffer = []
    for timestamp, press in parse_pcap_file(args.input):
        key = process_key(timestamp, press)
        if key:
            buffer.append(key)
    print("".join(buffer))


if __name__ == "__main__":
    main()
