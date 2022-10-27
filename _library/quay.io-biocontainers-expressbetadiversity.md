---
layout: container
name:  "quay.io/biocontainers/expressbetadiversity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/expressbetadiversity/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/expressbetadiversity/container.yaml"
updated_at: "2022-10-27 01:04:43.810859"
latest: "1.0.10--h9f5acd7_3"
container_url: "https://biocontainers.pro/tools/expressbetadiversity"
aliases:
 - "AbstractPlot.py"
 - "ExpressBetaDiversity"
 - "convertToEBD.py"
 - "convertToFullMatrix.py"
 - "pcoaPlot.py"
versions:
 - "1.0.10--h9f5acd7_3"
description: "shpc-registry automated BioContainers addition for expressbetadiversity"
config: {"url": "https://biocontainers.pro/tools/expressbetadiversity", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for expressbetadiversity", "latest": {"1.0.10--h9f5acd7_3": "sha256:76a28028846c5b78d430ff2646a91fa980827269c99c22b15fd791eff6c00d90"}, "tags": {"1.0.10--h9f5acd7_3": "sha256:76a28028846c5b78d430ff2646a91fa980827269c99c22b15fd791eff6c00d90"}, "docker": "quay.io/biocontainers/expressbetadiversity", "aliases": {"AbstractPlot.py": "/usr/local/bin/AbstractPlot.py", "ExpressBetaDiversity": "/usr/local/bin/ExpressBetaDiversity", "convertToEBD.py": "/usr/local/bin/convertToEBD.py", "convertToFullMatrix.py": "/usr/local/bin/convertToFullMatrix.py", "pcoaPlot.py": "/usr/local/bin/pcoaPlot.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/expressbetadiversity.
shpc-registry automated BioContainers addition for expressbetadiversity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/expressbetadiversity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/expressbetadiversity:1.0.10--h9f5acd7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/expressbetadiversity/1.0.10--h9f5acd7_3
$ module help quay.io/biocontainers/expressbetadiversity/1.0.10--h9f5acd7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### expressbetadiversity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### expressbetadiversity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### expressbetadiversity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### expressbetadiversity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### expressbetadiversity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### expressbetadiversity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AbstractPlot.py

```bash
$ singularity exec <container> /usr/local/bin/AbstractPlot.py
$ podman run --it --rm --entrypoint /usr/local/bin/AbstractPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AbstractPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ExpressBetaDiversity

```bash
$ singularity exec <container> /usr/local/bin/ExpressBetaDiversity
$ podman run --it --rm --entrypoint /usr/local/bin/ExpressBetaDiversity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ExpressBetaDiversity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertToEBD.py

```bash
$ singularity exec <container> /usr/local/bin/convertToEBD.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertToEBD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertToEBD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertToFullMatrix.py

```bash
$ singularity exec <container> /usr/local/bin/convertToFullMatrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertToFullMatrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertToFullMatrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcoaPlot.py

```bash
$ singularity exec <container> /usr/local/bin/pcoaPlot.py
$ podman run --it --rm --entrypoint /usr/local/bin/pcoaPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcoaPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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