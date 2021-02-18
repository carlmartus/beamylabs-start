"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import os
import time
import binascii

import grpc

import sys

sys.path.append("../common/generated")

import network_api_pb2
import network_api_pb2_grpc
import system_api_pb2
import system_api_pb2_grpc
import common_pb2

sys.path.append("../common")
import helper
from helper import *

from threading import Thread, Timer


def read_signal(stub, signal):
    read_info = network_api_pb2.SignalIds(signalId=[signal])
    return stub.ReadSignals(read_info)


def publish_signals(client_id, stub, signals_with_payload):
    publisher_info = network_api_pb2.PublisherConfig(
        clientId=client_id,
        signals=network_api_pb2.Signals(signal=signals_with_payload),
        frequency=0,
    )
    try:
        stub.PublishSignals(publisher_info)
    except grpc._channel._Rendezvous as err:
        print(err)


increasing_counter = 0


# ecu_A publish some value (counter, and testFr06_Child02, TestFr04), then it reads other value (counter_times_2) (which has been published by ecu_B)
def ecu_A(stub, pause):
    while True:
        global increasing_counter
        namespace = "ecu_A"
        clientId = common_pb2.ClientId(id="id_ecu_A")
        # counter
        counter = common_pb2.SignalId(
            name="counter", namespace=common_pb2.NameSpace(name=namespace)
        )
        counter_with_payload = network_api_pb2.Signal(
            id=counter, integer=increasing_counter
        )
        # TestFr06_Child02 - another signal
        testFr06_Child02 = common_pb2.SignalId(
            name="TestFr06_Child02", namespace=common_pb2.NameSpace(name=namespace)
        )
        testFr06_Child02_with_payload = network_api_pb2.Signal(
            id=testFr06_Child02, integer=increasing_counter + 1
        )
        # TestFr04 - now a frame
        testFr04 = common_pb2.SignalId(
            name="TestFr04", namespace=common_pb2.NameSpace(name=namespace)
        )
        testFr04_with_payload = network_api_pb2.Signal(
            id=testFr04, integer=increasing_counter + 2
        )

        print("\necu_A, seed is ", increasing_counter)
        publish_signals(
            clientId,
            stub,
            [
                counter_with_payload,
                testFr06_Child02_with_payload,
                testFr04_with_payload,
            ],
        )

        time.sleep(pause)

        # read the other value and output result
        counter_times_2 = common_pb2.SignalId(
            name="counter_times_2", namespace=common_pb2.NameSpace(name=namespace)
        )
        read_counter_times_2 = read_signal(stub, counter_times_2)

        print(
            "ecu_A, (result) counter_times_2 is ",
            read_counter_times_2.signal[0].integer,
        )
        increasing_counter = (increasing_counter + 1) % 4


# read some value (counter) published by ecu_a
def ecu_B_read(stub, pause):
    while True:
        namespace = "ecu_B"
        client_id = common_pb2.ClientId(id="id_ecu_B")
        counter = common_pb2.SignalId(
            name="counter", namespace=common_pb2.NameSpace(name=namespace)
        )
        read_counter = read_signal(stub, counter)
        print("ecu_B, (read) counter is ", read_counter.signal[0].integer)

        time.sleep(pause)


# subscribe to some value (counter) published by ecu_a, double and send value back to eca_a (counter_times_2)
def ecu_B_subscribe(stub):
    namespace = "ecu_B"
    client_id = common_pb2.ClientId(id="id_ecu_B")
    counter = common_pb2.SignalId(
        name="counter", namespace=common_pb2.NameSpace(name=namespace)
    )

    sub_info = network_api_pb2.SubscriberConfig(
        clientId=client_id,
        signals=network_api_pb2.SignalIds(signalId=[counter]),
        onChange=True,
    )
    try:
        for subs_counter in stub.SubscribeToSignals(sub_info):
            print("ecu_B, (subscribe) counter is ", subs_counter.signal[0].integer)
            counter_times_2 = common_pb2.SignalId(
                name="counter_times_2", namespace=common_pb2.NameSpace(name=namespace)
            )
            signal_with_payload = network_api_pb2.Signal(
                id=counter_times_2, integer=subs_counter.signal[0].integer * 2
            )
            publish_signals(client_id, stub, [signal_with_payload])

    except grpc._channel._Rendezvous as err:
        print(err)


