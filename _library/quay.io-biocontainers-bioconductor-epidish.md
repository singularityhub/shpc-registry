---
layout: container
name:  "quay.io/biocontainers/bioconductor-epidish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epidish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epidish/container.yaml"
updated_at: "2025-11-14 04:47:54.594049"
latest: "2.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epidish"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.16.0--r43hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
 - "2.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epidish"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epidish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epidish", "latest": {"2.22.0--r44hdfd78af_0": "sha256:9328a79015499e6dc2804b06045b83e629ac972f4ae87915a1dc17dae2646808"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:14ea3ce2c3d085a751707b287ea73aa94c626fb5cd50bd3b162e0dbe73faeb5e", "2.14.0--r42hdfd78af_0": "sha256:097ae430309be40893a320bb51c99888f2ca8a803e550c67201a6573e2788ef0", "2.10.0--r41hdfd78af_0": "sha256:0a2a630fd4a8c0e11a895c1fb75ac616e615e4d96f9fb70b0677ed48e6b832ea", "2.16.0--r43hdfd78af_0": "sha256:fb7c44b0a9564a032556bd90910ccd6601c095291c3ec8ba4149c04cbed225c5", "2.18.0--r43hdfd78af_0": "sha256:b87d88bc173bee613c12048217611f77a61cb412a5c1d6b1fba7e40f2aa10f72", "2.22.0--r44hdfd78af_0": "sha256:9328a79015499e6dc2804b06045b83e629ac972f4ae87915a1dc17dae2646808"}, "docker": "quay.io/biocontainers/bioconductor-epidish", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epidish.
shpc-registry automated BioContainers addition for bioconductor-epidish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epidish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epidish:2.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epidish/2.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epidish/2.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epidish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epidish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epidish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epidish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epidish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epidish-inspect-deffile:

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