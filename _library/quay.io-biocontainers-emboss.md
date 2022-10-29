---
layout: container
name:  "quay.io/biocontainers/emboss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/emboss/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/emboss/container.yaml"
updated_at: "2022-10-29 17:48:39.946731"
latest: "6.6.0--haa49230_5"
container_url: "https://biocontainers.pro/tools/emboss"
aliases:
 - "_embossdata"
 - "_embossversion"
 - "_jembossctl"
 - "embossdata"
 - "embossupdate"
 - "embossversion"
 - "jembossctl"
 - "runJemboss.sh"
 - "_bdftogd"
 - "_gd2copypal"
 - "_gd2togif"
 - "_gd2topng"
 - "_gdcmpgif"
 - "_gdparttopng"
 - "_gdtopng"
 - "_giftogd2"
 - "_pngtogd"
 - "_pngtogd2"
versions:
 - "6.6.0--haa49230_5"
description: "shpc-registry automated BioContainers addition for emboss"
config: {"url": "https://biocontainers.pro/tools/emboss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for emboss", "latest": {"6.6.0--haa49230_5": "sha256:51a26af4f2349bcb017855d7e797bcdb787e9177b3067ff439ccdeac550991ab"}, "tags": {"6.6.0--haa49230_5": "sha256:51a26af4f2349bcb017855d7e797bcdb787e9177b3067ff439ccdeac550991ab"}, "docker": "quay.io/biocontainers/emboss", "aliases": {"_embossdata": "/usr/local/bin/_embossdata", "_embossversion": "/usr/local/bin/_embossversion", "_jembossctl": "/usr/local/bin/_jembossctl", "embossdata": "/usr/local/bin/embossdata", "embossupdate": "/usr/local/bin/embossupdate", "embossversion": "/usr/local/bin/embossversion", "jembossctl": "/usr/local/bin/jembossctl", "runJemboss.sh": "/usr/local/bin/runJemboss.sh", "_bdftogd": "/usr/local/bin/_bdftogd", "_gd2copypal": "/usr/local/bin/_gd2copypal", "_gd2togif": "/usr/local/bin/_gd2togif", "_gd2topng": "/usr/local/bin/_gd2topng", "_gdcmpgif": "/usr/local/bin/_gdcmpgif", "_gdparttopng": "/usr/local/bin/_gdparttopng", "_gdtopng": "/usr/local/bin/_gdtopng", "_giftogd2": "/usr/local/bin/_giftogd2", "_pngtogd": "/usr/local/bin/_pngtogd", "_pngtogd2": "/usr/local/bin/_pngtogd2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/emboss.
shpc-registry automated BioContainers addition for emboss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/emboss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/emboss:6.6.0--haa49230_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/emboss/6.6.0--haa49230_5
$ module help quay.io/biocontainers/emboss/6.6.0--haa49230_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### emboss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### emboss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### emboss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### emboss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### emboss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### emboss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _embossdata

```bash
$ singularity exec <container> /usr/local/bin/_embossdata
$ podman run --it --rm --entrypoint /usr/local/bin/_embossdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_embossdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _embossversion

```bash
$ singularity exec <container> /usr/local/bin/_embossversion
$ podman run --it --rm --entrypoint /usr/local/bin/_embossversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_embossversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _jembossctl

```bash
$ singularity exec <container> /usr/local/bin/_jembossctl
$ podman run --it --rm --entrypoint /usr/local/bin/_jembossctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_jembossctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### embossdata

```bash
$ singularity exec <container> /usr/local/bin/embossdata
$ podman run --it --rm --entrypoint /usr/local/bin/embossdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/embossdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### embossupdate

```bash
$ singularity exec <container> /usr/local/bin/embossupdate
$ podman run --it --rm --entrypoint /usr/local/bin/embossupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/embossupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### embossversion

```bash
$ singularity exec <container> /usr/local/bin/embossversion
$ podman run --it --rm --entrypoint /usr/local/bin/embossversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/embossversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jembossctl

```bash
$ singularity exec <container> /usr/local/bin/jembossctl
$ podman run --it --rm --entrypoint /usr/local/bin/jembossctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jembossctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runJemboss.sh

```bash
$ singularity exec <container> /usr/local/bin/runJemboss.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runJemboss.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runJemboss.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _bdftogd

```bash
$ singularity exec <container> /usr/local/bin/_bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/_bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _gd2copypal

```bash
$ singularity exec <container> /usr/local/bin/_gd2copypal
$ podman run --it --rm --entrypoint /usr/local/bin/_gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _gd2togif

```bash
$ singularity exec <container> /usr/local/bin/_gd2togif
$ podman run --it --rm --entrypoint /usr/local/bin/_gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _gd2topng

```bash
$ singularity exec <container> /usr/local/bin/_gd2topng
$ podman run --it --rm --entrypoint /usr/local/bin/_gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _gdcmpgif

```bash
$ singularity exec <container> /usr/local/bin/_gdcmpgif
$ podman run --it --rm --entrypoint /usr/local/bin/_gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _gdparttopng

```bash
$ singularity exec <container> /usr/local/bin/_gdparttopng
$ podman run --it --rm --entrypoint /usr/local/bin/_gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _gdtopng

```bash
$ singularity exec <container> /usr/local/bin/_gdtopng
$ podman run --it --rm --entrypoint /usr/local/bin/_gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _giftogd2

```bash
$ singularity exec <container> /usr/local/bin/_giftogd2
$ podman run --it --rm --entrypoint /usr/local/bin/_giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _pngtogd

```bash
$ singularity exec <container> /usr/local/bin/_pngtogd
$ podman run --it --rm --entrypoint /usr/local/bin/_pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _pngtogd2

```bash
$ singularity exec <container> /usr/local/bin/_pngtogd2
$ podman run --it --rm --entrypoint /usr/local/bin/_pngtogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_pngtogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
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