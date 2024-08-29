---
layout: container
name:  "quay.io/biocontainers/bioconductor-rmassbankdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rmassbankdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rmassbankdata/container.yaml"
updated_at: "2024-08-29 11:25:06.188609"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rmassbankdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rmassbankdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rmassbankdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rmassbankdata", "latest": {"1.40.0--r43hdfd78af_0": "sha256:4a431000420117115398c5fd2b5f59b85ed1feb04f045ba56b328f19462ba4a9"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:c9731852a3fc4279577aa862dca9e8f4a9fbe4c833b14f4cb2ae41bdf85d09ee", "1.35.0--r42hdfd78af_0": "sha256:50ee96fbe62897c9677fcbac8c7ef44c694ccd186069cd3b5a0d764b66665950", "1.38.0--r43hdfd78af_0": "sha256:34eed4da6ca70dd18be3dfb1244bfbb7d09ffd3f1b5d98782a2963cb8e5a9a55", "1.40.0--r43hdfd78af_0": "sha256:4a431000420117115398c5fd2b5f59b85ed1feb04f045ba56b328f19462ba4a9"}, "docker": "quay.io/biocontainers/bioconductor-rmassbankdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rmassbankdata.
shpc-registry automated BioContainers addition for bioconductor-rmassbankdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rmassbankdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rmassbankdata:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rmassbankdata/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rmassbankdata/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rmassbankdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmassbankdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmassbankdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rmassbankdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rmassbankdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rmassbankdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rmassbankdata

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