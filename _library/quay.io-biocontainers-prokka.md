---
layout: container
name:  "quay.io/biocontainers/prokka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prokka/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/prokka/container.yaml"
updated_at: "2022-10-27 00:37:31.703261"
latest: "1.14.6--pl5321hdfd78af_4"
container_url: "https://biocontainers.pro/tools/prokka"
aliases:
 - "tbl2asn-test"
versions:
 - "1.14.6--pl5321hdfd78af_4"
description: "shpc-registry automated BioContainers addition for prokka"
config: {"url": "https://biocontainers.pro/tools/prokka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prokka", "latest": {"1.14.6--pl5321hdfd78af_4": "sha256:d68768c8a51763cb6de66a96e34107874556cee935a70e21c3369680e07b9e14"}, "tags": {"1.14.6--pl5321hdfd78af_4": "sha256:d68768c8a51763cb6de66a96e34107874556cee935a70e21c3369680e07b9e14"}, "docker": "quay.io/biocontainers/prokka", "aliases": {"tbl2asn-test": "/usr/local/bin/tbl2asn-test"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prokka.
shpc-registry automated BioContainers addition for prokka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prokka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prokka:1.14.6--pl5321hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prokka/1.14.6--pl5321hdfd78af_4
$ module help quay.io/biocontainers/prokka/1.14.6--pl5321hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prokka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prokka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prokka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prokka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prokka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prokka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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