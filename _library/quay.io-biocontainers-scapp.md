---
layout: container
name:  "quay.io/biocontainers/scapp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scapp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scapp/container.yaml"
updated_at: "2022-10-27 00:42:00.995967"
latest: "0.1.4--py_0"
container_url: "https://biocontainers.pro/tools/scapp"
aliases:
 - "classify_fasta.py"
 - "scapp"
 - "train.py"
versions:
 - "0.1.4--py_0"
description: "shpc-registry automated BioContainers addition for scapp"
config: {"url": "https://biocontainers.pro/tools/scapp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scapp", "latest": {"0.1.4--py_0": "sha256:d45235843c1ecc8a0352279a9e9ae8e5c3e815b1be7d69e2a510ef53b9dc2ef1"}, "tags": {"0.1.4--py_0": "sha256:d45235843c1ecc8a0352279a9e9ae8e5c3e815b1be7d69e2a510ef53b9dc2ef1"}, "docker": "quay.io/biocontainers/scapp", "aliases": {"classify_fasta.py": "/usr/local/bin/classify_fasta.py", "scapp": "/usr/local/bin/scapp", "train.py": "/usr/local/bin/train.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scapp.
shpc-registry automated BioContainers addition for scapp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scapp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scapp:0.1.4--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scapp/0.1.4--py_0
$ module help quay.io/biocontainers/scapp/0.1.4--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scapp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scapp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scapp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scapp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scapp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scapp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### classify_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/classify_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/classify_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classify_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scapp

```bash
$ singularity exec <container> /usr/local/bin/scapp
$ podman run --it --rm --entrypoint /usr/local/bin/scapp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scapp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train.py

```bash
$ singularity exec <container> /usr/local/bin/train.py
$ podman run --it --rm --entrypoint /usr/local/bin/train.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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