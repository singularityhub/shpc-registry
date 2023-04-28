---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqcna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqcna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqcna/container.yaml"
updated_at: "2023-04-28 02:58:44.606703"
latest: "1.44.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqcna"

versions:
 - "1.40.0--r41hc247a5b_2"
 - "1.44.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqcna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqcna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqcna", "latest": {"1.44.0--r42hc247a5b_0": "sha256:dcfb94043053a5c4001e5da3794c29552ba5dcaa44e7945cda525e9973019a1f"}, "tags": {"1.40.0--r41hc247a5b_2": "sha256:261ec3ce7def9d6908e4305604a465f859e023d6d8dc0a4a9d66dc81ad077df2", "1.44.0--r42hc247a5b_0": "sha256:dcfb94043053a5c4001e5da3794c29552ba5dcaa44e7945cda525e9973019a1f"}, "docker": "quay.io/biocontainers/bioconductor-seqcna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqcna.
shpc-registry automated BioContainers addition for bioconductor-seqcna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcna:1.44.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqcna/1.44.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-seqcna/1.44.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqcna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqcna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqcna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqcna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqcna

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