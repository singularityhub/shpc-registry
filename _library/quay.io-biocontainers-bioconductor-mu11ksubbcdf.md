---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu11ksubbcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu11ksubbcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu11ksubbcdf/container.yaml"
updated_at: "2024-08-15 04:07:22.185445"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mu11ksubbcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mu11ksubbcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu11ksubbcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu11ksubbcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:ea47f99bb20f961e1059d1b9a1d763f8ebbbee3a361eb3f475efd94d790343db"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:e5bf35c9302598c696aa379d989a3bb01b056d139d65f5695e22e923821251c1", "2.18.0--r42hdfd78af_10": "sha256:09d3e600423b531694280f4c673c000658074b0bbf6f88c121e1efba400fd7c1", "2.18.0--r43hdfd78af_11": "sha256:352b2c63871017ca748b1957598f4b9272600bec55682cc55b628353bf17aabf", "2.18.0--r43hdfd78af_12": "sha256:ea47f99bb20f961e1059d1b9a1d763f8ebbbee3a361eb3f475efd94d790343db"}, "docker": "quay.io/biocontainers/bioconductor-mu11ksubbcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu11ksubbcdf.
shpc-registry automated BioContainers addition for bioconductor-mu11ksubbcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubbcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubbcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu11ksubbcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mu11ksubbcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu11ksubbcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubbcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubbcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu11ksubbcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu11ksubbcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu11ksubbcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu11ksubbcdf

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