---
layout: container
name:  "quay.io/biocontainers/arborator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arborator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arborator/container.yaml"
updated_at: "2025-09-19 03:50:07.751522"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/arborator"
aliases:
 - "arborator"
 - "gas"
 - "profile_dists"
 - "cpuinfo"
 - "h5tools_test_utils"
 - "cmtime"
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
 - "io_demo"
versions:
 - "1.0.0--pyhdfd78af_1"
 - "1.0.0--pyhdfd78af_3"
 - "1.0.0--pyhdfd78af_4"
 - "1.0.0--pyhdfd78af_5"
 - "1.0.6--pyhdfd78af_0"
 - "1.0.6--pyhdfd78af_1"
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for arborator"
config: {"url": "https://biocontainers.pro/tools/arborator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for arborator", "latest": {"1.1.0--pyhdfd78af_0": "sha256:20cff7136b53acd3f1516c6abb1e66df0699f35adba30351d7976fa5945ffeb8"}, "tags": {"1.0.0--pyhdfd78af_1": "sha256:be154ce9cdd3f34454de606e699b7a7b0d301698f360c71244089af8875fd71e", "1.0.0--pyhdfd78af_3": "sha256:eb0f51aead91f40a0fd44a7c3fe758cc8c901ff6a48a8d2420ed4a20f4ee028b", "1.0.0--pyhdfd78af_4": "sha256:624e7cc690c3361efd4ffceb0fdb1782ed847be05f0b5ee7258aa6dd8ae30ccf", "1.0.0--pyhdfd78af_5": "sha256:cf706f588da964ff76eb23e010cd56973f31599a0ca009d8f20f34807d69e1b2", "1.0.6--pyhdfd78af_0": "sha256:2d01a2ab5773ab2637f8b13950af9f8572712a7d4bccffe69fdefa0a951780e8", "1.0.6--pyhdfd78af_1": "sha256:6fe9d0d92ebd8273b9445f23044d2e0566cc47abfb22e6c5f188de5fcd2eccb6", "1.1.0--pyhdfd78af_0": "sha256:20cff7136b53acd3f1516c6abb1e66df0699f35adba30351d7976fa5945ffeb8"}, "docker": "quay.io/biocontainers/arborator", "aliases": {"arborator": "/usr/local/bin/arborator", "gas": "/usr/local/bin/gas", "profile_dists": "/usr/local/bin/profile_dists", "cpuinfo": "/usr/local/bin/cpuinfo", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "cmtime": "/usr/local/bin/cmtime", "ib_acme": "/usr/local/bin/ib_acme", "ibv_asyncwatch": "/usr/local/bin/ibv_asyncwatch", "ibv_devices": "/usr/local/bin/ibv_devices", "ibv_devinfo": "/usr/local/bin/ibv_devinfo", "ibv_rc_pingpong": "/usr/local/bin/ibv_rc_pingpong", "ibv_srq_pingpong": "/usr/local/bin/ibv_srq_pingpong", "ibv_uc_pingpong": "/usr/local/bin/ibv_uc_pingpong", "ibv_ud_pingpong": "/usr/local/bin/ibv_ud_pingpong", "ibv_xsrq_pingpong": "/usr/local/bin/ibv_xsrq_pingpong", "mckey": "/usr/local/bin/mckey", "rcopy": "/usr/local/bin/rcopy", "rdma_client": "/usr/local/bin/rdma_client", "rdma_server": "/usr/local/bin/rdma_server", "rdma_xclient": "/usr/local/bin/rdma_xclient", "rdma_xserver": "/usr/local/bin/rdma_xserver", "riostream": "/usr/local/bin/riostream", "rping": "/usr/local/bin/rping", "rstream": "/usr/local/bin/rstream", "ucmatose": "/usr/local/bin/ucmatose", "udaddy": "/usr/local/bin/udaddy", "udpong": "/usr/local/bin/udpong", "io_demo": "/usr/local/bin/io_demo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arborator.
singularity registry hpc automated addition for arborator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arborator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arborator:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arborator/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/arborator/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arborator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arborator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arborator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arborator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arborator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arborator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arborator

```bash
$ singularity exec <container> /usr/local/bin/arborator
$ podman run --it --rm --entrypoint /usr/local/bin/arborator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arborator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gas

```bash
$ singularity exec <container> /usr/local/bin/gas
$ podman run --it --rm --entrypoint /usr/local/bin/gas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profile_dists

```bash
$ singularity exec <container> /usr/local/bin/profile_dists
$ podman run --it --rm --entrypoint /usr/local/bin/profile_dists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profile_dists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpuinfo

```bash
$ singularity exec <container> /usr/local/bin/cpuinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpuinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmtime

```bash
$ singularity exec <container> /usr/local/bin/cmtime
$ podman run --it --rm --entrypoint /usr/local/bin/cmtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmtime   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### io_demo

```bash
$ singularity exec <container> /usr/local/bin/io_demo
$ podman run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
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