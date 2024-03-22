---
layout: container
name:  "quay.io/biocontainers/bioconductor-ipddb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ipddb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ipddb/container.yaml"
updated_at: "2024-03-22 02:27:28.943657"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ipddb"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ipddb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ipddb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ipddb", "latest": {"1.20.0--r43hdfd78af_0": "sha256:c1864eb4c97a7340346b2637848e7dfbacb29fc85ad15dbb9b66a58430fa8811"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:91835ac77fcf2840c1ab73d9bcbc4414eb5af3abcba74a3162634b84b3dd775b", "1.16.0--r42hdfd78af_0": "sha256:d1bb67105aae38158066107d2aa7ac5accb28a0b3c6e27970f80f002a52206cd", "1.12.0--r41hdfd78af_0": "sha256:463b74e5728f243178e507dfbef1f953e51456a7f29e0ff5d881b4fc1f0fd8ad", "1.10.0--r41hdfd78af_0": "sha256:8068428255e453a9686d367201a663be11ac39e3bb9820e2ea3eeefc6ca37af7", "1.18.0--r43hdfd78af_0": "sha256:e19a6107b4e527d7ae1df78abec8707888b6e0d1f483ccb96ff4e7ef61d7f030", "1.20.0--r43hdfd78af_0": "sha256:c1864eb4c97a7340346b2637848e7dfbacb29fc85ad15dbb9b66a58430fa8811"}, "docker": "quay.io/biocontainers/bioconductor-ipddb", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ipddb.
shpc-registry automated BioContainers addition for bioconductor-ipddb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ipddb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ipddb:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ipddb/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ipddb/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ipddb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ipddb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ipddb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ipddb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ipddb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ipddb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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