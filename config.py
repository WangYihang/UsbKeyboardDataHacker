"""
[1] https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
"""

# KEY_MAPPINGS stores the mapping of the key codes to the actual keys
# The key codes are the values of the dictionary
# The actual keys are the values of the dictionary
# The first value is the key when the shift key is not pressed
# The second value is the key when the shift key is pressed
KEY_MAPPINGS = {
    0x01: ("<ErrorRollOver>", "<ErrorRollOver>"),
    0x02: ("<PostFail>", "<PostFail>"),
    0x03: ("<ErrorUndefined>", "<ErrorUndefined>"),

    0x04: ("a", "A"), 
    0x05: ("b", "B"), 
    0x06: ("c", "C"), 
    0x07: ("d", "D"), 
    0x08: ("e", "E"), 
    0x09: ("f", "F"), 
    0x0A: ("g", "G"), 
    0x0B: ("h", "H"), 
    0x0C: ("i", "I"), 
    0x0D: ("j", "J"), 
    0x0E: ("k", "K"), 
    0x0F: ("l", "L"), 
    0x10: ("m", "M"), 
    0x11: ("n", "N"), 
    0x12: ("o", "O"), 
    0x13: ("p", "P"), 
    0x14: ("q", "Q"), 
    0x15: ("r", "R"), 
    0x16: ("s", "S"), 
    0x17: ("t", "T"), 
    0x18: ("u", "U"), 
    0x19: ("v", "V"), 
    0x1A: ("w", "W"), 
    0x1B: ("x", "X"), 
    0x1C: ("y", "Y"), 
    0x1D: ("z", "Z"), 

    0x1E: ("1", "!"), 
    0x1F: ("2", "@"), 
    0x20: ("3", "#"), 
    0x21: ("4", "$"), 
    0x22: ("5", "%"), 
    0x23: ("6", "^"), 
    0x24: ("7", "&"), 
    0x25: ("8", "*"), 
    0x26: ("9", "("), 
    0x27: ("0", ")"), 

    0x28: ("<RET>", "<RET>"), 
    0x29: ("<ESC>", "<ESC>"), 
    0x2A: ("<DEL>", "<DEL>"), 
    0x2B: ("\t", "\t"), 
    0x2C: ("<SPACE>", "<SPACE>"), 
    0x2D: ("-", "_"), 
    0x2E: ("=", "+"), 
    0x2F: ("[", "{"), 
    0x30: ("]", "}"), 
    0x31: ("\\", "|"), 
    0x32: ("<NON>", "<NON>"), 
    0x33: (";", ":"), 
    0x34: ("'", "\""), 
    0x35: ("<GA>", "<GA>"), 
    0x36: (",", "<"), 
    0x37: (".", ">"), 
    0x38: ("/", "?"), 
    0x39: ("<CAP>", "<CAP>"), 

    0x3A: ("<F1>", "<F1>"), 
    0x3B: ("<F2>", "<F2>"), 
    0x3C: ("<F3>", "<F3>"), 
    0x3D: ("<F4>", "<F4>"), 
    0x3E: ("<F5>", "<F5>"), 
    0x3F: ("<F6>", "<F6>"), 
    0x40: ("<F7>", "<F7>"), 
    0x41: ("<F8>", "<F8>"), 
    0x42: ("<F9>", "<F9>"), 
    0x43: ("<F10>", "<F10>"), 
    0x44: ("<F11>", "<F11>"), 
    0x45: ("<F12>", "<F12>"), 

    0x46: ("<PrintScreen>", "<PrintScreen>"),
    0x47: ("<Scroll Lock>", "<Scroll Lock>"),
    0x48: ("<Pause>", "<Pause>"),
    0x49: ("<Insert>", "<Insert>"),
    0x4A: ("<Home>", "<Home>"),
    0x4B: ("<PageUp>", "<PageUp>"),
    0x4C: ("<Delete Forward>", "<Delete Forward>"),
    0x4D: ("<End>", "<End>"),
    0x4E: ("<PageDown>", "<PageDown>"),
    0x4F: ("<RightArrow>", "<RightArrow>"),
    0x50: ("<LeftArrow>", "<LeftArrow>"),
    0x51: ("<DownArrow>", "<DownArrow>"),
    0x52: ("<UpArrow>", "<UpArrow>"),
    0x53: ("<Num Lock>", "<Clear>"),

    0x54: ("/", "/"),
    0x55: ("*", "*"),
    0x56: (".", "."),
    0x57: ("+", "+"),

    0x58: ("<Enter>", "<Enter>"),

    0x59: ("1", "<End>"),
    0x5A: ("2", "<Down Arrow>"),
    0x5B: ("3", "<PageDn>"),
    0x5C: ("4", "<Left Arrow>"),
    0x5D: ("5", "5"),
    0x5E: ("6", "<Right Arrow>"),
    0x5F: ("7", "<Home>"),
    0x60: ("8", "<Up Arrow>"),
    0x61: ("9", "<PageUp>"), 
    0x62: ("0", "<Insert>"), 
    0x63: (".", "<Delete>"), 

    0x64: ("<Non-US>", "|"),
    0x65: ("<Application>", "<Application>"),
    0x66: ("<Power>", "<Power>"),

    0x67: ("=", ""), 

    0x68: ("<F13>", "<F13>"),
    0x69: ("<F14>", "<F14>"),
    0x6A: ("<F15>", "<F15>"),
    0x6B: ("<F16>", "<F16>"),
    0x6C: ("<F17>", "<F17>"),
    0x6D: ("<F18>", "<F18>"),
    0x6E: ("<F19>", "<F19>"),
    0x6F: ("<F20>", "<F20>"),
    0x70: ("<F21>", "<F21>"),
    0x71: ("<F22>", "<F22>"),
    0x72: ("<F23>", "<F23>"),
    0x73: ("<F24>", "<F24>"),
    0x74: ("<Execute>", "<Execute>"),
    0x75: ("<Help>", "<Help>"),
    0x76: ("<Menu>", "<Menu>"),
    0x77: ("<Select>", "<Select>"),
    0x78: ("<Stop>", "<Stop>"),
    0x79: ("<Again>", "<Again>"),
    0x7A: ("<Undo>", "<Undo>"),
    0x7B: ("<Cut>", "<Cut>"),
    0x7C: ("<Copy>", "<Copy>"),
    0x7D: ("<Paste>", "<Paste>"),
    0x7E: ("<Find>", "<Find>"),
    0x7F: ("<Mute>", "<Mute>"),
    0x80: ("<Volume Up>", "<Volume Up>"),
    0x81: ("<Volume Down>", "<Volume Down>"),
    0x82: ("<Locking Caps Lock>", "<Locking Caps Lock>"),
    0x83: ("<Locking Num Lock>", "<Locking Num Lock>"),
    0x84: ("<Locking Scroll Lock>", "<Locking Scroll Lock>"),
    0x85: ("<Comma>", "<Comma>"),
    0x86: ("<Equal Sign>", "<Equal Sign>"),

    # ...
    # see: https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
}
