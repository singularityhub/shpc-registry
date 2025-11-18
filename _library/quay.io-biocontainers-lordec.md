---
layout: container
name:  "quay.io/biocontainers/lordec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lordec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lordec/container.yaml"
updated_at: "2025-11-18 03:52:59.761845"
latest: "0.9--h77376b9_3"
container_url: "https://biocontainers.pro/tools/lordec"
aliases:
 - "dbgh5"
 - "dbginfo"
 - "leon"
 - "lordec-build-SR-graph"
 - "lordec-correct"
 - "lordec-stat"
 - "lordec-trim"
 - "lordec-trim-split"
 - "lordec_sge_slurm_wrapper.sh"
 - "f2py3.10"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
versions:
 - "0.9--h77376b9_3"
description: "shpc-registry automated BioContainers addition for lordec"
config: {"url": "https://biocontainers.pro/tools/lordec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lordec", "latest": {"0.9--h77376b9_3": "sha256:a83c41f5e6b8cc6ddfe5e43d155f5a354b8ec47e3f969c123a82b8ea592ade36"}, "tags": {"0.9--h77376b9_3": "sha256:a83c41f5e6b8cc6ddfe5e43d155f5a354b8ec47e3f969c123a82b8ea592ade36"}, "docker": "quay.io/biocontainers/lordec", "aliases": {"dbgh5": "/usr/local/bin/dbgh5", "dbginfo": "/usr/local/bin/dbginfo", "leon": "/usr/local/bin/leon", "lordec-build-SR-graph": "/usr/local/bin/lordec-build-SR-graph", "lordec-correct": "/usr/local/bin/lordec-correct", "lordec-stat": "/usr/local/bin/lordec-stat", "lordec-trim": "/usr/local/bin/lordec-trim", "lordec-trim-split": "/usr/local/bin/lordec-trim-split", "lordec_sge_slurm_wrapper.sh": "/usr/local/bin/lordec_sge_slurm_wrapper.sh", "f2py3.10": "/usr/local/bin/f2py3.10", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lordec.
shpc-registry automated BioContainers addition for lordec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lordec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lordec:0.9--h77376b9_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lordec/0.9--h77376b9_3
$ module help quay.io/biocontainers/lordec/0.9--h77376b9_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lordec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lordec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lordec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lordec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lordec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lordec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dbgh5

```bash
$ singularity exec <container> /usr/local/bin/dbgh5
$ podman run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbginfo

```bash
$ singularity exec <container> /usr/local/bin/dbginfo
$ podman run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### leon

```bash
$ singularity exec <container> /usr/local/bin/leon
$ podman run --it --rm --entrypoint /usr/local/bin/leon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-build-SR-graph

```bash
$ singularity exec <container> /usr/local/bin/lordec-build-SR-graph
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-build-SR-graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-build-SR-graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-correct

```bash
$ singularity exec <container> /usr/local/bin/lordec-correct
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-correct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-correct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-stat

```bash
$ singularity exec <container> /usr/local/bin/lordec-stat
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-trim

```bash
$ singularity exec <container> /usr/local/bin/lordec-trim
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-trim-split

```bash
$ singularity exec <container> /usr/local/bin/lordec-trim-split
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-trim-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-trim-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec_sge_slurm_wrapper.sh

```bash
$ singularity exec <container> /usr/local/bin/lordec_sge_slurm_wrapper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lordec_sge_slurm_wrapper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec_sge_slurm_wrapper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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