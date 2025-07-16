---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaseqsamplesize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaseqsamplesize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaseqsamplesize/container.yaml"
updated_at: "2025-07-16 04:13:42.381249"
latest: "2.16.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaseqsamplesize"

versions:
 - "2.4.1--r41hc247a5b_1"
 - "2.8.0--r42hc247a5b_0"
 - "2.8.0--r42hf17093f_1"
 - "2.10.0--r43hf17093f_0"
 - "2.12.0--r43hf17093f_0"
 - "2.16.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaseqsamplesize"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaseqsamplesize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaseqsamplesize", "latest": {"2.16.0--r44he5774e6_0": "sha256:e8ca410ce1460686e6ff5eb1270d6309ad82dfb782f8e320fc713f365efe0282"}, "tags": {"2.4.1--r41hc247a5b_1": "sha256:d3afd62e336e0e70ded562decfeb76b9c3f5e426d4603367edee704542799cc7", "2.8.0--r42hc247a5b_0": "sha256:e2bb6da2be99845a36ad07c076d57395fb319fbe5e8eac3be28d4218a5ad8214", "2.8.0--r42hf17093f_1": "sha256:dc79aac70a9852bbecf01a725035e6d71a778a0b21d1825f5792b4a4eb1c3631", "2.10.0--r43hf17093f_0": "sha256:f6e18008c1db645f2c24f19497386dd7a5b147e6a628f250a67761c42e90b783", "2.12.0--r43hf17093f_0": "sha256:31765282f6557ef05046c233b9dc8e14d332b4c1fa3d4031e608c0d1a10dc04e", "2.16.0--r44he5774e6_0": "sha256:e8ca410ce1460686e6ff5eb1270d6309ad82dfb782f8e320fc713f365efe0282"}, "docker": "quay.io/biocontainers/bioconductor-rnaseqsamplesize"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaseqsamplesize.
shpc-registry automated BioContainers addition for bioconductor-rnaseqsamplesize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqsamplesize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqsamplesize:2.16.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaseqsamplesize/2.16.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-rnaseqsamplesize/2.16.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaseqsamplesize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqsamplesize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqsamplesize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaseqsamplesize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaseqsamplesize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaseqsamplesize-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnaseqsamplesize

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