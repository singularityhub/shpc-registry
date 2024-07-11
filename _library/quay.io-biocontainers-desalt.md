---
layout: container
name:  "quay.io/biocontainers/desalt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/desalt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/desalt/container.yaml"
updated_at: "2024-07-11 03:42:53.958162"
latest: "1.5.6--he4a0461_5"
container_url: "https://biocontainers.pro/tools/desalt"
aliases:
 - "Annotation_Load.py"
 - "deBGA"
 - "deSALT"
versions:
 - "1.5.6--h7132678_2"
 - "1.5.6--he4a0461_4"
 - "1.5.6--he4a0461_5"
description: "shpc-registry automated BioContainers addition for desalt"
config: {"url": "https://biocontainers.pro/tools/desalt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for desalt", "latest": {"1.5.6--he4a0461_5": "sha256:bb67908be995417a2ae758d4bcebedff1bb5266642608fa049055382064d2598"}, "tags": {"1.5.6--h7132678_2": "sha256:3cbc60eb1eab0c4a1c57effb5093578593047e296847b147dcbb2250b341c286", "1.5.6--he4a0461_4": "sha256:ec5ed90bc132529b9ef45facdb0020ebbc950a67b966e6636f5615df12c0b6d4", "1.5.6--he4a0461_5": "sha256:bb67908be995417a2ae758d4bcebedff1bb5266642608fa049055382064d2598"}, "docker": "quay.io/biocontainers/desalt", "aliases": {"Annotation_Load.py": "/usr/local/bin/Annotation_Load.py", "deBGA": "/usr/local/bin/deBGA", "deSALT": "/usr/local/bin/deSALT"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/desalt.
shpc-registry automated BioContainers addition for desalt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/desalt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/desalt:1.5.6--he4a0461_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/desalt/1.5.6--he4a0461_5
$ module help quay.io/biocontainers/desalt/1.5.6--he4a0461_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### desalt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### desalt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### desalt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### desalt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### desalt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### desalt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Annotation_Load.py

```bash
$ singularity exec <container> /usr/local/bin/Annotation_Load.py
$ podman run --it --rm --entrypoint /usr/local/bin/Annotation_Load.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Annotation_Load.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deBGA

```bash
$ singularity exec <container> /usr/local/bin/deBGA
$ podman run --it --rm --entrypoint /usr/local/bin/deBGA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deBGA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deSALT

```bash
$ singularity exec <container> /usr/local/bin/deSALT
$ podman run --it --rm --entrypoint /usr/local/bin/deSALT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deSALT   -v ${PWD} -w ${PWD} <container> -c " $@"
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