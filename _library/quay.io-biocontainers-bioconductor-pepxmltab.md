---
layout: container
name:  "quay.io/biocontainers/bioconductor-pepxmltab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pepxmltab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pepxmltab/container.yaml"
updated_at: "2025-07-28 09:49:24.784521"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pepxmltab"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_1"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pepxmltab"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pepxmltab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pepxmltab", "latest": {"1.40.0--r44hdfd78af_0": "sha256:42fa0e3d0bacaecc438d8e15c4586101c72eb8a93b83359b6570ed802dba9968"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:d993130a9ebefe27f21b66a878de618f12ef6285b7f5e2cbe652754364ac1094", "1.32.0--r42hdfd78af_0": "sha256:f941fe42e3ae27406915427b35bbce79cae4a5b79a6860bc327f8a3a063106e0", "1.34.0--r43hdfd78af_0": "sha256:92913f3466d7977894abe166e42e2f551216e4747c34f35069e760ccaa01261e", "1.36.0--r43hdfd78af_1": "sha256:79a90157529c57acd6809e0c012c1ec38e50adbbd2898453c54170a0a86686f3", "1.40.0--r44hdfd78af_0": "sha256:42fa0e3d0bacaecc438d8e15c4586101c72eb8a93b83359b6570ed802dba9968"}, "docker": "quay.io/biocontainers/bioconductor-pepxmltab"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pepxmltab.
shpc-registry automated BioContainers addition for bioconductor-pepxmltab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pepxmltab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pepxmltab:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pepxmltab/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pepxmltab/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pepxmltab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepxmltab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepxmltab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pepxmltab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pepxmltab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pepxmltab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pepxmltab

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