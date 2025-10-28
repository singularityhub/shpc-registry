---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db/container.yaml"
updated_at: "2025-10-28 04:02:57.196378"
latest: "1.26.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanwgdaslv4.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
 - "1.26.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanwgdaslv4.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanwgdaslv4.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanwgdaslv4.db", "latest": {"1.26.0--r44hdfd78af_13": "sha256:aaf0d464eed9e6d65c968f3045f90bc91f346d55b70def76fd5a714305ea2ecb"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:d5ed88772ad0b53cd2f2e482a4192510521481961b8b6a3bce474b294c0e3d6b", "1.26.0--r42hdfd78af_10": "sha256:516ed81ae5b6971b80d5d5db1fb26ab2e44b5548610fe6e984b23c3d26b28e60", "1.26.0--r43hdfd78af_11": "sha256:03f18f76f889b18fa256fbfc59959dcab299086fb23d3b29646d6283bad7730d", "1.26.0--r43hdfd78af_12": "sha256:e4cf875f4533b3901bc05ae98989a12260880525dd25e7bd235fd39c282ce095", "1.26.0--r44hdfd78af_13": "sha256:aaf0d464eed9e6d65c968f3045f90bc91f346d55b70def76fd5a714305ea2ecb"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanwgdaslv4.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db:1.26.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db/1.26.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-illuminahumanwgdaslv4.db/1.26.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanwgdaslv4.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanwgdaslv4.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanwgdaslv4.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanwgdaslv4.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanwgdaslv4.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanwgdaslv4.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanwgdaslv4.db

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