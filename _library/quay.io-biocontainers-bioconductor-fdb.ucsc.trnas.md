---
layout: container
name:  "quay.io/biocontainers/bioconductor-fdb.ucsc.trnas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fdb.ucsc.trnas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fdb.ucsc.trnas/container.yaml"
updated_at: "2023-08-06 02:58:46.479532"
latest: "1.0.1--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-fdb.ucsc.trnas"

versions:
 - "1.0.1--r41hdfd78af_9"
 - "1.0.1--r42hdfd78af_10"
 - "1.0.1--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.trnas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fdb.ucsc.trnas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.trnas", "latest": {"1.0.1--r43hdfd78af_11": "sha256:91618418996d28d0a3b3998ffc2e69bcb15ba01c316141da9a33816e1f47b6b5"}, "tags": {"1.0.1--r41hdfd78af_9": "sha256:78f1ad565ff78166c336a43a03df41516e941ab2d5aca1de3112ca0c58b73828", "1.0.1--r42hdfd78af_10": "sha256:7d413ca44e00c55ab3f786581bb560e0550aadd2e7cc145ba89d8667343b0ffd", "1.0.1--r43hdfd78af_11": "sha256:91618418996d28d0a3b3998ffc2e69bcb15ba01c316141da9a33816e1f47b6b5"}, "docker": "quay.io/biocontainers/bioconductor-fdb.ucsc.trnas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fdb.ucsc.trnas.
shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.trnas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.ucsc.trnas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.ucsc.trnas:1.0.1--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fdb.ucsc.trnas/1.0.1--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-fdb.ucsc.trnas/1.0.1--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fdb.ucsc.trnas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.ucsc.trnas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.ucsc.trnas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fdb.ucsc.trnas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fdb.ucsc.trnas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fdb.ucsc.trnas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fdb.ucsc.trnas

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