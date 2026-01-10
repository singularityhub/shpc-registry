---
layout: container
name:  "quay.io/biocontainers/nextdenovo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nextdenovo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nextdenovo/container.yaml"
updated_at: "2026-01-10 03:35:00.802981"
latest: "2.5.2--py310h0ceaa1d_6"
container_url: "https://biocontainers.pro/tools/nextdenovo"
aliases:
 - "nextDenovo"
 - "paralleltask"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "2.5.0--py39h20169af_0"
 - "2.5.2--py39h20169af_0"
 - "2.5.2--py39h36aabaf_3"
 - "2.5.2--py38h76b73ad_3"
 - "2.5.2--py39h4a8586d_4"
 - "2.5.2--py38h80588be_5"
 - "2.5.2--py310h0ceaa1d_6"
description: "singularity registry hpc automated addition for nextdenovo"
config: {"url": "https://biocontainers.pro/tools/nextdenovo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nextdenovo", "latest": {"2.5.2--py310h0ceaa1d_6": "sha256:b228a35caacf271838108f83d954e7c372449ef367502c5519105ed7be1197ac"}, "tags": {"2.5.0--py39h20169af_0": "sha256:f3fc2264ce1343ef26f8304b4e78872d9e3cd625e5225e97986bf66fd1924ba1", "2.5.2--py39h20169af_0": "sha256:7e4193ebfce11c9e17c78dfa7e9d7584b3adb3d8361d49fb265cc5b6aebaa5ab", "2.5.2--py39h36aabaf_3": "sha256:5c0a33732c3837c543dbe49abaef2172203d217ad95815409205ef149e7eb126", "2.5.2--py38h76b73ad_3": "sha256:78fe99fa56688be0e728cfd83598275645a5a1c0f15ec08a42bcc189df5a5a0c", "2.5.2--py39h4a8586d_4": "sha256:84e892767ba08a8fdf172e41bb268c7dd86ed2b2b78bbf7b9a64ea7343c42c99", "2.5.2--py38h80588be_5": "sha256:bf5bacb6b5f2427d17b4776625308180f0af099eefc3c49bc6f24e1db1602d07", "2.5.2--py310h0ceaa1d_6": "sha256:b228a35caacf271838108f83d954e7c372449ef367502c5519105ed7be1197ac"}, "docker": "quay.io/biocontainers/nextdenovo", "aliases": {"nextDenovo": "/usr/local/bin/nextDenovo", "paralleltask": "/usr/local/bin/paralleltask", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nextdenovo.
singularity registry hpc automated addition for nextdenovo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nextdenovo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nextdenovo:2.5.2--py310h0ceaa1d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nextdenovo/2.5.2--py310h0ceaa1d_6
$ module help quay.io/biocontainers/nextdenovo/2.5.2--py310h0ceaa1d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nextdenovo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nextdenovo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nextdenovo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nextdenovo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nextdenovo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nextdenovo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nextDenovo

```bash
$ singularity exec <container> /usr/local/bin/nextDenovo
$ podman run --it --rm --entrypoint /usr/local/bin/nextDenovo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextDenovo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paralleltask

```bash
$ singularity exec <container> /usr/local/bin/paralleltask
$ podman run --it --rm --entrypoint /usr/local/bin/paralleltask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paralleltask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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