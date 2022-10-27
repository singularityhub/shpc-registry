---
layout: container
name:  "quay.io/biocontainers/r-merge-kallisto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-merge-kallisto/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-merge-kallisto/container.yaml"
updated_at: "2022-10-27 01:09:39.605634"
latest: "0.6--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-merge-kallisto"
aliases:
 - "merge_kallisto.R"
versions:
 - "0.6--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-merge-kallisto"
config: {"url": "https://biocontainers.pro/tools/r-merge-kallisto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-merge-kallisto", "latest": {"0.6--hdfd78af_1": "sha256:3b4522235d25f421df8b5174f2f7ac3666b3a850aff808a54c2f90de521b8532"}, "tags": {"0.6--hdfd78af_1": "sha256:3b4522235d25f421df8b5174f2f7ac3666b3a850aff808a54c2f90de521b8532"}, "docker": "quay.io/biocontainers/r-merge-kallisto", "aliases": {"merge_kallisto.R": "/usr/local/bin/merge_kallisto.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-merge-kallisto.
shpc-registry automated BioContainers addition for r-merge-kallisto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-merge-kallisto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-merge-kallisto:0.6--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-merge-kallisto/0.6--hdfd78af_1
$ module help quay.io/biocontainers/r-merge-kallisto/0.6--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-merge-kallisto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-merge-kallisto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-merge-kallisto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-merge-kallisto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-merge-kallisto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-merge-kallisto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### merge_kallisto.R

```bash
$ singularity exec <container> /usr/local/bin/merge_kallisto.R
$ podman run --it --rm --entrypoint /usr/local/bin/merge_kallisto.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_kallisto.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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