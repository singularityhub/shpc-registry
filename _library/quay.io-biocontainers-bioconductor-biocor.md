---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocor/container.yaml"
updated_at: "2024-07-17 02:53:36.783480"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocor"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocor", "latest": {"1.26.0--r43hdfd78af_0": "sha256:4ca21b86e5fab6033c003f878eb42faa48f393b08d1074ec21d4c86c835f56a9"}, "tags": {"1.8.1--r36_0": "sha256:df76c7d8f0f90ace7f91f348fba75de4da813c137497a08a3cc66cac224e55ab", "1.22.0--r42hdfd78af_0": "sha256:1908dd95351cc1abbf495afce4b1fff1ee92c78d099ef48f6b05d1e1f0326b58", "1.18.0--r41hdfd78af_0": "sha256:c6880a4df7af4daeba67e672e5fb1fc82ce7fa57f8847282f85dbe1b431ce6c8", "1.16.0--r41hdfd78af_0": "sha256:382d6fcc81faa71fb77921ba6c5dc82a35188c8968fe2bb38272343fee2a42c3", "1.14.0--r40hdfd78af_1": "sha256:dc4d03adcff898f0bc8c19911ad8d359b6ab6b84572dbb8746b35cab4128371b", "1.12.0--r40_0": "sha256:427500bc8f6bef6ee029e86609be7b4e84ec2fd122a330422c0f79c64fae2b1a", "1.24.0--r43hdfd78af_0": "sha256:e554f55b390d814127cc01b4c4577021f03136008af2a13fbde5b3c1468f930c", "1.26.0--r43hdfd78af_0": "sha256:4ca21b86e5fab6033c003f878eb42faa48f393b08d1074ec21d4c86c835f56a9"}, "docker": "quay.io/biocontainers/bioconductor-biocor", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocor.
shpc-registry automated BioContainers addition for bioconductor-biocor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocor:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocor/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocor/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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