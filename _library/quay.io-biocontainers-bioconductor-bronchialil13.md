---
layout: container
name:  "quay.io/biocontainers/bioconductor-bronchialil13"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bronchialil13/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bronchialil13/container.yaml"
updated_at: "2025-05-17 03:49:32.991624"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bronchialil13"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bronchialil13"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bronchialil13", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bronchialil13", "latest": {"1.44.0--r44hdfd78af_0": "sha256:6ad32fe6a37f3bb0db93b2df4592b906d3c3e0be8e13d29879ed7078553573af"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:aa28300dbc398dde2bef8283de9bf88856eccad1bda88bab934ba853c316e81a", "1.36.0--r42hdfd78af_0": "sha256:52b5891e18d1f69308f1aa841e5c4a50193609a0af5c837c23d3b451e69aacd4", "1.38.0--r43hdfd78af_0": "sha256:3e5f77628518da7bcd220997fa54df1177c996ea0fc2572691c87a0d0ccfce4c", "1.40.0--r43hdfd78af_0": "sha256:85f7b8207c74d2dd60f59e3bb0d2116b9fc6dc736a1cca2c037b7010e5f1a530", "1.44.0--r44hdfd78af_0": "sha256:6ad32fe6a37f3bb0db93b2df4592b906d3c3e0be8e13d29879ed7078553573af"}, "docker": "quay.io/biocontainers/bioconductor-bronchialil13"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bronchialil13.
shpc-registry automated BioContainers addition for bioconductor-bronchialil13
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bronchialil13
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bronchialil13:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bronchialil13/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bronchialil13/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bronchialil13-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bronchialil13-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bronchialil13-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bronchialil13-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bronchialil13-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bronchialil13-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bronchialil13

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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