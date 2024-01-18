---
layout: container
name:  "quay.io/biocontainers/bioconductor-treeandleaf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-treeandleaf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-treeandleaf/container.yaml"
updated_at: "2024-01-18 03:10:39.814786"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-treeandleaf"

versions:
 - "1.6.1--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-treeandleaf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-treeandleaf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-treeandleaf", "latest": {"1.14.0--r43hdfd78af_0": "sha256:51e5dd9d542d7c5e81ad1cfc32aadd26c394621819af72f87ad8ea30e7ebd0f6"}, "tags": {"1.6.1--r41hdfd78af_0": "sha256:f22b244ff9cc1c0131b940dffa1b949eb3f7280c799ec0f3eef8d2f4c991d793", "1.10.0--r42hdfd78af_0": "sha256:05dde973b1e6ba18bc108d63194006bfcf79e8a7073163ca34666330f14e078a", "1.12.0--r43hdfd78af_0": "sha256:81dc94a5df8bf6809ed61d7cce7a68534fde268732cf419d23bb6043e7ec0372", "1.14.0--r43hdfd78af_0": "sha256:51e5dd9d542d7c5e81ad1cfc32aadd26c394621819af72f87ad8ea30e7ebd0f6"}, "docker": "quay.io/biocontainers/bioconductor-treeandleaf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-treeandleaf.
shpc-registry automated BioContainers addition for bioconductor-treeandleaf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-treeandleaf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-treeandleaf:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-treeandleaf/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-treeandleaf/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-treeandleaf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treeandleaf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treeandleaf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-treeandleaf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-treeandleaf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-treeandleaf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-treeandleaf

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