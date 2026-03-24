#!/bin/bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.nexus.pantheon-api.plist 2>/dev/null
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.nexus.pantheon-api.plist
sleep 2
launchctl list | grep pantheon
