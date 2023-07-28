---
layout: container
name:  "quay.io/biocontainers/gatk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gatk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gatk/container.yaml"
updated_at: "2023-07-28 03:22:06.919711"
latest: "3.8--hdfd78af_11"
container_url: "https://biocontainers.pro/tools/gatk"

versions:
 - "3.8--9"
 - "3.8--hdfd78af_11"
description: "shpc-registry automated BioContainers addition for gatk"
config: {"url": "https://biocontainers.pro/tools/gatk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gatk", "latest": {"3.8--hdfd78af_11": "sha256:8f1ee6b1a419132bda968af90c9abcd1ea1f48eb9780cff408438e59fe6615c5"}, "tags": {"3.8--9": "sha256:e07c301b41224bd79f114438945677e3c62339d84e96659be29315c2b6d6c5db", "3.8--hdfd78af_11": "sha256:8f1ee6b1a419132bda968af90c9abcd1ea1f48eb9780cff408438e59fe6615c5"}, "docker": "quay.io/biocontainers/gatk"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gatk.
shpc-registry automated BioContainers addition for gatk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gatk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gatk:3.8--hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gatk/3.8--hdfd78af_11
$ module help quay.io/biocontainers/gatk/3.8--hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gatk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gatk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gatk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gatk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gatk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gatk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gatk

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