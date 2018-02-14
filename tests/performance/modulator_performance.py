import time

from urh.signalprocessing.Modulator import Modulator


def test_fsk_performance():
    bit_data = "10" * 100 + "0000011111" + "001101011" * 100 + "111111100000" * 100
    modulator = Modulator("Perf")
    modulator.modulation_type_str = "FSK"
    t = time.time()
    result = modulator.modulate(bit_data, pause=10000000)
    elapsed = time.time() - t

    result.tofile("/tmp/fsk.complex")
    print("FSK {}ms".format(elapsed * 1000))


def test_ask_performance():
    bit_data = "10" * 100 + "0000011111" + "001101011" * 100 + "111111100000" * 1000
    modulator = Modulator("Perf")
    modulator.modulation_type_str = "ASK"
    t = time.time()
    result = modulator.modulate(bit_data, pause=10000000)
    elapsed = time.time() - t

    result.tofile("/tmp/ask.complex")
    print("ASK {}ms".format(elapsed * 1000))


def test_psk_performance():
    bit_data = "10" * 100 + "0000011111" + "001101011" * 100 + "111111100000" * 1000
    modulator = Modulator("Perf")
    modulator.modulation_type_str = "PSK"
    t = time.time()
    result = modulator.modulate(bit_data, pause=10000000)
    elapsed = time.time() - t

    result.tofile("/tmp/psk.complex")
    print("PSK {}ms".format(elapsed * 1000))


if __name__ == '__main__':
    test_psk_performance()
