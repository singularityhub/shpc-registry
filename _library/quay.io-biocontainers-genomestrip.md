---
layout: container
name:  "quay.io/biocontainers/genomestrip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomestrip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/genomestrip/container.yaml"
updated_at: "2022-10-27 00:59:01.012004"
latest: "2.00.1833--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/genomestrip"
aliases:
 - "genomestrip"
versions:
 - "2.00.1833--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for genomestrip"
config: {"url": "https://biocontainers.pro/tools/genomestrip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomestrip", "latest": {"2.00.1833--hdfd78af_4": "sha256:8b10af529781c89854549ca2e66e585e48553c94e761bf6ed4fbb34af57c7134"}, "tags": {"2.00.1833--hdfd78af_4": "sha256:8b10af529781c89854549ca2e66e585e48553c94e761bf6ed4fbb34af57c7134"}, "docker": "quay.io/biocontainers/genomestrip", "aliases": {"genomestrip": "/usr/local/bin/genomestrip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomestrip.
shpc-registry automated BioContainers addition for genomestrip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomestrip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomestrip:2.00.1833--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomestrip/2.00.1833--hdfd78af_4
$ module help quay.io/biocontainers/genomestrip/2.00.1833--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomestrip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomestrip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomestrip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomestrip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomestrip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomestrip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genomestrip

```bash
$ singularity exec <container> /usr/local/bin/genomestrip
$ podman run --it --rm --entrypoint /usr/local/bin/genomestrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomestrip   -v ${PWD} -w ${PWD} <container> -c " $@"
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