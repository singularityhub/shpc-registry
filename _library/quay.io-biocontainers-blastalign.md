---
layout: container
name:  "quay.io/biocontainers/blastalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blastalign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/blastalign/container.yaml"
updated_at: "2022-10-27 00:18:26.530270"
latest: "1.4--hec16e2b_7"
container_url: "https://biocontainers.pro/tools/blastalign"
aliases:
 - "BlastAlign"
 - "BlastAlign.py"
 - "BlastAlignP"
versions:
 - "1.4--hec16e2b_7"
description: "shpc-registry automated BioContainers addition for blastalign"
config: {"url": "https://biocontainers.pro/tools/blastalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blastalign", "latest": {"1.4--hec16e2b_7": "sha256:744cad6391a4e9f01c39c5b3c8e11d1cce6eae440060b6ad223663b3877bcca4"}, "tags": {"1.4--hec16e2b_7": "sha256:744cad6391a4e9f01c39c5b3c8e11d1cce6eae440060b6ad223663b3877bcca4"}, "docker": "quay.io/biocontainers/blastalign", "aliases": {"BlastAlign": "/usr/local/bin/BlastAlign", "BlastAlign.py": "/usr/local/bin/BlastAlign.py", "BlastAlignP": "/usr/local/bin/BlastAlignP"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blastalign.
shpc-registry automated BioContainers addition for blastalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blastalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blastalign:1.4--hec16e2b_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blastalign/1.4--hec16e2b_7
$ module help quay.io/biocontainers/blastalign/1.4--hec16e2b_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blastalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blastalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blastalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blastalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blastalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blastalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BlastAlign

```bash
$ singularity exec <container> /usr/local/bin/BlastAlign
$ podman run --it --rm --entrypoint /usr/local/bin/BlastAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlastAlign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BlastAlign.py

```bash
$ singularity exec <container> /usr/local/bin/BlastAlign.py
$ podman run --it --rm --entrypoint /usr/local/bin/BlastAlign.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlastAlign.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BlastAlignP

```bash
$ singularity exec <container> /usr/local/bin/BlastAlignP
$ podman run --it --rm --entrypoint /usr/local/bin/BlastAlignP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlastAlignP   -v ${PWD} -w ${PWD} <container> -c " $@"
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