---
layout: container
name:  "quay.io/biocontainers/bioconductor-mi16cod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mi16cod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mi16cod.db/container.yaml"
updated_at: "2023-12-08 02:54:08.056439"
latest: "3.4.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mi16cod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mi16cod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mi16cod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mi16cod.db", "latest": {"3.4.0--r43hdfd78af_11": "sha256:8ccef5736d2230d69554935f693d0fe7e5f00f07a9b8d887c3e8375d66daf6ec"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:b8746b193edd334e3958bebfd9b4ee2842982147d140d6669e607e7a9fe5bdc4", "3.4.0--r42hdfd78af_10": "sha256:8f31db97bcb10c1d1a6c22eb8cd78d5b70e9ceaf3c6146463f57edb1ae58aefa", "3.4.0--r43hdfd78af_11": "sha256:8ccef5736d2230d69554935f693d0fe7e5f00f07a9b8d887c3e8375d66daf6ec"}, "docker": "quay.io/biocontainers/bioconductor-mi16cod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mi16cod.db.
shpc-registry automated BioContainers addition for bioconductor-mi16cod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mi16cod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mi16cod.db:3.4.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mi16cod.db/3.4.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mi16cod.db/3.4.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mi16cod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mi16cod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mi16cod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mi16cod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mi16cod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mi16cod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mi16cod.db

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