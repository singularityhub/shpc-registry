---
layout: container
name:  "ghcr.io/autamus/xrootd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/xrootd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/xrootd/container.yaml"
updated_at: "2024-03-20 02:21:33.140342"
latest: "5.3.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/xrootd"
aliases:
 - "xrdacctest"
 - "xrdadler32"
 - "xrdcopy"
 - "xrdcp"
 - "xrdfs"
 - "xrdgsiproxy"
 - "xrdgsitest"
 - "xrdmapc"
 - "xrdpfc_print"
 - "xrdpinls"
 - "xrdpwdadmin"
 - "xrdsssadmin"
 - "xrootd"
 - "xrootd-config"
versions:
 - "5.1.0"
 - "5.3.1"
 - "5.3.2"
 - "latest"
description: "XRootD software framework is a fully generic suite for fast, low latency and scalable data access, which can serve natively any kind of data, organized as a hierarchical filesystem-like namespace, based on the concept of directory."
config: {"docker": "ghcr.io/autamus/xrootd", "url": "https://github.com/orgs/autamus/packages/container/package/xrootd", "maintainer": "@vsoch", "description": "XRootD software framework is a fully generic suite for fast, low latency and scalable data access, which can serve natively any kind of data, organized as a hierarchical filesystem-like namespace, based on the concept of directory.", "latest": {"5.3.2": "sha256:79ca99e2dfc5c2834899fc9b486cbb368cfdf0b5ec16d9f9aafd317787020679"}, "tags": {"5.1.0": "sha256:37902350afb153684fa04bba4926f86f8bb0d580c8a2bda9dcdf0d371923dfbf", "5.3.1": "sha256:9b42939274b693da6a54e003855a8be2ca8a7114d9fe0705197cc987b6ccea5b", "5.3.2": "sha256:79ca99e2dfc5c2834899fc9b486cbb368cfdf0b5ec16d9f9aafd317787020679", "latest": "sha256:79ca99e2dfc5c2834899fc9b486cbb368cfdf0b5ec16d9f9aafd317787020679"}, "aliases": {"xrdacctest": "/opt/view/bin/xrdacctest", "xrdadler32": "/opt/view/bin/xrdadler32", "xrdcopy": "/opt/view/bin/xrdcopy", "xrdcp": "/opt/view/bin/xrdcp", "xrdfs": "/opt/view/bin/xrdfs", "xrdgsiproxy": "/opt/view/bin/xrdgsiproxy", "xrdgsitest": "/opt/view/bin/xrdgsitest", "xrdmapc": "/opt/view/bin/xrdmapc", "xrdpfc_print": "/opt/view/bin/xrdpfc_print", "xrdpinls": "/opt/view/bin/xrdpinls", "xrdpwdadmin": "/opt/view/bin/xrdpwdadmin", "xrdsssadmin": "/opt/view/bin/xrdsssadmin", "xrootd": "/opt/view/bin/xrootd", "xrootd-config": "/opt/view/bin/xrootd-config"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/xrootd.
XRootD software framework is a fully generic suite for fast, low latency and scalable data access, which can serve natively any kind of data, organized as a hierarchical filesystem-like namespace, based on the concept of directory.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/xrootd
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/xrootd:5.3.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/xrootd/5.3.2
$ module help ghcr.io/autamus/xrootd/5.3.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xrootd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xrootd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xrootd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xrootd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xrootd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xrootd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xrdacctest

```bash
$ singularity exec <container> /opt/view/bin/xrdacctest
$ podman run --it --rm --entrypoint /opt/view/bin/xrdacctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdacctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdadler32

```bash
$ singularity exec <container> /opt/view/bin/xrdadler32
$ podman run --it --rm --entrypoint /opt/view/bin/xrdadler32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdadler32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdcopy

```bash
$ singularity exec <container> /opt/view/bin/xrdcopy
$ podman run --it --rm --entrypoint /opt/view/bin/xrdcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdcp

```bash
$ singularity exec <container> /opt/view/bin/xrdcp
$ podman run --it --rm --entrypoint /opt/view/bin/xrdcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdfs

```bash
$ singularity exec <container> /opt/view/bin/xrdfs
$ podman run --it --rm --entrypoint /opt/view/bin/xrdfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdgsiproxy

```bash
$ singularity exec <container> /opt/view/bin/xrdgsiproxy
$ podman run --it --rm --entrypoint /opt/view/bin/xrdgsiproxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdgsiproxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdgsitest

```bash
$ singularity exec <container> /opt/view/bin/xrdgsitest
$ podman run --it --rm --entrypoint /opt/view/bin/xrdgsitest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdgsitest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdmapc

```bash
$ singularity exec <container> /opt/view/bin/xrdmapc
$ podman run --it --rm --entrypoint /opt/view/bin/xrdmapc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdmapc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdpfc_print

```bash
$ singularity exec <container> /opt/view/bin/xrdpfc_print
$ podman run --it --rm --entrypoint /opt/view/bin/xrdpfc_print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdpfc_print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdpinls

```bash
$ singularity exec <container> /opt/view/bin/xrdpinls
$ podman run --it --rm --entrypoint /opt/view/bin/xrdpinls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdpinls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdpwdadmin

```bash
$ singularity exec <container> /opt/view/bin/xrdpwdadmin
$ podman run --it --rm --entrypoint /opt/view/bin/xrdpwdadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdpwdadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrdsssadmin

```bash
$ singularity exec <container> /opt/view/bin/xrdsssadmin
$ podman run --it --rm --entrypoint /opt/view/bin/xrdsssadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrdsssadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrootd

```bash
$ singularity exec <container> /opt/view/bin/xrootd
$ podman run --it --rm --entrypoint /opt/view/bin/xrootd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrootd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xrootd-config

```bash
$ singularity exec <container> /opt/view/bin/xrootd-config
$ podman run --it --rm --entrypoint /opt/view/bin/xrootd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xrootd-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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