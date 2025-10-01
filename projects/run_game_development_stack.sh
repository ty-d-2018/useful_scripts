#!/bin/bash

nohup run_godot.sh > godot_log.log 2>&1 &

nohup blender > blender_log.log 2>&1 &