---
layout: container
name:  "quay.io/biocontainers/bioconductor-crisprseekplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-crisprseekplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-crisprseekplus/container.yaml"
updated_at: "2024-07-17 03:23:17.415888"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-crisprseekplus"
aliases:
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
description: "shpc-registry automated BioContainers addition for bioconductor-crisprseekplus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-crisprseekplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-crisprseekplus", "latest": {"1.26.0--r43hdfd78af_0": "sha256:422aa87ba6895072f18e2cd0bb04ca74d911dae1ad59553fefd941ac9c082d9e"}, "tags": {"1.8.0--r351_0": "sha256:a5cd90ae7a761d760e84c07ee07121bb42e1e90e507ad17e4b2c1fb905a5db96", "1.24.0--r42hdfd78af_0": "sha256:d4a227824e4398b492888684a1e6bdfd2162b10350abca1b64a6fd1e30d135c1", "1.20.0--r41hdfd78af_0": "sha256:477b1be38964e3941a22579ac1bef2cc2dbb4768d9ac0a73a623214375c00dd4", "1.18.0--r41hdfd78af_0": "sha256:a564d606ffd418a76d655f1412e5ee1c4d36243a813a04950212e3efa6bca13c", "1.16.0--r40hdfd78af_1": "sha256:14e5ed83b549e76ccb4ee34258901bd8610b62bb5be965b253369c6a0d69d746", "1.14.0--r40_0": "sha256:c98a9657a39ce5d882a6263c9175808c4c23dd3bf2086d54dbfb2fa17f0633a0", "1.26.0--r43hdfd78af_0": "sha256:422aa87ba6895072f18e2cd0bb04ca74d911dae1ad59553fefd941ac9c082d9e"}, "docker": "quay.io/biocontainers/bioconductor-crisprseekplus", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-crisprseekplus.
shpc-registry automated BioContainers addition for bioconductor-crisprseekplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-crisprseekplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-crisprseekplus:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-crisprseekplus/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-crisprseekplus/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-crisprseekplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crisprseekplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crisprseekplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-crisprseekplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-crisprseekplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-crisprseekplus-inspect-deffile:

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