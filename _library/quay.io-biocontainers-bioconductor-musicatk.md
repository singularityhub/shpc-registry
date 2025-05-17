---
layout: container
name:  "quay.io/biocontainers/bioconductor-musicatk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-musicatk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-musicatk/container.yaml"
updated_at: "2025-05-17 03:25:44.703091"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-musicatk"
aliases:
 - "pandoc"
versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-musicatk"
config: {"url": "https://biocontainers.pro/tools/bioconductor-musicatk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-musicatk", "latest": {"1.12.0--r43hdfd78af_0": "sha256:db955614ec935076394185af10203aa6280b528a53f9a4403e27c6827b0c0e26"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:ba9ae41dfd5e2565eb3bb4472562095abd319411e499486fda46eeb8252b5c37", "1.8.0--r42hdfd78af_0": "sha256:c97cac1ab0b7ccd781de8a5afa1cacafdf689a2a19c15851e66b1b64bffc1bbe", "1.10.0--r43hdfd78af_0": "sha256:c5ce05cc4a05b0fc43e52977a8e64c9e04f307c03627aa5b5a40cca65fe99fc7", "1.12.0--r43hdfd78af_0": "sha256:db955614ec935076394185af10203aa6280b528a53f9a4403e27c6827b0c0e26"}, "docker": "quay.io/biocontainers/bioconductor-musicatk", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-musicatk.
shpc-registry automated BioContainers addition for bioconductor-musicatk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-musicatk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-musicatk:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-musicatk/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-musicatk/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-musicatk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-musicatk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-musicatk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-musicatk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-musicatk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-musicatk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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