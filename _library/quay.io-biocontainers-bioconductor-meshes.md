---
layout: container
name:  "quay.io/biocontainers/bioconductor-meshes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meshes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meshes/container.yaml"
updated_at: "2024-07-11 03:32:35.157251"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meshes"
aliases:
 - "udunits2"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meshes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meshes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meshes", "latest": {"1.28.0--r43hdfd78af_0": "sha256:f610f420e806f6eb8618f370b62a5e8af253d53d423f1e03921a2a063278a496"}, "tags": {"1.8.0--r351_0": "sha256:4052fcdbf57a02a068208fc6bc09c5b44f4fe5e3c47986b785eb0907883ae2b9", "1.24.0--r42hdfd78af_0": "sha256:d1cc7e0425a67e4fb3af714996990c26f447902989dde9a78d320145c5ac3907", "1.20.0--r41hdfd78af_0": "sha256:d578e43b7454c97531c18891535af1efc69aaf3f825830427451ee0556397cd0", "1.18.0--r41hdfd78af_0": "sha256:2fa6e07adc4d4968f7653ae0a53de0d184c83a67600dff4b6ffcbf2aa8c94b01", "1.16.0--r40hdfd78af_1": "sha256:5cddcb07b9048ce982506addd2e91bb6210cc7c21c27525624699dd7bd94f432", "1.14.0--r40_0": "sha256:ace673c517d0db72c105be4a779ac83b99b4f5953b382e4b0f8ac33cd596bdee", "1.26.0--r43hdfd78af_0": "sha256:2b3c5de109f6cdbcf8f87fefd7841626db8a4286c0e5799405d9de51cc1190f1", "1.28.0--r43hdfd78af_0": "sha256:f610f420e806f6eb8618f370b62a5e8af253d53d423f1e03921a2a063278a496"}, "docker": "quay.io/biocontainers/bioconductor-meshes", "aliases": {"udunits2": "/usr/local/bin/udunits2", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meshes.
shpc-registry automated BioContainers addition for bioconductor-meshes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meshes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meshes:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meshes/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meshes/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meshes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meshes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meshes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meshes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meshes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meshes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### udunits2

```bash
$ singularity exec <container> /usr/local/bin/udunits2
$ podman run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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