---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanv4.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanv4.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanv4.db/container.yaml"
updated_at: "2024-08-25 03:25:38.403028"
latest: "1.26.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanv4.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv4.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanv4.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv4.db", "latest": {"1.26.0--r43hdfd78af_12": "sha256:11be00f076f42aafd8561b91a7f7d7be17816d851c9c0cc9eda8c7e77b9e13ce"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:cf07e8a7400d6c2c340076dd04cf614ee0a33a441495df13c7572bdccc292c8f", "1.26.0--r42hdfd78af_10": "sha256:9fc6f764e6f145cf216e68da0f9fe93255d0094d3fb3f0436330b1ee41b11574", "1.26.0--r43hdfd78af_11": "sha256:adbeed7327f7e4f749b8995e8ff21bfb04a6874ab1d0a5ee4f03e973a82f1c80", "1.26.0--r43hdfd78af_12": "sha256:11be00f076f42aafd8561b91a7f7d7be17816d851c9c0cc9eda8c7e77b9e13ce"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanv4.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanv4.db.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanv4.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv4.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv4.db:1.26.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanv4.db/1.26.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-illuminahumanv4.db/1.26.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanv4.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv4.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv4.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanv4.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanv4.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanv4.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanv4.db

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