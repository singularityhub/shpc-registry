---
layout: container
name:  "quay.io/biocontainers/bioconductor-generxcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-generxcluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-generxcluster/container.yaml"
updated_at: "2024-01-18 03:16:10.848719"
latest: "1.38.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-generxcluster"

versions:
 - "1.30.0--r41hc0cfd56_2"
 - "1.34.0--r42hc0cfd56_0"
 - "1.34.0--r42ha9d7317_1"
 - "1.36.0--r43ha9d7317_0"
 - "1.38.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-generxcluster"
config: {"url": "https://biocontainers.pro/tools/bioconductor-generxcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-generxcluster", "latest": {"1.38.0--r43ha9d7317_0": "sha256:11bef2376a8145df8756364b28c129b388ad0820dfc9ffba8d8c4412d09c8739"}, "tags": {"1.30.0--r41hc0cfd56_2": "sha256:f7efd6b08460fb73df4e389200b2ca8749c6d3807fa3eeaea4acd2553eba606d", "1.34.0--r42hc0cfd56_0": "sha256:efe76aaae4ee8c8d1a1799c3694dea5c43f4e80a0510f70826eb4517b99eac37", "1.34.0--r42ha9d7317_1": "sha256:c9189410c5923dd9a1725bf265e035d780daa698455e3d464e3ee5e662f8f9f8", "1.36.0--r43ha9d7317_0": "sha256:a028f506340e1458bbfe94a01c8525ae60dda0d55c3b38fb2814b74bcd272902", "1.38.0--r43ha9d7317_0": "sha256:11bef2376a8145df8756364b28c129b388ad0820dfc9ffba8d8c4412d09c8739"}, "docker": "quay.io/biocontainers/bioconductor-generxcluster"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-generxcluster.
shpc-registry automated BioContainers addition for bioconductor-generxcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-generxcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-generxcluster:1.38.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-generxcluster/1.38.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-generxcluster/1.38.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-generxcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-generxcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-generxcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-generxcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-generxcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-generxcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-generxcluster

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