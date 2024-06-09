---
layout: container
name:  "quay.io/biocontainers/corset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/corset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/corset/container.yaml"
updated_at: "2024-06-09 02:42:15.857136"
latest: "1.09--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/corset"
aliases:
 - "corset"
 - "corset_fasta_ID_changer"
versions:
 - "1.09--hd03093a_3"
 - "1.09--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for corset"
config: {"url": "https://biocontainers.pro/tools/corset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for corset", "latest": {"1.09--hdcf5f25_4": "sha256:2fdd3c566c12116e28358f636d1e65060a53f2ae42f59e530437980831d94369"}, "tags": {"1.09--hd03093a_3": "sha256:b60f3da57f6a2b491ca3509e589d299402e536843b0d4a4885df94f357ad933a", "1.09--hdcf5f25_4": "sha256:2fdd3c566c12116e28358f636d1e65060a53f2ae42f59e530437980831d94369"}, "docker": "quay.io/biocontainers/corset", "aliases": {"corset": "/usr/local/bin/corset", "corset_fasta_ID_changer": "/usr/local/bin/corset_fasta_ID_changer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/corset.
shpc-registry automated BioContainers addition for corset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/corset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/corset:1.09--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/corset/1.09--hdcf5f25_4
$ module help quay.io/biocontainers/corset/1.09--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### corset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### corset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### corset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### corset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### corset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### corset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### corset

```bash
$ singularity exec <container> /usr/local/bin/corset
$ podman run --it --rm --entrypoint /usr/local/bin/corset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corset_fasta_ID_changer

```bash
$ singularity exec <container> /usr/local/bin/corset_fasta_ID_changer
$ podman run --it --rm --entrypoint /usr/local/bin/corset_fasta_ID_changer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corset_fasta_ID_changer   -v ${PWD} -w ${PWD} <container> -c " $@"
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