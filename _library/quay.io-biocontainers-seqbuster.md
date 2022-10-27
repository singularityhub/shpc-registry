---
layout: container
name:  "quay.io/biocontainers/seqbuster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqbuster/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/seqbuster/container.yaml"
updated_at: "2022-10-27 01:15:45.669103"
latest: "3.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/seqbuster"
aliases:
 - "miraligner"
versions:
 - "3.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for seqbuster"
config: {"url": "https://biocontainers.pro/tools/seqbuster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqbuster", "latest": {"3.5--hdfd78af_1": "sha256:bdcee5918ba4545bcf1a947f93c255a7afe0767b133791d1a897492b000f78e1"}, "tags": {"3.5--hdfd78af_1": "sha256:bdcee5918ba4545bcf1a947f93c255a7afe0767b133791d1a897492b000f78e1"}, "docker": "quay.io/biocontainers/seqbuster", "aliases": {"miraligner": "/usr/local/bin/miraligner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqbuster.
shpc-registry automated BioContainers addition for seqbuster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqbuster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqbuster:3.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqbuster/3.5--hdfd78af_1
$ module help quay.io/biocontainers/seqbuster/3.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqbuster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqbuster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqbuster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqbuster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqbuster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqbuster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miraligner

```bash
$ singularity exec <container> /usr/local/bin/miraligner
$ podman run --it --rm --entrypoint /usr/local/bin/miraligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miraligner   -v ${PWD} -w ${PWD} <container> -c " $@"
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