---
layout: container
name:  "quay.io/biocontainers/bioconductor-prodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prodata/container.yaml"
updated_at: "2024-12-01 03:43:10.889390"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prodata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prodata", "latest": {"1.40.0--r43hdfd78af_0": "sha256:1c83df49ba9d0f02b5fd4ccb1e2a1746a07d65b2c7024bcd1a92d9a2d63aa18a"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:133c0b0cf00fc69c7074f79246e1ff21804d404275b3e5b39a6be8a905f089d5", "1.36.0--r42hdfd78af_0": "sha256:ce94a2a5909fc1ec3f1573a822d3a25608e32e36c7e33f362fe8fc927171b4dc", "1.38.0--r43hdfd78af_0": "sha256:6cded9a941dff5d99d41c2cd8158b50348f7ae7cc827fed5f6a2681c17f46f1a", "1.40.0--r43hdfd78af_0": "sha256:1c83df49ba9d0f02b5fd4ccb1e2a1746a07d65b2c7024bcd1a92d9a2d63aa18a"}, "docker": "quay.io/biocontainers/bioconductor-prodata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prodata.
shpc-registry automated BioContainers addition for bioconductor-prodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prodata:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prodata/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-prodata/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prodata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-prodata

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