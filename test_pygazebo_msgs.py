#!/usr/bin/env python3

import asyncio

import pygazebo
import pygazebo.msg.joint_cmd_pb2

def callback(data):
    print("Received data")
    print(data)

async def subscriber(manager):
    subscriber = await manager.subscribe(
        '/gazebo/default/pioneer2dx/joint_cmd',
        'gazebo.msgs.JointCmd',
        callback
    )
    print("created the subscriber")
    print("Waiting for connection")
    await subscriber.wait_for_connection()
    print("Waiting for data")
    while True:
        await asyncio.sleep(1)

async def publish_loop():
    manager = await pygazebo.connect()

    publisher = await manager.advertise(
        '/gazebo/default/pioneer2dx/joint_cmd',
        'gazebo.msgs.JointCmd'
    )

    sub_task = asyncio.ensure_future(subscriber(manager))

    message = pygazebo.msg.joint_cmd_pb2.JointCmd()
    message.name = 'pioneer2dx::left_wheel_hinge'
    message.force = 100
    message.axis = 3
    # message.velocity.target = 3
    # message.velocity.p_gain = 1
    print(message)
    while True:
        print("sending message")
        await publisher.publish(message)
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(publish_loop())

# try:
#     import asyncio
# except ImportError:
#     import trollius as asyncio
#     from trollius import From
#
# import pygazebo
# import pygazebo.msg.joint_cmd_pb2
#
# @asyncio.coroutine
# def publish_loop():
#     manager = yield From(pygazebo.connect())
#     # model_name1 = "milanbot"
#     # model_name2 = "milanbot_0"
#
#     publisher = yield From(
#         manager.advertise(
#             # topic_name='/gazebo/default/milanbot/joint_cmd',
#             # msg_type='gazebo.msgs.JointCmd'
#             topic_name = '/gazebo/default/pioneer2dx/joint_cmd',
#             msg_type = 'gazebo.msgs.JointCmd'
#         ))
#
#     message = pygazebo.msg.joint_cmd_pb2.JointCmd()
#     # message.name = 'milanbot::left_wheel_hinge'
#     # message.axis = 0
#     # message.force = 1.0
#     message.name = 'pioneer2dx::left_wheel_hinge'
#     message.force = 100
#     message.axis = 3
#
#     print (message)
#     while True:
#         yield From(publisher.publish(message))
#         yield From(asyncio.sleep(1.0))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(publish_loop())
#
