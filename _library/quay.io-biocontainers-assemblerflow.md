---
layout: container
name:  "quay.io/biocontainers/assemblerflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/assemblerflow/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/assemblerflow/container.yaml"
updated_at: "2022-10-27 00:53:33.480244"
latest: "1.1.0.post3--py_2"
container_url: "https://biocontainers.pro/tools/assemblerflow"
aliases:
 - "assemblerflow"
 - "nextflow"
 - "nextflow.bak"
versions:
 - "1.1.0.post3--py_2"
description: "shpc-registry automated BioContainers addition for assemblerflow"
config: {"url": "https://biocontainers.pro/tools/assemblerflow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for assemblerflow", "latest": {"1.1.0.post3--py_2": "sha256:9dabb05c13c64ebe77abed3445458ccc92caecbe97295eb56d2c48188181246b"}, "tags": {"1.1.0.post3--py_2": "sha256:9dabb05c13c64ebe77abed3445458ccc92caecbe97295eb56d2c48188181246b"}, "docker": "quay.io/biocontainers/assemblerflow", "aliases": {"assemblerflow": "/usr/local/bin/assemblerflow", "nextflow": "/usr/local/bin/nextflow", "nextflow.bak": "/usr/local/bin/nextflow.bak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/assemblerflow.
shpc-registry automated BioContainers addition for assemblerflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/assemblerflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/assemblerflow:1.1.0.post3--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/assemblerflow/1.1.0.post3--py_2
$ module help quay.io/biocontainers/assemblerflow/1.1.0.post3--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### assemblerflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### assemblerflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### assemblerflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### assemblerflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### assemblerflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### assemblerflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assemblerflow

```bash
$ singularity exec <container> /usr/local/bin/assemblerflow
$ podman run --it --rm --entrypoint /usr/local/bin/assemblerflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assemblerflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow

```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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