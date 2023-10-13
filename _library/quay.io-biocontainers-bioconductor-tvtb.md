---
layout: container
name:  "quay.io/biocontainers/bioconductor-tvtb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tvtb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tvtb/container.yaml"
updated_at: "2023-10-13 03:09:57.601994"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tvtb"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tvtb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tvtb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tvtb", "latest": {"1.26.0--r43hdfd78af_0": "sha256:3832472c58cf2fb646e285bd00a9c7c7ef6d791773b1bf016d4176e92c0e98b3"}, "tags": {"1.8.0--r351_0": "sha256:5b06f2bbb52cafe3dcfef8eba452f22918409991e1264cb26da186c7434e2329", "1.20.0--r41hdfd78af_0": "sha256:aa4cc522e5b486bfbfee7780982ee857dade5dd437dba18486aa13e3e77091fa", "1.18.0--r41hdfd78af_0": "sha256:ff98f099c4dab74a2fa21d3b5d704d8d7f91ce10021eb179c49fef0ad7fa4941", "1.16.0--r40hdfd78af_1": "sha256:18bad05f19ca57403ef17b00f749d0462f3e71487236a64bbf538bfe9110e524", "1.14.0--r40_0": "sha256:0adb3afc38a626a203f18770ea81bd556b002f390f05f081f9d5acf35be95b39", "1.12.0--r36_0": "sha256:be17f1c2211c9ee9226be1267a0cbb74fc53bd88c59395c251f1d662e26f687f", "1.26.0--r43hdfd78af_0": "sha256:3832472c58cf2fb646e285bd00a9c7c7ef6d791773b1bf016d4176e92c0e98b3"}, "docker": "quay.io/biocontainers/bioconductor-tvtb", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tvtb.
shpc-registry automated BioContainers addition for bioconductor-tvtb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tvtb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tvtb:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tvtb/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tvtb/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tvtb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tvtb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tvtb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tvtb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tvtb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tvtb-inspect-deffile:

```bash
$ singularity inspect -d <container>
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