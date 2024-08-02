---
layout: container
name:  "quay.io/biocontainers/r-pscbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pscbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pscbs/container.yaml"
updated_at: "2024-08-02 02:47:29.865279"
latest: "0.67.0--r43h3121a25_0"
container_url: "https://biocontainers.pro/tools/r-pscbs"

versions:
 - "0.66.0--r41h3121a25_0"
 - "0.66.0--r42h3121a25_1"
 - "0.66.0--r43h3121a25_2"
 - "0.67.0--r43h3121a25_0"
description: "shpc-registry automated BioContainers addition for r-pscbs"
config: {"url": "https://biocontainers.pro/tools/r-pscbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-pscbs", "latest": {"0.67.0--r43h3121a25_0": "sha256:9eb32d984373f6b9e9e5a2b9a1fe1c6e09d07d5787b56ad5bbc489f7f818f76b"}, "tags": {"0.66.0--r41h3121a25_0": "sha256:439a2f5f549c0a0369afbb41f2750e61d29d454b7e62f31bdda6b17cd87dc622", "0.66.0--r42h3121a25_1": "sha256:1224df9657373c8a0b3085b26d93196ad61b45f03edf970348e1f0e31495f20a", "0.66.0--r43h3121a25_2": "sha256:2564625adc8bee84e11deb12207153e7cfc46ba9e30f236ad8807a76a4e65c47", "0.67.0--r43h3121a25_0": "sha256:9eb32d984373f6b9e9e5a2b9a1fe1c6e09d07d5787b56ad5bbc489f7f818f76b"}, "docker": "quay.io/biocontainers/r-pscbs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pscbs.
shpc-registry automated BioContainers addition for r-pscbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pscbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pscbs:0.67.0--r43h3121a25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pscbs/0.67.0--r43h3121a25_0
$ module help quay.io/biocontainers/r-pscbs/0.67.0--r43h3121a25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pscbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pscbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pscbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pscbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pscbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pscbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-pscbs

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