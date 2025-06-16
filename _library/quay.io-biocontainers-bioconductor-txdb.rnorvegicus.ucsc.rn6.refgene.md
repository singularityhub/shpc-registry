---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene/container.yaml"
updated_at: "2025-06-16 04:42:39.721598"
latest: "3.4.6--r44hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene"

versions:
 - "3.4.6--r41hdfd78af_8"
 - "3.4.6--r42hdfd78af_9"
 - "3.4.6--r43hdfd78af_10"
 - "3.4.6--r43hdfd78af_11"
 - "3.4.6--r44hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene", "latest": {"3.4.6--r44hdfd78af_12": "sha256:c8f3dacff3f5ae641e69a3c3b328e6d17b08c1ee18427959065227e6dc2b2be6"}, "tags": {"3.4.6--r41hdfd78af_8": "sha256:54a045a5a2b8dc001f5713c361b890c9ee6d8c93b58a4c22f3b3710b5c81ce39", "3.4.6--r42hdfd78af_9": "sha256:207638b5bc382881b11b12c5fdd2fe5e60d7ec8d43c4e74923f167a84c753e0b", "3.4.6--r43hdfd78af_10": "sha256:8f227bb7a05e933787951cb88a932f2ba16450513eba508bd98ca31a51b11c2b", "3.4.6--r43hdfd78af_11": "sha256:3830cfe46b8591dba2056e74f5c0f3a1b44df6d4b7fa363742277e7a477148c3", "3.4.6--r44hdfd78af_12": "sha256:c8f3dacff3f5ae641e69a3c3b328e6d17b08c1ee18427959065227e6dc2b2be6"}, "docker": "quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene:3.4.6--r44hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene/3.4.6--r44hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene/3.4.6--r44hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene

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