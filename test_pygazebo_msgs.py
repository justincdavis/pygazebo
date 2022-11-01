#!/usr/bin/env python3

import asyncio

import pygazebo
import pygazebo.msg.joint_cmd_pb2


async def publish_loop():
    manager = await pygazebo.connect()

    publisher = await manager.advertise(
        '/gazebo/default/pioneer2dx/joint_cmd',
        'gazebo.msgs.JointCmd')

    message = pygazebo.msg.joint_cmd_pb2.JointCmd()
    message.name = 'pioneer2dx::left_wheel_hinge'
    message.force = 100
    message.axis = 3
    print(message)
    while True:
        await publisher.publish(message)
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(publish_loop())
