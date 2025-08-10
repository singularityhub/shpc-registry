---
layout: container
name:  "quay.io/biocontainers/bioconductor-htmg430a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htmg430a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htmg430a.db/container.yaml"
updated_at: "2025-08-10 04:36:00.626849"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-htmg430a.db"

versions:
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-htmg430a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htmg430a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htmg430a.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:6df3910404f8d0d5982e5fa734ef44bc879dd11953744ac377e697e091166c79"}, "tags": {"3.13.0--r41hdfd78af_1": "sha256:20cdaac3ec2b5a8add9e47f9e48e9d207c836ecfa3825052e996f128bba5a46f", "3.13.0--r42hdfd78af_2": "sha256:04c19e93f8b1d1ded4d0077119978f436d5f947310855f7bc0ed24e216f8e0db", "3.13.0--r43hdfd78af_3": "sha256:ef5a1ecf5c82a5a96716e41542447d72f9e8bcf3075e8bdb819853645da3e0bb", "3.13.0--r43hdfd78af_4": "sha256:3c6f704c8eed279aa0542f264fd52301792a5932389ab3e491ef519cddfca38a", "3.13.0--r44hdfd78af_5": "sha256:6df3910404f8d0d5982e5fa734ef44bc879dd11953744ac377e697e091166c79"}, "docker": "quay.io/biocontainers/bioconductor-htmg430a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htmg430a.db.
shpc-registry automated BioContainers addition for bioconductor-htmg430a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430a.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htmg430a.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-htmg430a.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htmg430a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htmg430a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htmg430a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htmg430a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htmg430a.db

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