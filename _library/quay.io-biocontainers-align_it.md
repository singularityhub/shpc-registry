---
layout: container
name:  "quay.io/biocontainers/align_it"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/align_it/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/align_it/container.yaml"
updated_at: "2024-10-03 03:06:22.472139"
latest: "1.0.4--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/align_it"
aliases:
 - "align-it"
 - "babel"
 - "obchiral"
 - "obabel"
 - "obconformer"
 - "obdistgen"
 - "obenergy"
 - "obfit"
 - "obgen"
 - "obgrep"
 - "obminimize"
 - "obprobe"
 - "obprop"
versions:
 - "1.0.4--hd03093a_1"
 - "1.0.4--hd03093a_2"
 - "1.0.4--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for align_it"
config: {"url": "https://biocontainers.pro/tools/align_it", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for align_it", "latest": {"1.0.4--hdcf5f25_3": "sha256:5a1bb473a36a7c4f0609b30391e6b51ea4bb05191b2512393c8b7a253eeea268"}, "tags": {"1.0.4--hd03093a_1": "sha256:e290322e782e4ba005a340ba08964c031924df4465eaaaa1ebbdd5cfbe9100a8", "1.0.4--hd03093a_2": "sha256:e3f1a73163348ac205e7478536c5906d3315f6e386e97b825ae2514b50eecadb", "1.0.4--hdcf5f25_3": "sha256:5a1bb473a36a7c4f0609b30391e6b51ea4bb05191b2512393c8b7a253eeea268"}, "docker": "quay.io/biocontainers/align_it", "aliases": {"align-it": "/usr/local/bin/align-it", "babel": "/usr/local/bin/babel", "obchiral": "/usr/local/bin/obchiral", "obabel": "/usr/local/bin/obabel", "obconformer": "/usr/local/bin/obconformer", "obdistgen": "/usr/local/bin/obdistgen", "obenergy": "/usr/local/bin/obenergy", "obfit": "/usr/local/bin/obfit", "obgen": "/usr/local/bin/obgen", "obgrep": "/usr/local/bin/obgrep", "obminimize": "/usr/local/bin/obminimize", "obprobe": "/usr/local/bin/obprobe", "obprop": "/usr/local/bin/obprop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/align_it.
shpc-registry automated BioContainers addition for align_it
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/align_it
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/align_it:1.0.4--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/align_it/1.0.4--hdcf5f25_3
$ module help quay.io/biocontainers/align_it/1.0.4--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### align_it-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### align_it-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### align_it-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### align_it-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### align_it-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### align_it-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### align-it

```bash
$ singularity exec <container> /usr/local/bin/align-it
$ podman run --it --rm --entrypoint /usr/local/bin/align-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### babel

```bash
$ singularity exec <container> /usr/local/bin/babel
$ podman run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obchiral

```bash
$ singularity exec <container> /usr/local/bin/obchiral
$ podman run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obabel

```bash
$ singularity exec <container> /usr/local/bin/obabel
$ podman run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obconformer

```bash
$ singularity exec <container> /usr/local/bin/obconformer
$ podman run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obdistgen

```bash
$ singularity exec <container> /usr/local/bin/obdistgen
$ podman run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obenergy

```bash
$ singularity exec <container> /usr/local/bin/obenergy
$ podman run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfit

```bash
$ singularity exec <container> /usr/local/bin/obfit
$ podman run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgen

```bash
$ singularity exec <container> /usr/local/bin/obgen
$ podman run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgrep

```bash
$ singularity exec <container> /usr/local/bin/obgrep
$ podman run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obminimize

```bash
$ singularity exec <container> /usr/local/bin/obminimize
$ podman run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprobe

```bash
$ singularity exec <container> /usr/local/bin/obprobe
$ podman run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprop

```bash
$ singularity exec <container> /usr/local/bin/obprop
$ podman run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
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