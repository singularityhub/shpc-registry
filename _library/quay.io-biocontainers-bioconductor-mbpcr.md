---
layout: container
name:  "quay.io/biocontainers/bioconductor-mbpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mbpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mbpcr/container.yaml"
updated_at: "2024-07-29 17:04:35.825699"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mbpcr"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mbpcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mbpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mbpcr", "latest": {"1.56.0--r43hdfd78af_0": "sha256:fcffd30e77fc977af20d9ec059f0ee464612189c45bc198bad8a6f6fb85b8c2e"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:fb2eaef6d16ded1fdb9d8a80b6b9c279efe1c8480355756402f77ee359d19ab4", "1.52.0--r42hdfd78af_0": "sha256:838178f14b0c6d18382a84f30e0a864ad932aab14a373697d7bd582318384e93", "1.54.0--r43hdfd78af_0": "sha256:aba201af22704bc9010969867bb74648acb704cb016ce4766dd03f25ff87a996", "1.56.0--r43hdfd78af_0": "sha256:fcffd30e77fc977af20d9ec059f0ee464612189c45bc198bad8a6f6fb85b8c2e"}, "docker": "quay.io/biocontainers/bioconductor-mbpcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mbpcr.
shpc-registry automated BioContainers addition for bioconductor-mbpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mbpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mbpcr:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mbpcr/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mbpcr/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mbpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mbpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mbpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mbpcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mbpcr

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