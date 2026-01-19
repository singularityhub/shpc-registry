---
layout: container
name:  "quay.io/biocontainers/bioconductor-ctcf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ctcf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ctcf/container.yaml"
updated_at: "2026-01-19 04:35:37.928603"
latest: "0.99.11--r44hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-ctcf"

versions:
 - "0.99.4--r41hdfd78af_1"
 - "0.99.9--r42hdfd78af_0"
 - "0.99.11--r43hdfd78af_0"
 - "0.99.11--r43hdfd78af_1"
 - "0.99.11--r44hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-ctcf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ctcf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ctcf", "latest": {"0.99.11--r44hdfd78af_2": "sha256:74e0446c21259bd9e610b4a7978702f98320256a2b429a822a13da558783d6fb"}, "tags": {"0.99.4--r41hdfd78af_1": "sha256:244a8c5eefdf79c541aa02e9a94d7db57cbf7f7b89b5d0485fe86cfeb960fc9e", "0.99.9--r42hdfd78af_0": "sha256:90eedf5fbf659a3da16fcb06bb07db1a0374b8e23010b7bfca77789d6275a31f", "0.99.11--r43hdfd78af_0": "sha256:a740ee4609677e8bdf0b60c22bffd7c4ac905448b97cf2c157a13b4f454bdb76", "0.99.11--r43hdfd78af_1": "sha256:3cba5642ebb7906fccd23ab2516846e7306da6406e2dcffd1313cab07f362477", "0.99.11--r44hdfd78af_2": "sha256:74e0446c21259bd9e610b4a7978702f98320256a2b429a822a13da558783d6fb"}, "docker": "quay.io/biocontainers/bioconductor-ctcf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ctcf.
shpc-registry automated BioContainers addition for bioconductor-ctcf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ctcf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ctcf:0.99.11--r44hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ctcf/0.99.11--r44hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-ctcf/0.99.11--r44hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ctcf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctcf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctcf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ctcf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ctcf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ctcf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ctcf

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