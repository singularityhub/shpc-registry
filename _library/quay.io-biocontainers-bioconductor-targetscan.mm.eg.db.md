---
layout: container
name:  "quay.io/biocontainers/bioconductor-targetscan.mm.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-targetscan.mm.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-targetscan.mm.eg.db/container.yaml"
updated_at: "2025-09-24 03:23:25.413915"
latest: "0.6.1--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-targetscan.mm.eg.db"

versions:
 - "0.6.1--r41hdfd78af_9"
 - "0.6.1--r42hdfd78af_10"
 - "0.6.1--r43hdfd78af_11"
 - "0.6.1--r43hdfd78af_12"
 - "0.6.1--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-targetscan.mm.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-targetscan.mm.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-targetscan.mm.eg.db", "latest": {"0.6.1--r44hdfd78af_13": "sha256:ea3f2da1f31483fbc357f294ee2d25a7d1cfc92b03220779e4f5f0ed1fbd974e"}, "tags": {"0.6.1--r41hdfd78af_9": "sha256:e59c1d04db1c3bbe88ca3073fb9aa4e80a8b611befb95f6e6c35eac318bca418", "0.6.1--r42hdfd78af_10": "sha256:373bee41bad87df957ae1212a0db1935f3031c0970663e17ccbf2e80391d720e", "0.6.1--r43hdfd78af_11": "sha256:0931ee031ae17d0bd9f155237529fe7083ddf255d7a084532640b08d46983c83", "0.6.1--r43hdfd78af_12": "sha256:f44d59a50c6e0e4c70ab77c2f687536e77d695ceb2e24c5479e65acb16d068d8", "0.6.1--r44hdfd78af_13": "sha256:ea3f2da1f31483fbc357f294ee2d25a7d1cfc92b03220779e4f5f0ed1fbd974e"}, "docker": "quay.io/biocontainers/bioconductor-targetscan.mm.eg.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-targetscan.mm.eg.db.
shpc-registry automated BioContainers addition for bioconductor-targetscan.mm.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-targetscan.mm.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-targetscan.mm.eg.db:0.6.1--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-targetscan.mm.eg.db/0.6.1--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-targetscan.mm.eg.db/0.6.1--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-targetscan.mm.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetscan.mm.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetscan.mm.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-targetscan.mm.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-targetscan.mm.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-targetscan.mm.eg.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-targetscan.mm.eg.db

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