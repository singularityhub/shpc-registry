---
layout: container
name:  "quay.io/biocontainers/bioconductor-xlaevis.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xlaevis.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xlaevis.db/container.yaml"
updated_at: "2025-11-06 03:20:51.865741"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-xlaevis.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-xlaevis.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xlaevis.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xlaevis.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:a2d94da5bae7e668148fab11ac046712adcf0b2c772d62e4ebe6e3832bb9e95b"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:0f501eb5d76b3e0c77eda0393677d6c6b17e31de1357b6c3bf07be4a9ff9b21e", "3.2.3--r42hdfd78af_10": "sha256:d29c1b33c91a7bbe6fe8d6cd6333b0f20b5f3c1ed5d0fddac63e589fc45e3ac2", "3.2.3--r43hdfd78af_11": "sha256:ef8fdbcac1d822505b4ca5841ae4c4b31ff39e6fe86bdb425ac3d654d1f41b5e", "3.2.3--r43hdfd78af_12": "sha256:493bff0a379462532a2f7a7416394571a93258501ef7108c11e6129996e5019b", "3.2.3--r44hdfd78af_13": "sha256:a2d94da5bae7e668148fab11ac046712adcf0b2c772d62e4ebe6e3832bb9e95b"}, "docker": "quay.io/biocontainers/bioconductor-xlaevis.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xlaevis.db.
shpc-registry automated BioContainers addition for bioconductor-xlaevis.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xlaevis.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xlaevis.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xlaevis.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-xlaevis.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xlaevis.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xlaevis.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xlaevis.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xlaevis.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xlaevis.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xlaevis.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xlaevis.db

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