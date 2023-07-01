---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtcga.mrna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtcga.mrna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtcga.mrna/container.yaml"
updated_at: "2023-07-01 03:30:35.792250"
latest: "1.25.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtcga.mrna"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.25.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_1"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.17.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtcga.mrna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtcga.mrna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtcga.mrna", "latest": {"1.25.0--r42hdfd78af_0": "sha256:8e070c6feafdf81b201b0a8b271567882d2b06e8b173a1335a569d477ea546f3"}, "tags": {"1.8.0--r351_0": "sha256:e997891a35892b582f188b274aa7367278bbc4050861ea98aab5a0944978d57f", "1.25.0--r42hdfd78af_0": "sha256:8e070c6feafdf81b201b0a8b271567882d2b06e8b173a1335a569d477ea546f3", "1.22.0--r41hdfd78af_1": "sha256:7c2c857e49bc3589283b906a552ac9931e7b34bb554b3d650e42fdc53609d6b9", "1.20.0--r41hdfd78af_0": "sha256:2574b5315f59d0ed089d1b4fde1bf8806b05e64dd532ffd5b8c8d35d200e9569", "1.18.0--r40hdfd78af_1": "sha256:d60cfd7e13af0cc38dcb4473b9ca2853659493fb06d8f3160d3d7a4122456af3", "1.17.0--r40_0": "sha256:5fd5a1e14590ae50c4842030d12e7f3fff20fb237e816e5badccee62ce1be358"}, "docker": "quay.io/biocontainers/bioconductor-rtcga.mrna", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtcga.mrna.
shpc-registry automated BioContainers addition for bioconductor-rtcga.mrna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga.mrna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtcga.mrna:1.25.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtcga.mrna/1.25.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtcga.mrna/1.25.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtcga.mrna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga.mrna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtcga.mrna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtcga.mrna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtcga.mrna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtcga.mrna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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