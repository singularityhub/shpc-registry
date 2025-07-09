---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneoverlap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneoverlap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneoverlap/container.yaml"
updated_at: "2025-07-09 03:43:27.134082"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneoverlap"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneoverlap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneoverlap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneoverlap", "latest": {"1.42.0--r44hdfd78af_0": "sha256:33abf6a1fe9d0bf103c005b26caf8da312f21f9c7087eb97116b962c3fd10741"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:8d877a09ba1e49f8d4a3a2c9529feeb7e4179ecf8b91a42e628a1729ab87041b", "1.34.0--r42hdfd78af_0": "sha256:862c37e9bc4a0b4f304a025d0e23de716705b37ca5d7cfed20bdf8640c1ba22b", "1.36.0--r43hdfd78af_0": "sha256:224ffab58dd31c1d00f3dd1dc6bf5b794ed24a8643f9d9eb925e995577d2eba1", "1.38.0--r43hdfd78af_0": "sha256:4dcf12eabf4785868589ecf4aa3db5c2c5b7af47ddffff2c86def030eb5b7a62", "1.42.0--r44hdfd78af_0": "sha256:33abf6a1fe9d0bf103c005b26caf8da312f21f9c7087eb97116b962c3fd10741"}, "docker": "quay.io/biocontainers/bioconductor-geneoverlap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneoverlap.
shpc-registry automated BioContainers addition for bioconductor-geneoverlap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneoverlap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneoverlap:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneoverlap/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneoverlap/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneoverlap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneoverlap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneoverlap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneoverlap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneoverlap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneoverlap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geneoverlap

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