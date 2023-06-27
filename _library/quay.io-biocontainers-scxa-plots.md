---
layout: container
name:  "quay.io/biocontainers/scxa-plots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scxa-plots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scxa-plots/container.yaml"
updated_at: "2023-06-27 03:04:50.026083"
latest: "0.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/scxa-plots"
aliases:
 - "dropletBarcodePlot.R"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for scxa-plots"
config: {"url": "https://biocontainers.pro/tools/scxa-plots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scxa-plots", "latest": {"0.0.1--hdfd78af_1": "sha256:2c7d3cf8e4a7e4c89e5cc4830770b4d97e791b47945a945307a5043d340ee17f"}, "tags": {"0.0.1--hdfd78af_1": "sha256:2c7d3cf8e4a7e4c89e5cc4830770b4d97e791b47945a945307a5043d340ee17f"}, "docker": "quay.io/biocontainers/scxa-plots", "aliases": {"dropletBarcodePlot.R": "/usr/local/bin/dropletBarcodePlot.R", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scxa-plots.
shpc-registry automated BioContainers addition for scxa-plots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scxa-plots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scxa-plots:0.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scxa-plots/0.0.1--hdfd78af_1
$ module help quay.io/biocontainers/scxa-plots/0.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scxa-plots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scxa-plots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scxa-plots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scxa-plots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scxa-plots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scxa-plots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dropletBarcodePlot.R

```bash
$ singularity exec <container> /usr/local/bin/dropletBarcodePlot.R
$ podman run --it --rm --entrypoint /usr/local/bin/dropletBarcodePlot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropletBarcodePlot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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