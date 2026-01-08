---
layout: container
name:  "quay.io/biocontainers/bioconductor-synaptome.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-synaptome.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-synaptome.data/container.yaml"
updated_at: "2026-01-08 03:44:26.258067"
latest: "0.99.6--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-synaptome.data"

versions:
 - "0.99.3--r41hdfd78af_1"
 - "0.99.6--r42hdfd78af_0"
 - "0.99.6--r43hdfd78af_1"
 - "0.99.6--r43hdfd78af_2"
 - "0.99.6--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-synaptome.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-synaptome.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-synaptome.data", "latest": {"0.99.6--r44hdfd78af_3": "sha256:861dd6c16e5470cce9275cfa077237f01bf7a275b71afc1d5f287de64dc9ef71"}, "tags": {"0.99.3--r41hdfd78af_1": "sha256:1e00ed83147a4dda8fe9660e8592de2e38087a23d05d4c50bcc47fe8fe732b9a", "0.99.6--r42hdfd78af_0": "sha256:c882f2f2c2fa077d400ac6fefe5a9ad68aaacfc409ccc9ff115451d93abe99a8", "0.99.6--r43hdfd78af_1": "sha256:f34399b74124ff562ee29fce4e0cb6917ef4280cef4cdc28a42928fe6e0920b3", "0.99.6--r43hdfd78af_2": "sha256:209e24633cce4880700281cd742d3430eba587cad7fe530cb81e65e436269758", "0.99.6--r44hdfd78af_3": "sha256:861dd6c16e5470cce9275cfa077237f01bf7a275b71afc1d5f287de64dc9ef71"}, "docker": "quay.io/biocontainers/bioconductor-synaptome.data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-synaptome.data.
shpc-registry automated BioContainers addition for bioconductor-synaptome.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-synaptome.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-synaptome.data:0.99.6--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-synaptome.data/0.99.6--r44hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-synaptome.data/0.99.6--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-synaptome.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synaptome.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synaptome.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-synaptome.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-synaptome.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-synaptome.data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-synaptome.data

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