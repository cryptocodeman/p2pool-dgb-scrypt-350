from p2pool.bitcoin import networks

PARENT=networks.nets['digibyteday']
SHARE_PERIOD = 15
CHAIN_LENGTH = 1*24*60
REAL_CHAIN_LENGTH = 1*24*60
TARGET_LOOKBEHIND = 60
SPREAD = 30
IDENTIFIER = '31878C3D13481C8D'.decode('hex')
PREFIX = '2358B404B4781CD0'.decode('hex')
P2P_PORT = 5024
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5025
BOOTSTRAP_ADDRS = 'triplezen.tk'.split(' ')
ANNOUNCE_CHANNEL = '#triplezen'
VERSION_CHECK = lambda v: None if 6160400 <= v else 'DigiByte version too old. Upgrade to 6.16.4 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
