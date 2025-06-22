---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db/container.yaml"
updated_at: "2025-06-22 03:35:19.642690"
latest: "1.26.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanwgdaslv3.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
 - "1.26.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanwgdaslv3.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanwgdaslv3.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanwgdaslv3.db", "latest": {"1.26.0--r44hdfd78af_13": "sha256:7ece7089a11fa5c5c6720cbf1e97e56134f6d98783d1ab24d0ca08d08948486b"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:223013993b0982d70a57e1dedad98a1d81da8234a25692ac89584992db3e5da9", "1.26.0--r42hdfd78af_10": "sha256:55202f938f913c53d0a24b83c0cfa5521482cac117dd2ba4c0e4301c63d9a5ce", "1.26.0--r43hdfd78af_11": "sha256:9b257b50b8bece0d58d42496cc712ebb4d0291faff764b27a39d2a9fe612c33c", "1.26.0--r43hdfd78af_12": "sha256:9add51dc1571386d9eeef3fe1bca8164364ecae1dd7559ce26cb6597f79aae8b", "1.26.0--r44hdfd78af_13": "sha256:7ece7089a11fa5c5c6720cbf1e97e56134f6d98783d1ab24d0ca08d08948486b"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanwgdaslv3.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db:1.26.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db/1.26.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-illuminahumanwgdaslv3.db/1.26.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanwgdaslv3.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanwgdaslv3.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanwgdaslv3.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanwgdaslv3.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanwgdaslv3.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanwgdaslv3.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanwgdaslv3.db

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