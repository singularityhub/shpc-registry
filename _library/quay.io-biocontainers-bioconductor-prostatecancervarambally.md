---
layout: container
name:  "quay.io/biocontainers/bioconductor-prostatecancervarambally"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prostatecancervarambally/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prostatecancervarambally/container.yaml"
updated_at: "2026-01-09 04:21:05.718318"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prostatecancervarambally"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prostatecancervarambally"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prostatecancervarambally", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prostatecancervarambally", "latest": {"1.34.0--r44hdfd78af_0": "sha256:4d1866d195f7779a3796d4859633a48b1a5c01fc4c3b96d303b361ce7b48fcca"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:cf62f25a049f839bb6e5720445d3d1676b94d8ea39c63c488678978f4c784b7f", "1.26.0--r42hdfd78af_0": "sha256:87a534a2c6fd75b256c074e316ad73f63732fdf63caa5a33da826671612a49f0", "1.28.0--r43hdfd78af_0": "sha256:689963344fc7460a9e2c8ba6387262e6bfd55e2ba003ef5e75f00b2852163986", "1.30.0--r43hdfd78af_0": "sha256:6fc20767b30c91790d44eea57f624b8c60fc827ba3d88e4fa591d8d7419dd087", "1.34.0--r44hdfd78af_0": "sha256:4d1866d195f7779a3796d4859633a48b1a5c01fc4c3b96d303b361ce7b48fcca"}, "docker": "quay.io/biocontainers/bioconductor-prostatecancervarambally"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prostatecancervarambally.
shpc-registry automated BioContainers addition for bioconductor-prostatecancervarambally
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancervarambally
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancervarambally:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prostatecancervarambally/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-prostatecancervarambally/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prostatecancervarambally-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancervarambally-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancervarambally-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prostatecancervarambally-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prostatecancervarambally-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prostatecancervarambally-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-prostatecancervarambally

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