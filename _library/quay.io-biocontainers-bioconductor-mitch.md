---
layout: container
name:  "quay.io/biocontainers/bioconductor-mitch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mitch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mitch/container.yaml"
updated_at: "2025-02-25 03:35:54.988299"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mitch"
aliases:
 - "pandoc"
versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mitch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mitch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mitch", "latest": {"1.14.0--r43hdfd78af_0": "sha256:71730e21e08743bed6d20046b3d9f3c6d545fa54aa1cec9bd8933d78c8819a0d"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:72a0ef1a0fac977bca1c82ed2fce643f77f455fcd4c30b1164bf4df3800a023d", "1.10.0--r42hdfd78af_0": "sha256:f0b40e378bf757a13a7284f79d81007e5054b0ff4406f78e9ea1782b4e0792a9", "1.12.0--r43hdfd78af_0": "sha256:6c7c02a6a6fcdaa1291e3d27695c4454b7d11dc422c3563dfd51904db0ffedea", "1.14.0--r43hdfd78af_0": "sha256:71730e21e08743bed6d20046b3d9f3c6d545fa54aa1cec9bd8933d78c8819a0d"}, "docker": "quay.io/biocontainers/bioconductor-mitch", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mitch.
shpc-registry automated BioContainers addition for bioconductor-mitch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mitch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mitch:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mitch/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mitch/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mitch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mitch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mitch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mitch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mitch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mitch-inspect-deffile:

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