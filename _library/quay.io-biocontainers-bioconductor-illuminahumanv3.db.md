---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanv3.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanv3.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanv3.db/container.yaml"
updated_at: "2023-08-30 02:24:16.943343"
latest: "1.26.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanv3.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv3.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanv3.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv3.db", "latest": {"1.26.0--r43hdfd78af_11": "sha256:89f5b423ec3d3173abc3545769739a8fa0f0875e885f258f83b1ead21140ccb4"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:734410825a5aebe184d02cf278f12756a7ce4b51199232355371992d106c536b", "1.26.0--r42hdfd78af_10": "sha256:4e78bff6cd3c0348a67c9f0e5cc118d99a260e3558c3cbaf8ae2a2556331678b", "1.26.0--r43hdfd78af_11": "sha256:89f5b423ec3d3173abc3545769739a8fa0f0875e885f258f83b1ead21140ccb4"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanv3.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanv3.db.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanv3.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv3.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv3.db:1.26.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanv3.db/1.26.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-illuminahumanv3.db/1.26.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanv3.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv3.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv3.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanv3.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanv3.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanv3.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanv3.db

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