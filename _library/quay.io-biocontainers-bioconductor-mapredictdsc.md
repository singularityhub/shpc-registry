---
layout: container
name:  "quay.io/biocontainers/bioconductor-mapredictdsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mapredictdsc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mapredictdsc/container.yaml"
updated_at: "2024-02-16 02:53:32.482377"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mapredictdsc"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mapredictdsc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mapredictdsc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mapredictdsc", "latest": {"1.40.0--r43hdfd78af_0": "sha256:964fca777c9de7b564fbe334b06ae2bb15cbedc2c8eb1b03322689089c8f8b1d"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:a13c01f8c65cb82cabd49d5bb61f3caaa22d2cd668888688e81b9ab9819b5c4e", "1.36.0--r42hdfd78af_0": "sha256:4fffd69b9b5640cfecbf0ab857c3045928d7a66310afcc8a137ddbb8db60d26a", "1.38.0--r43hdfd78af_0": "sha256:772cc68d2eb91ab93a3735d4c73e8b9e3f253eb3a1c0d2f2839c5e8f41c386f0", "1.40.0--r43hdfd78af_0": "sha256:964fca777c9de7b564fbe334b06ae2bb15cbedc2c8eb1b03322689089c8f8b1d"}, "docker": "quay.io/biocontainers/bioconductor-mapredictdsc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mapredictdsc.
shpc-registry automated BioContainers addition for bioconductor-mapredictdsc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mapredictdsc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mapredictdsc:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mapredictdsc/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mapredictdsc/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mapredictdsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapredictdsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapredictdsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mapredictdsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mapredictdsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mapredictdsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mapredictdsc

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