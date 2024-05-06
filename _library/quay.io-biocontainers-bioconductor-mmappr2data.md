---
layout: container
name:  "quay.io/biocontainers/bioconductor-mmappr2data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mmappr2data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mmappr2data/container.yaml"
updated_at: "2024-05-06 04:45:03.914551"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mmappr2data"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mmappr2data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mmappr2data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mmappr2data", "latest": {"1.16.0--r43hdfd78af_0": "sha256:2623b16a57365adddc1f0857498d65e63239dbe20971375a1cbce330268d5d61"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:58490534e96ddfc4cf46947c800843657754c1ae93c35ce1adbc948f45e4c30b", "1.12.0--r42hdfd78af_0": "sha256:5bdb8b96d44aa55cff768d98dd49a0730c5e1b254d76b5e1981ac66d5f870955", "1.14.0--r43hdfd78af_0": "sha256:26904bd79f5786d45460107acc006f59236c0930d17f2eb79bc97ce582e241bc", "1.16.0--r43hdfd78af_0": "sha256:2623b16a57365adddc1f0857498d65e63239dbe20971375a1cbce330268d5d61"}, "docker": "quay.io/biocontainers/bioconductor-mmappr2data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mmappr2data.
shpc-registry automated BioContainers addition for bioconductor-mmappr2data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mmappr2data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mmappr2data:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mmappr2data/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mmappr2data/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mmappr2data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmappr2data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmappr2data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mmappr2data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mmappr2data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mmappr2data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mmappr2data

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