---
layout: container
name:  "quay.io/biocontainers/damasker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/damasker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/damasker/container.yaml"
updated_at: "2025-01-13 03:25:35.040843"
latest: "1.0p1--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/damasker"
aliases:
 - "HPC.REPmask"
 - "HPC.TANmask"
 - "REPmask"
 - "TANmask"
 - "datander"
versions:
 - "1.0p1--hec16e2b_4"
 - "1.0p1--h031d066_6"
 - "1.0p1--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for damasker"
config: {"url": "https://biocontainers.pro/tools/damasker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for damasker", "latest": {"1.0p1--h7b50bb2_7": "sha256:ccc8366a772cfdfcd39eec5c1399cfe7cbfd5015d39e9a329b072cc1767391b9"}, "tags": {"1.0p1--hec16e2b_4": "sha256:ed4af8957f360fd46c6efad21cf255cb92a2d9a42a3b422c503122ca38477740", "1.0p1--h031d066_6": "sha256:e8acfae33b317163a5e105ad913d27c704ef8abff3223d4ce2f2d91eb896fb72", "1.0p1--h7b50bb2_7": "sha256:ccc8366a772cfdfcd39eec5c1399cfe7cbfd5015d39e9a329b072cc1767391b9"}, "docker": "quay.io/biocontainers/damasker", "aliases": {"HPC.REPmask": "/usr/local/bin/HPC.REPmask", "HPC.TANmask": "/usr/local/bin/HPC.TANmask", "REPmask": "/usr/local/bin/REPmask", "TANmask": "/usr/local/bin/TANmask", "datander": "/usr/local/bin/datander"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/damasker.
shpc-registry automated BioContainers addition for damasker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/damasker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/damasker:1.0p1--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/damasker/1.0p1--h7b50bb2_7
$ module help quay.io/biocontainers/damasker/1.0p1--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### damasker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### damasker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### damasker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### damasker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### damasker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### damasker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HPC.REPmask

```bash
$ singularity exec <container> /usr/local/bin/HPC.REPmask
$ podman run --it --rm --entrypoint /usr/local/bin/HPC.REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPC.REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HPC.TANmask

```bash
$ singularity exec <container> /usr/local/bin/HPC.TANmask
$ podman run --it --rm --entrypoint /usr/local/bin/HPC.TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPC.TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### REPmask

```bash
$ singularity exec <container> /usr/local/bin/REPmask
$ podman run --it --rm --entrypoint /usr/local/bin/REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TANmask

```bash
$ singularity exec <container> /usr/local/bin/TANmask
$ podman run --it --rm --entrypoint /usr/local/bin/TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datander

```bash
$ singularity exec <container> /usr/local/bin/datander
$ podman run --it --rm --entrypoint /usr/local/bin/datander   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datander   -v ${PWD} -w ${PWD} <container> -c " $@"
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