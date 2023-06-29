---
layout: container
name:  "quay.io/biocontainers/bioconductor-targetscan.hs.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-targetscan.hs.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-targetscan.hs.eg.db/container.yaml"
updated_at: "2023-06-29 03:18:09.100033"
latest: "0.6.1--r42hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-targetscan.hs.eg.db"

versions:
 - "0.6.1--r41hdfd78af_9"
 - "0.6.1--r42hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-targetscan.hs.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-targetscan.hs.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-targetscan.hs.eg.db", "latest": {"0.6.1--r42hdfd78af_11": "sha256:de7bc99a57bd705348ecf63afbc86c936bcc454caee0c34064fdec2e36e3e13a"}, "tags": {"0.6.1--r41hdfd78af_9": "sha256:bae8ffba00388284ac8a89349c694908924828212d4b10f9cf917a0c57dae96d", "0.6.1--r42hdfd78af_11": "sha256:de7bc99a57bd705348ecf63afbc86c936bcc454caee0c34064fdec2e36e3e13a"}, "docker": "quay.io/biocontainers/bioconductor-targetscan.hs.eg.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-targetscan.hs.eg.db.
shpc-registry automated BioContainers addition for bioconductor-targetscan.hs.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-targetscan.hs.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-targetscan.hs.eg.db:0.6.1--r42hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-targetscan.hs.eg.db/0.6.1--r42hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-targetscan.hs.eg.db/0.6.1--r42hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-targetscan.hs.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetscan.hs.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetscan.hs.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-targetscan.hs.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-targetscan.hs.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-targetscan.hs.eg.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-targetscan.hs.eg.db

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