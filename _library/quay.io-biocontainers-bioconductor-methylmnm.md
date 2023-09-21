---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylmnm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylmnm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylmnm/container.yaml"
updated_at: "2023-09-21 02:57:45.807530"
latest: "1.38.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylmnm"

versions:
 - "1.32.0--r41hc0cfd56_2"
 - "1.36.0--r42hc0cfd56_0"
 - "1.36.0--r42ha9d7317_1"
 - "1.38.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylmnm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylmnm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylmnm", "latest": {"1.38.0--r43ha9d7317_0": "sha256:0a5a1291b8e59c8de932902c8566c465f189e3a994f2a16e062c9d4cb5475516"}, "tags": {"1.32.0--r41hc0cfd56_2": "sha256:76db74e93222fe45d45b039dc5148f5358756aa274897d1ac54ec05530fb4178", "1.36.0--r42hc0cfd56_0": "sha256:87a100f6d8389c8addab16a4435e1c2566ced3978e21efdb579933ba2a9bd36e", "1.36.0--r42ha9d7317_1": "sha256:cbff63a479c6d5e16e94480946e85885a9a5bf7dd5f546d6eb69c1bb8363baa2", "1.38.0--r43ha9d7317_0": "sha256:0a5a1291b8e59c8de932902c8566c465f189e3a994f2a16e062c9d4cb5475516"}, "docker": "quay.io/biocontainers/bioconductor-methylmnm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylmnm.
shpc-registry automated BioContainers addition for bioconductor-methylmnm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylmnm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylmnm:1.38.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylmnm/1.38.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-methylmnm/1.38.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylmnm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylmnm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylmnm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylmnm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylmnm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylmnm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylmnm

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