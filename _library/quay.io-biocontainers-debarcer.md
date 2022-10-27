---
layout: container
name:  "quay.io/biocontainers/debarcer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/debarcer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/debarcer/container.yaml"
updated_at: "2022-10-27 00:42:02.301480"
latest: "2.1.4--pyhdfd78af_2"
container_url: "https://biocontainers.pro/tools/debarcer"
aliases:
 - "debarcer"
 - "pygal_gen.py"
versions:
 - "2.1.4--pyhdfd78af_2"
description: "shpc-registry automated BioContainers addition for debarcer"
config: {"url": "https://biocontainers.pro/tools/debarcer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for debarcer", "latest": {"2.1.4--pyhdfd78af_2": "sha256:a90402d9d7f24264d3a586cb4d42499c65ee465cc894eacbba025244421b3e50"}, "tags": {"2.1.4--pyhdfd78af_2": "sha256:a90402d9d7f24264d3a586cb4d42499c65ee465cc894eacbba025244421b3e50"}, "docker": "quay.io/biocontainers/debarcer", "aliases": {"debarcer": "/usr/local/bin/debarcer", "pygal_gen.py": "/usr/local/bin/pygal_gen.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/debarcer.
shpc-registry automated BioContainers addition for debarcer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/debarcer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/debarcer:2.1.4--pyhdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/debarcer/2.1.4--pyhdfd78af_2
$ module help quay.io/biocontainers/debarcer/2.1.4--pyhdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### debarcer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### debarcer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### debarcer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### debarcer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### debarcer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### debarcer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### debarcer

```bash
$ singularity exec <container> /usr/local/bin/debarcer
$ podman run --it --rm --entrypoint /usr/local/bin/debarcer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debarcer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygal_gen.py

```bash
$ singularity exec <container> /usr/local/bin/pygal_gen.py
$ podman run --it --rm --entrypoint /usr/local/bin/pygal_gen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygal_gen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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