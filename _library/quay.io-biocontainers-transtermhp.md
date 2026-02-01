---
layout: container
name:  "quay.io/biocontainers/transtermhp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transtermhp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transtermhp/container.yaml"
updated_at: "2026-02-01 04:38:47.662217"
latest: "2.09--h9948957_2"
container_url: "https://biocontainers.pro/tools/transtermhp"
aliases:
 - "2ndscore"
 - "calibrate.sh"
 - "make_expterm.py"
 - "mfold_rna.sh"
 - "transterm"
versions:
 - "2.09--h2d50403_1"
 - "2.09--h9948957_2"
description: "shpc-registry automated BioContainers addition for transtermhp"
config: {"url": "https://biocontainers.pro/tools/transtermhp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transtermhp", "latest": {"2.09--h9948957_2": "sha256:fc6fe0404be9340a883ec7a7b90415dfc3826c2bca7333a0314335c7bfee2d03"}, "tags": {"2.09--h2d50403_1": "sha256:310af5ac72c3c29d3872a87e42fdc0fef95e52eab045d8cd4b7f31efb80f4916", "2.09--h9948957_2": "sha256:fc6fe0404be9340a883ec7a7b90415dfc3826c2bca7333a0314335c7bfee2d03"}, "docker": "quay.io/biocontainers/transtermhp", "aliases": {"2ndscore": "/usr/local/bin/2ndscore", "calibrate.sh": "/usr/local/bin/calibrate.sh", "make_expterm.py": "/usr/local/bin/make_expterm.py", "mfold_rna.sh": "/usr/local/bin/mfold_rna.sh", "transterm": "/usr/local/bin/transterm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transtermhp.
shpc-registry automated BioContainers addition for transtermhp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transtermhp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transtermhp:2.09--h9948957_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transtermhp/2.09--h9948957_2
$ module help quay.io/biocontainers/transtermhp/2.09--h9948957_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transtermhp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transtermhp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transtermhp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transtermhp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transtermhp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transtermhp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2ndscore

```bash
$ singularity exec <container> /usr/local/bin/2ndscore
$ podman run --it --rm --entrypoint /usr/local/bin/2ndscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2ndscore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calibrate.sh

```bash
$ singularity exec <container> /usr/local/bin/calibrate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/calibrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calibrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_expterm.py

```bash
$ singularity exec <container> /usr/local/bin/make_expterm.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_expterm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_expterm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfold_rna.sh

```bash
$ singularity exec <container> /usr/local/bin/mfold_rna.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mfold_rna.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfold_rna.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transterm

```bash
$ singularity exec <container> /usr/local/bin/transterm
$ podman run --it --rm --entrypoint /usr/local/bin/transterm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transterm   -v ${PWD} -w ${PWD} <container> -c " $@"
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