---
layout: container
name:  "quay.io/biocontainers/bioconductor-nugomm1a520177probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nugomm1a520177probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nugomm1a520177probe/container.yaml"
updated_at: "2023-10-06 02:55:44.979060"
latest: "3.4.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-nugomm1a520177probe"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nugomm1a520177probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177probe", "latest": {"3.4.0--r43hdfd78af_11": "sha256:96442ede7d8f039b9b069de58dc762389084e1900c11f524f5da6a9143e0476e"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:e32cc5b960ce529805f1dd88d9612768249976a143fa5af5dba07afdc55f5e19", "3.4.0--r42hdfd78af_10": "sha256:5ceb4a42ce1d9bde9ec49a0d824b9f16f02b1dbaaa0a2ecd47458b1266bdb16c", "3.4.0--r43hdfd78af_11": "sha256:96442ede7d8f039b9b069de58dc762389084e1900c11f524f5da6a9143e0476e"}, "docker": "quay.io/biocontainers/bioconductor-nugomm1a520177probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nugomm1a520177probe.
shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nugomm1a520177probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nugomm1a520177probe:3.4.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nugomm1a520177probe/3.4.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-nugomm1a520177probe/3.4.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nugomm1a520177probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugomm1a520177probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugomm1a520177probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nugomm1a520177probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nugomm1a520177probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nugomm1a520177probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nugomm1a520177probe

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