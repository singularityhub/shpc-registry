---
layout: container
name:  "quay.io/biocontainers/find_differential_primers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/find_differential_primers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/find_differential_primers/container.yaml"
updated_at: "2025-03-30 03:07:57.777187"
latest: "0.1.4--py_2"
container_url: "https://biocontainers.pro/tools/find_differential_primers"
aliases:
 - "_gdlib-config"
 - "find_differential_primers.py"
 - "long_seq_tm_test"
 - "ntdpal"
 - "oligotm"
 - "perl5.30.3"
 - "primer3_core"
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
 - "0.1.4--py_2"
description: "shpc-registry automated BioContainers addition for find_differential_primers"
config: {"url": "https://biocontainers.pro/tools/find_differential_primers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for find_differential_primers", "latest": {"0.1.4--py_2": "sha256:12a23db1dfce9563eb5ba4986ac6ad3fb77ec2d0b483330bf64bee00a929e463"}, "tags": {"0.1.4--py_2": "sha256:12a23db1dfce9563eb5ba4986ac6ad3fb77ec2d0b483330bf64bee00a929e463"}, "docker": "quay.io/biocontainers/find_differential_primers", "aliases": {"_gdlib-config": "/usr/local/bin/_gdlib-config", "find_differential_primers.py": "/usr/local/bin/find_differential_primers.py", "long_seq_tm_test": "/usr/local/bin/long_seq_tm_test", "ntdpal": "/usr/local/bin/ntdpal", "oligotm": "/usr/local/bin/oligotm", "perl5.30.3": "/usr/local/bin/perl5.30.3", "primer3_core": "/usr/local/bin/primer3_core", "_bdftogd": "/usr/local/bin/_bdftogd", "_gd2copypal": "/usr/local/bin/_gd2copypal", "_gd2togif": "/usr/local/bin/_gd2togif", "_gd2topng": "/usr/local/bin/_gd2topng", "_gdcmpgif": "/usr/local/bin/_gdcmpgif", "_gdparttopng": "/usr/local/bin/_gdparttopng", "_gdtopng": "/usr/local/bin/_gdtopng", "_giftogd2": "/usr/local/bin/_giftogd2", "_pngtogd": "/usr/local/bin/_pngtogd", "_pngtogd2": "/usr/local/bin/_pngtogd2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/find_differential_primers.
shpc-registry automated BioContainers addition for find_differential_primers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/find_differential_primers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/find_differential_primers:0.1.4--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/find_differential_primers/0.1.4--py_2
$ module help quay.io/biocontainers/find_differential_primers/0.1.4--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### find_differential_primers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### find_differential_primers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### find_differential_primers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### find_differential_primers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### find_differential_primers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### find_differential_primers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/_gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/_gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_differential_primers.py

```bash
$ singularity exec <container> /usr/local/bin/find_differential_primers.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_differential_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_differential_primers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long_seq_tm_test

```bash
$ singularity exec <container> /usr/local/bin/long_seq_tm_test
$ podman run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long_seq_tm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntdpal

```bash
$ singularity exec <container> /usr/local/bin/ntdpal
$ podman run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntdpal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oligotm

```bash
$ singularity exec <container> /usr/local/bin/oligotm
$ podman run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oligotm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.30.3

```bash
$ singularity exec <container> /usr/local/bin/perl5.30.3
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.30.3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.30.3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primer3_core

```bash
$ singularity exec <container> /usr/local/bin/primer3_core
$ podman run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primer3_core   -v ${PWD} -w ${PWD} <container> -c " $@"
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