---
layout: container
name:  "quay.io/biocontainers/bioconductor-dresscheck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dresscheck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dresscheck/container.yaml"
updated_at: "2024-09-08 02:56:25.481916"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dresscheck"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.36.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dresscheck"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dresscheck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dresscheck", "latest": {"0.40.0--r43hdfd78af_0": "sha256:309226696f6e5128a6cefae1ca44870c5d060f42f1615419ebddc6bd9237e047"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:a6b60f491207265ca64c2c1006cc982dcb96824808c3d93bf8b8b05f6b30680a", "0.36.0--r42hdfd78af_0": "sha256:1db4d8702861c425f96fec761f493e63837aaa9fee453c1506e966ca9e7aa5ee", "0.38.0--r43hdfd78af_0": "sha256:abe1d6e02702f0f24fe3937a0db2ec3251e1322dc2c83d567b27c2e51042c719", "0.40.0--r43hdfd78af_0": "sha256:309226696f6e5128a6cefae1ca44870c5d060f42f1615419ebddc6bd9237e047"}, "docker": "quay.io/biocontainers/bioconductor-dresscheck"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dresscheck.
shpc-registry automated BioContainers addition for bioconductor-dresscheck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dresscheck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dresscheck:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dresscheck/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dresscheck/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dresscheck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dresscheck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dresscheck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dresscheck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dresscheck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dresscheck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dresscheck

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