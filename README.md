## Installation

```
python3 -m pip install poetry
poetry install
```

## Usage

```
poetry run python UsbKeyboardDataHacker.py ./example.pcap
```

```
Usage : 
        python UsbKeyboardHacker.py data.pcap
Tips : 
        To use this python script , you must install the tshark first.
        You can use `sudo apt-get install tshark` to install it
Author : 
        WangYihang <wangyihanger@gmail.com>
        If you have any questions , please contact me by email.
        Thank you for using.

```

## Example

### Step1: Get data

```
sun@ubuntu:~/UsbKeyboardDataHacker$ tshark -r ./example.pcap -T fields -e usb.capdata
00:00:09:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0f:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:04:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0a:00:00:00:00:00
00:00:00:00:00:00:00:00
20:00:00:00:00:00:00:00
20:00:2f:00:00:00:00:00
...
```

### Step2: decode

```
sun@ubuntu:~/UsbKeyboardDataHacker$ python UsbKeyboardDataHacker.py ./example.pcap 
[-] Unknow Key : 01
[-] Unknow Key : 01
[+] Found : flag{pr355_0nwards_a2fee6e0}
```

### Additional Video

* https://www.youtube.com/watch?v=unBwmcpXbhE


## Acknowledgment

* [@ChristopherKai](https://github.com/ChristopherKai)
* [@seadog007](https://github.com/seadog007)
* [@hurricane618](https://github.com/hurricane618)
* [@BlueSky01st](https://github.com/BlueSky01st)
