#!/usr/local/bin/python3

# CCloud Watcher v0.1

# Dirty dirty hack script to interogate Confluent Cloud
# and be able to point fingers at users using too many
# clusters

# really, it's dirty... don't use this

import json, subprocess

cmd = "/usr/local/bin/ccloud "
cmd_env_list = f"{cmd} environment list -o json "
cmd_env_use = f"{cmd} environment use "
cmd_cluster_list = f"{cmd} kafka cluster list -o json "
cmd_cluster_use = f"{cmd} kafka cluster use "

# get all environments
s = subprocess.check_output(cmd_env_list, shell=True, text=True)
j = json.loads(s)

# for each environment, get each cluster
for e in j:
    print("{name} ({id})".format(**e))
    # use this environment
    # SECURITY RISK HERE: if an id contained semi-colons, could inject commands
    s = subprocess.check_output(cmd_env_use + e["id"], shell=True, text=True)
    # get the list of clusters in this environment
    s = subprocess.check_output(cmd_cluster_list, shell=True, text=True)
    clusters = json.loads(s)
    for c in clusters:
        print("\tid: {id}, name: {name}, type: {type}".format(**c))

    print ("-"*42)
