---
layout: container
name:  "quay.io/biocontainers/bioconductor-prostatecancercamcap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prostatecancercamcap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prostatecancercamcap/container.yaml"
updated_at: "2024-08-24 02:46:50.490140"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prostatecancercamcap"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prostatecancercamcap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prostatecancercamcap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prostatecancercamcap", "latest": {"1.30.0--r43hdfd78af_0": "sha256:9b6208c4a80e0f64c6d7fdd65c49ba6cb62ba5a31db012904ba0f8d10ba6b6eb"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:01a85a0908c7117fccd52023cf1e78e18e180637dfb877d11a83673a3c8061e9", "1.26.0--r42hdfd78af_0": "sha256:1715e26a4aaa66a56516489901f678fffe8e0f6bc9a09d32e1b44233b5b8ab4e", "1.28.0--r43hdfd78af_0": "sha256:378722ecde7740f5e2639e36a63ae8b3faa37f7245bbb08fa516184c7302abb8", "1.30.0--r43hdfd78af_0": "sha256:9b6208c4a80e0f64c6d7fdd65c49ba6cb62ba5a31db012904ba0f8d10ba6b6eb"}, "docker": "quay.io/biocontainers/bioconductor-prostatecancercamcap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prostatecancercamcap.
shpc-registry automated BioContainers addition for bioconductor-prostatecancercamcap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancercamcap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancercamcap:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prostatecancercamcap/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-prostatecancercamcap/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prostatecancercamcap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancercamcap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancercamcap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prostatecancercamcap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prostatecancercamcap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prostatecancercamcap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-prostatecancercamcap

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