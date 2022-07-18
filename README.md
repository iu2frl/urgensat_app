# urgensat_app
## Software versions
- GnuRadio 3.7.13.5
- Python 2.7

## Install procedure (tested Ubuntu 18.04 LTS)
- Add GnuRadio 3.7 repo `sudo add-apt-repository ppa:gnuradio/gnuradio-releases-3.7`
- Install GnuRadio `sudo apt install gnuradio`
  - Additional dependencies (Python 2.7) should be automatically installed
- Clone repo `git clone git@github.com:iu2frl/urgensat_app.git`
- Open dir `cd urgensat_app`
- Install Python requirements `pip install -r requirements.txt`
- ...

## Features list
### General
- [x] Add event logger
- [x] Add optional packet logger
- [x] Add message handler
- [x] Change message encoding to comply with [MessagePack](https://msgpack.org/)
- [x] Convert from UDP to TCP
- [ ] Create `io_controller` to control remote devices
- [ ] Automate core run
- [ ] Create full-screen CLI version
- [ ] Create install script
- [ ] Add file send/receive capability
- [ ] Create multi-thread version

### Command handler
- [ ] Manage `station_info()` function
- [ ] Use regex for special commands
- [x] Manage exceptions

### Rx deamon
- [x] Add handler to send messages to MessageHandler
- [ ] Manage exceptions
