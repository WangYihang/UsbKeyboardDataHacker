## Usage

```bash
$ python3 -m pip install poetry
$ git clone https://github.com/WangYihang/UsbKeyboardDataHacker.git
$ cd UsbKeyboardDataHacker
$ poetry install
$ poetry run python UsbKeyboardDataHacker.py --input tests/example.pcap

poetry run python UsbKeyboardDataHacker.py --input tests/example.pcap
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:16.777061, key='f'
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:16.914192, key=''
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:17.076812, key='l'
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:17.176842, key=''
...
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:36.514108, key=''
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:40.230170, key='', modifiers=left_ctrl
2024-10-15 21:47:39 ubuntu __main__[63413] INFO time=2017-03-23 09:07:40.330012, key='c', modifiers=left_ctrl
flag{pr355_0nwards_a2fee6e0}c
```


### Additional Video

* https://www.youtube.com/watch?v=unBwmcpXbhE

### References 

+ https://www.usb.org/sites/default/files/documents/hid1_11.pdf
+ https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf

## Acknowledgment

* [@ChristopherKai](https://github.com/ChristopherKai)
* [@seadog007](https://github.com/seadog007)
* [@hurricane618](https://github.com/hurricane618)
* [@BlueSky01st](https://github.com/BlueSky01st)
