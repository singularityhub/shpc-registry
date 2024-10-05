---
layout: container
name:  "quay.io/biocontainers/profile_dists"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/profile_dists/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/profile_dists/container.yaml"
updated_at: "2024-10-05 03:28:18.854111"
latest: "1.0.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/profile_dists"
aliases:
 - "cmtime"
 - "cpuinfo"
 - "ib_acme"
 - "ibv_asyncwatch"
 - "ibv_devices"
 - "ibv_devinfo"
 - "ibv_rc_pingpong"
 - "ibv_srq_pingpong"
 - "ibv_uc_pingpong"
 - "ibv_ud_pingpong"
 - "ibv_xsrq_pingpong"
 - "mckey"
 - "profile_dists"
 - "protoc-24.3.0"
 - "rcopy"
 - "rdma_client"
 - "rdma_server"
 - "rdma_xclient"
 - "rdma_xserver"
 - "riostream"
 - "rping"
 - "rstream"
 - "ucmatose"
 - "udaddy"
 - "udpong"
 - "h5fuse.sh"
 - "io_demo"
 - "ucx_info"
 - "ucx_perftest"
 - "ucx_read_profile"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "produce_x_platform_fuzz_corpus"
 - "run_x_platform_fuzz_corpus"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "sha256_profile"
 - "h5delete"
 - "gflags_completions.sh"
 - "pt2to3"
versions:
 - "1.0.0--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for profile_dists"
