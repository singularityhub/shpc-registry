---
layout: container
name:  "quay.io/biocontainers/r-histonehmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-histonehmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-histonehmm/container.yaml"
updated_at: "2025-01-12 03:30:44.452378"
latest: "1.8--r42h8537716_6"
container_url: "https://biocontainers.pro/tools/r-histonehmm"
aliases:
 - "pandoc"
versions:
 - "1.8--r41h1aed7a7_4"
 - "1.8--r42h1aed7a7_5"
 - "1.8--r42h8537716_6"
description: "shpc-registry automated BioContainers addition for r-histonehmm"
config: {"url": "https://biocontainers.pro/tools/r-histonehmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-histonehmm", "latest": {"1.8--r42h8537716_6": "sha256:4d137667bd4c29d67aa5c6f925b851fdbfeb8c754c8448ea7b2895f8f43e01f9"}, "tags": {"1.8--r41h1aed7a7_4": "sha256:8f06c1153c46e6329a9ae138cef7e9987e0ad43a62bb5f635bfd7887424938cc", "1.8--r42h1aed7a7_5": "sha256:d21332c0fea4272db83825026c4e1a2293971e67d4271eaecdd500b324c1957c", "1.8--r42h8537716_6": "sha256:4d137667bd4c29d67aa5c6f925b851fdbfeb8c754c8448ea7b2895f8f43e01f9"}, "docker": "quay.io/biocontainers/r-histonehmm", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-histonehmm.
shpc-registry automated BioContainers addition for r-histonehmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-histonehmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-histonehmm:1.8--r42h8537716_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-histonehmm/1.8--r42h8537716_6
$ module help quay.io/biocontainers/r-histonehmm/1.8--r42h8537716_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-histonehmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-histonehmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-histonehmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-histonehmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-histonehmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-histonehmm-inspect-deffile:

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