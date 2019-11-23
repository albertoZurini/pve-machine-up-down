# PVE Machine up Down

Simple script which pings a PVE (Proxmox) host and in the case the host is down will automatically turn on some PVE VMs.
When the other hosts cames up all machines will be shut down.

# Why this instead of a cluster?

This script is much versatile than configuring a Cluster.

# How to edit

Edit the `settings.json` file and set `remoteAddress` with the other PVE host IP address and the array `vmIds` with all the VMs which will be turned on when the other host is down.