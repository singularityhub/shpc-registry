---
layout: container
name:  "quay.io/biocontainers/mcroni"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mcroni/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mcroni/container.yaml"
updated_at: "2025-07-11 15:02:44.541824"
latest: "1.0.4--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/mcroni"
aliases:
 - "_gdlib-config"
 - "abricate"
 - "abricate-get_db"
 - "mcroni"
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
 - "1.0.4--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for mcroni"
config: {"url": "https://biocontainers.pro/tools/mcroni", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mcroni", "latest": {"1.0.4--pyh5e36f6f_0": "sha256:bcee9f6b16a877faac58e8e39c214f7cdd1b8262c24260d2d9bb081f4df77e68"}, "tags": {"1.0.4--pyh5e36f6f_0": "sha256:bcee9f6b16a877faac58e8e39c214f7cdd1b8262c24260d2d9bb081f4df77e68"}, "docker": "quay.io/biocontainers/mcroni", "aliases": {"_gdlib-config": "/usr/local/bin/_gdlib-config", "abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "mcroni": "/usr/local/bin/mcroni", "_bdftogd": "/usr/local/bin/_bdftogd", "_gd2copypal": "/usr/local/bin/_gd2copypal", "_gd2togif": "/usr/local/bin/_gd2togif", "_gd2topng": "/usr/local/bin/_gd2topng", "_gdcmpgif": "/usr/local/bin/_gdcmpgif", "_gdparttopng": "/usr/local/bin/_gdparttopng", "_gdtopng": "/usr/local/bin/_gdtopng", "_giftogd2": "/usr/local/bin/_giftogd2", "_pngtogd": "/usr/local/bin/_pngtogd", "_pngtogd2": "/usr/local/bin/_pngtogd2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mcroni.
shpc-registry automated BioContainers addition for mcroni
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mcroni
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mcroni:1.0.4--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mcroni/1.0.4--pyh5e36f6f_0
$ module help quay.io/biocontainers/mcroni/1.0.4--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mcroni-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mcroni-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mcroni-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mcroni-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mcroni-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mcroni-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/_gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/_gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcroni

```bash
$ singularity exec <container> /usr/local/bin/mcroni
$ podman run --it --rm --entrypoint /usr/local/bin/mcroni   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcroni   -v ${PWD} -w ${PWD} <container> -c " $@"
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