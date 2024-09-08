---
layout: container
name:  "quay.io/biocontainers/bioconductor-anaquin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anaquin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anaquin/container.yaml"
updated_at: "2024-09-08 03:19:35.067028"
latest: "2.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anaquin"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.22.0--r42hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.0--r40_0"
 - "2.24.0--r43hdfd78af_0"
 - "2.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-anaquin"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anaquin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anaquin", "latest": {"2.26.0--r43hdfd78af_0": "sha256:fe778a10c26d0f45020141a2a0c041855c6f83edf17678c7729f76afdc8b2acd"}, "tags": {"2.8.0--r36_1": "sha256:cb64a8f0e4d7a3dde52545e33384e8623caf3cc1c31a386d51adb5c800386319", "2.22.0--r42hdfd78af_0": "sha256:80778c8929adfe2f199493567ba05e593bbd03fedbf90b2176004d1de0af31b9", "2.18.0--r41hdfd78af_0": "sha256:d6df2ad1e024106ac60d00614db66eec1c7d4c02a82770eb1ce92b6e7394a3d5", "2.16.0--r41hdfd78af_0": "sha256:ec4a88cfceb04bf78d4fb22c144fc093d8fde4d79cbb89dde203a1589eb17520", "2.14.0--r40hdfd78af_1": "sha256:92dbf3358d5a1ab7c96314ecee6b2228d5fe1b0b56bca9c5a51812dbbd8e8a87", "2.12.0--r40_0": "sha256:2c659f6ac36fd0f4c92972ba3dbccb5828751a3661dd55ea6107c23a98503e04", "2.24.0--r43hdfd78af_0": "sha256:bab9f71539929031dadc54956038a07bb578a7b037c1f03600b9decc95309af5", "2.26.0--r43hdfd78af_0": "sha256:fe778a10c26d0f45020141a2a0c041855c6f83edf17678c7729f76afdc8b2acd"}, "docker": "quay.io/biocontainers/bioconductor-anaquin", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anaquin.
shpc-registry automated BioContainers addition for bioconductor-anaquin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anaquin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anaquin:2.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anaquin/2.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anaquin/2.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anaquin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anaquin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anaquin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anaquin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anaquin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anaquin-inspect-deffile:

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