# shows possibiliy to subscribe to same signal muliple times
# also using array to subscribe to additonal signals
# logs on purpose tabbed with single space
def ecu_B_subscribe_2(stub):
    namespace = "ecu_B"
    # specify some signals
    client_id = common_pb2.ClientId(id="id_ecu_B")
    counter = common_pb2.SignalId(
        name="counter", namespace=common_pb2.NameSpace(name=namespace)
    )
    testFr06_Child02 = common_pb2.SignalId(
        name="TestFr06_Child02", namespace=common_pb2.NameSpace(name=namespace)
    )
    testFr04 = common_pb2.SignalId(
        name="TestFr04", namespace=common_pb2.NameSpace(name=namespace)
    )

    sub_info = network_api_pb2.SubscriberConfig(
        clientId=client_id,
        signals=network_api_pb2.SignalIds(
            signalId=[counter, testFr06_Child02, testFr04]
        ),
        onChange=True,
    )
    try:
        for response in stub.SubscribeToSignals(sub_info):
            # since we subscribe to a set of signal we need to check which arrived.
            for signal in response.signal:
                if signal.id.name == "counter":
                    print(" ecu_B, (subscribe_2) counter is ", signal.integer)
                if signal.id.name == "TestFr06_Child02":
                    print(
                        " ecu_B signal: "
                        + signal.id.name
                        + " arrived: "
                        + str(signal.integer)
                    )
                if signal.id.name == "TestFr04":
                    print(" ecu_B, (subscribe_2) raw is ", binascii.hexlify(signal.raw))

    except grpc._channel._Rendezvous as err:
        print(err)


# simple reading
# logs on purpose tabbed with double space
def read_on_timer(stub, signals, pause):
    while True:
        read_info = network_api_pb2.SignalIds(signalId=signals)
        try:
            response = stub.ReadSignals(read_info)
            for signal in response.signal:
                print(
                    "  read_on_timer "
                    + signal.id.name
                    + " value "
                    + str(signal.integer)
                )
        except grpc._channel._Rendezvous as err:
            print(err)
        time.sleep(pause)


def run():
    # allows to custom set message max size. (default 4Mb, 4194304)
    # MAX_MESSAGE_LENGTH = 6000000
    # channel = grpc.insecure_channel('127.0.0.1:50051', options=[
    #     ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
    #     ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    #     ],
    # )
    channel = grpc.insecure_channel("127.0.0.1:50051")
    network_stub = network_api_pb2_grpc.NetworkServiceStub(channel)
    system_stub = system_api_pb2_grpc.SystemServiceStub(channel)
    check_license(system_stub)
    # request_license(system_stub)
    # download_and_install_license(system_stub, "your_emailed_hash")

    upload_folder(system_stub, "configuration_udp")
    # upload_folder(system_stub, "configuration_lin")
    # upload_folder(system_stub, "configuration_can")
    # upload_folder(system_stub, "configuration_canfd")
    reload_configuration(system_stub)

    # list available signals
    configuration = system_stub.GetConfiguration(common_pb2.Empty())
    for networkInfo in configuration.networkInfo:
        print(
            "signals in namespace ",
            networkInfo.namespace.name,
            system_stub.ListSignals(networkInfo.namespace),
        )

    ecu_A_thread = Thread(
        target=ecu_A,
        args=(
            network_stub,
            1,
        ),
    )
    ecu_A_thread.start()

    ecu_B_thread_read = Thread(
        target=ecu_B_read,
        args=(
            network_stub,
            1,
        ),
    )
    ecu_B_thread_read.start()

    ecu_B_thread_subscribe = Thread(target=ecu_B_subscribe, args=(network_stub,))
    ecu_B_thread_subscribe.start()

    ecu_B_thread_subscribe_2 = Thread(target=ecu_B_subscribe_2, args=(network_stub,))
    ecu_B_thread_subscribe_2.start()

    read_signals = [
        common_pb2.SignalId(
            name="counter", namespace=common_pb2.NameSpace(name="ecu_A")
        ),
        common_pb2.SignalId(
            name="TestFr06_Child02", namespace=common_pb2.NameSpace(name="ecu_A")
        ),
    ]
    ecu_read_demo = Thread(target=read_on_timer, args=(network_stub, read_signals, 10))
    ecu_read_demo.start()


if __name__ == "__main__":
    run()
