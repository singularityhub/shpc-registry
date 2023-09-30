---
layout: container
name:  "quay.io/biocontainers/bioconductor-ngsreports"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ngsreports/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ngsreports/container.yaml"
updated_at: "2023-09-30 02:37:41.289171"
latest: "2.2.4--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ngsreports"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "2.0.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "2.2.4--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ngsreports"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ngsreports", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ngsreports", "latest": {"2.2.4--r43hdfd78af_0": "sha256:67c7b65a91f1dfa4f50e105efef98d54628c17e671491c522773f6d3221ce7ff"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:61e7866c4ec6d14a9455a0cdca31172af7563078c630034baff5646226d62d27", "2.0.0--r42hdfd78af_0": "sha256:9a8c4b120bff007beb5c060b9e3091db19689643953832b06776670cb36b880a", "1.10.0--r41hdfd78af_0": "sha256:f0805db5366c69b5ab012cf76776732a8ac825048efeda8193c049595ad7f4b6", "2.2.4--r43hdfd78af_0": "sha256:67c7b65a91f1dfa4f50e105efef98d54628c17e671491c522773f6d3221ce7ff"}, "docker": "quay.io/biocontainers/bioconductor-ngsreports", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ngsreports.
shpc-registry automated BioContainers addition for bioconductor-ngsreports
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ngsreports
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ngsreports:2.2.4--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ngsreports/2.2.4--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ngsreports/2.2.4--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ngsreports-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ngsreports-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ngsreports-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ngsreports-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ngsreports-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ngsreports-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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