config: {"url": "https://biocontainers.pro/tools/profile_dists", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for profile_dists", "latest": {"1.0.0--pyh7cba7a3_0": "sha256:1dba60a50a9665d3bedd1cedd56dc0801d9669c508fe0ea3083944601ef02561"}, "tags": {"1.0.0--pyh7cba7a3_0": "sha256:1dba60a50a9665d3bedd1cedd56dc0801d9669c508fe0ea3083944601ef02561"}, "docker": "quay.io/biocontainers/profile_dists", "aliases": {"cmtime": "/usr/local/bin/cmtime", "cpuinfo": "/usr/local/bin/cpuinfo", "ib_acme": "/usr/local/bin/ib_acme", "ibv_asyncwatch": "/usr/local/bin/ibv_asyncwatch", "ibv_devices": "/usr/local/bin/ibv_devices", "ibv_devinfo": "/usr/local/bin/ibv_devinfo", "ibv_rc_pingpong": "/usr/local/bin/ibv_rc_pingpong", "ibv_srq_pingpong": "/usr/local/bin/ibv_srq_pingpong", "ibv_uc_pingpong": "/usr/local/bin/ibv_uc_pingpong", "ibv_ud_pingpong": "/usr/local/bin/ibv_ud_pingpong", "ibv_xsrq_pingpong": "/usr/local/bin/ibv_xsrq_pingpong", "mckey": "/usr/local/bin/mckey", "profile_dists": "/usr/local/bin/profile_dists", "protoc-24.3.0": "/usr/local/bin/protoc-24.3.0", "rcopy": "/usr/local/bin/rcopy", "rdma_client": "/usr/local/bin/rdma_client", "rdma_server": "/usr/local/bin/rdma_server", "rdma_xclient": "/usr/local/bin/rdma_xclient", "rdma_xserver": "/usr/local/bin/rdma_xserver", "riostream": "/usr/local/bin/riostream", "rping": "/usr/local/bin/rping", "rstream": "/usr/local/bin/rstream", "ucmatose": "/usr/local/bin/ucmatose", "udaddy": "/usr/local/bin/udaddy", "udpong": "/usr/local/bin/udpong", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "io_demo": "/usr/local/bin/io_demo", "ucx_info": "/usr/local/bin/ucx_info", "ucx_perftest": "/usr/local/bin/ucx_perftest", "ucx_read_profile": "/usr/local/bin/ucx_read_profile", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "produce_x_platform_fuzz_corpus": "/usr/local/bin/produce_x_platform_fuzz_corpus", "run_x_platform_fuzz_corpus": "/usr/local/bin/run_x_platform_fuzz_corpus", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "sha256_profile": "/usr/local/bin/sha256_profile", "h5delete": "/usr/local/bin/h5delete", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "pt2to3": "/usr/local/bin/pt2to3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/profile_dists.
singularity registry hpc automated addition for profile_dists
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/profile_dists
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/profile_dists:1.0.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/profile_dists/1.0.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/profile_dists/1.0.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### profile_dists-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### profile_dists-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### profile_dists-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### profile_dists-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### profile_dists-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### profile_dists-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cmtime

```bash
$ singularity exec <container> /usr/local/bin/cmtime
$ podman run --it --rm --entrypoint /usr/local/bin/cmtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ib_acme

```bash
$ singularity exec <container> /usr/local/bin/ib_acme
$ podman run --it --rm --entrypoint /usr/local/bin/ib_acme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ib_acme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_asyncwatch

```bash
$ singularity exec <container> /usr/local/bin/ibv_asyncwatch
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_asyncwatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_asyncwatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_devices

```bash
$ singularity exec <container> /usr/local/bin/ibv_devices
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_devices   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_devices   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_devinfo

```bash
$ singularity exec <container> /usr/local/bin/ibv_devinfo
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_devinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_devinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_rc_pingpong

```bash
$ singularity exec <container> /usr/local/bin/ibv_rc_pingpong
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_rc_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_rc_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_srq_pingpong

```bash
$ singularity exec <container> /usr/local/bin/ibv_srq_pingpong
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_srq_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_srq_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_uc_pingpong

```bash
$ singularity exec <container> /usr/local/bin/ibv_uc_pingpong
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_uc_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_uc_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_ud_pingpong

```bash
$ singularity exec <container> /usr/local/bin/ibv_ud_pingpong
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_ud_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_ud_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibv_xsrq_pingpong

```bash
$ singularity exec <container> /usr/local/bin/ibv_xsrq_pingpong
$ podman run --it --rm --entrypoint /usr/local/bin/ibv_xsrq_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibv_xsrq_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mckey

```bash
$ singularity exec <container> /usr/local/bin/mckey
$ podman run --it --rm --entrypoint /usr/local/bin/mckey   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mckey   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profile_dists

```bash
$ singularity exec <container> /usr/local/bin/profile_dists
$ podman run --it --rm --entrypoint /usr/local/bin/profile_dists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profile_dists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-24.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-24.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-24.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-24.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcopy

```bash
$ singularity exec <container> /usr/local/bin/rcopy
$ podman run --it --rm --entrypoint /usr/local/bin/rcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdma_client

```bash
$ singularity exec <container> /usr/local/bin/rdma_client
$ podman run --it --rm --entrypoint /usr/local/bin/rdma_client   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdma_client   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdma_server

```bash
$ singularity exec <container> /usr/local/bin/rdma_server
$ podman run --it --rm --entrypoint /usr/local/bin/rdma_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdma_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdma_xclient

```bash
$ singularity exec <container> /usr/local/bin/rdma_xclient
$ podman run --it --rm --entrypoint /usr/local/bin/rdma_xclient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdma_xclient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdma_xserver

```bash
$ singularity exec <container> /usr/local/bin/rdma_xserver
$ podman run --it --rm --entrypoint /usr/local/bin/rdma_xserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdma_xserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### riostream

```bash
$ singularity exec <container> /usr/local/bin/riostream
$ podman run --it --rm --entrypoint /usr/local/bin/riostream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/riostream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rping

```bash
$ singularity exec <container> /usr/local/bin/rping
$ podman run --it --rm --entrypoint /usr/local/bin/rping   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rping   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstream

```bash
$ singularity exec <container> /usr/local/bin/rstream
$ podman run --it --rm --entrypoint /usr/local/bin/rstream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rstream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucmatose

```bash
$ singularity exec <container> /usr/local/bin/ucmatose
$ podman run --it --rm --entrypoint /usr/local/bin/ucmatose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucmatose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### udaddy

```bash
$ singularity exec <container> /usr/local/bin/udaddy
$ podman run --it --rm --entrypoint /usr/local/bin/udaddy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udaddy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### udpong

```bash
$ singularity exec <container> /usr/local/bin/udpong
$ podman run --it --rm --entrypoint /usr/local/bin/udpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io_demo

```bash
$ singularity exec <container> /usr/local/bin/io_demo
$ podman run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_info

```bash
$ singularity exec <container> /usr/local/bin/ucx_info
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_read_profile

```bash
$ singularity exec <container> /usr/local/bin/ucx_read_profile
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_read_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_read_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub5

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub5
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_app

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_app
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### produce_x_platform_fuzz_corpus

```bash
$ singularity exec <container> /usr/local/bin/produce_x_platform_fuzz_corpus
$ podman run --it --rm --entrypoint /usr/local/bin/produce_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/produce_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_x_platform_fuzz_corpus

```bash
$ singularity exec <container> /usr/local/bin/run_x_platform_fuzz_corpus
$ podman run --it --rm --entrypoint /usr/local/bin/run_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-contents

```bash
$ singularity exec <container> /usr/local/bin/orc-contents
$ podman run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-metadata

```bash
$ singularity exec <container> /usr/local/bin/orc-metadata
$ podman run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-statistics

```bash
$ singularity exec <container> /usr/local/bin/orc-statistics
$ podman run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sha256_profile

```bash
$ singularity exec <container> /usr/local/bin/sha256_profile
$ podman run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)