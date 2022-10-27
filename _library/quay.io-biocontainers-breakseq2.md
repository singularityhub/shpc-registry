---
layout: container
name:  "quay.io/biocontainers/breakseq2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/breakseq2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/breakseq2/container.yaml"
updated_at: "2022-10-27 01:04:23.839072"
latest: "2.2--py27_2"
container_url: "https://biocontainers.pro/tools/breakseq2"
aliases:
 - "breakseq2_gen_bplib.py"
 - "run_breakseq2.py"
versions:
 - "2.2--py27_2"
description: "shpc-registry automated BioContainers addition for breakseq2"
config: {"url": "https://biocontainers.pro/tools/breakseq2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for breakseq2", "latest": {"2.2--py27_2": "sha256:9999ff086fcf05f5c484ce6fa635ed02e5918da6fbb0e60f606aaaf05c1f7fb5"}, "tags": {"2.2--py27_2": "sha256:9999ff086fcf05f5c484ce6fa635ed02e5918da6fbb0e60f606aaaf05c1f7fb5"}, "docker": "quay.io/biocontainers/breakseq2", "aliases": {"breakseq2_gen_bplib.py": "/usr/local/bin/breakseq2_gen_bplib.py", "run_breakseq2.py": "/usr/local/bin/run_breakseq2.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/breakseq2.
shpc-registry automated BioContainers addition for breakseq2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/breakseq2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/breakseq2:2.2--py27_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/breakseq2/2.2--py27_2
$ module help quay.io/biocontainers/breakseq2/2.2--py27_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### breakseq2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### breakseq2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### breakseq2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### breakseq2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### breakseq2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### breakseq2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### breakseq2_gen_bplib.py

```bash
$ singularity exec <container> /usr/local/bin/breakseq2_gen_bplib.py
$ podman run --it --rm --entrypoint /usr/local/bin/breakseq2_gen_bplib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/breakseq2_gen_bplib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_breakseq2.py

```bash
$ singularity exec <container> /usr/local/bin/run_breakseq2.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_breakseq2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_breakseq2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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