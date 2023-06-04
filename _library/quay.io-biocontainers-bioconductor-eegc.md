---
layout: container
name:  "quay.io/biocontainers/bioconductor-eegc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eegc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eegc/container.yaml"
updated_at: "2023-06-04 03:24:11.339587"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eegc"
aliases:
 - "udunits2"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-eegc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eegc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eegc", "latest": {"1.24.0--r42hdfd78af_0": "sha256:32b6efbe36f751fa0eb64271549340ae5491c66762830256599767b97a681ad7"}, "tags": {"1.8.1--r351_0": "sha256:ad37d47986fa924558c8f9d74186e5908664984a7fdcb521dfa2f0c1feddad54", "1.24.0--r42hdfd78af_0": "sha256:32b6efbe36f751fa0eb64271549340ae5491c66762830256599767b97a681ad7", "1.20.0--r41hdfd78af_0": "sha256:55cc179181fd31e92bd1d5e6d2de36da4d272ea2581efee57e7a73a4c1a47391", "1.18.0--r41hdfd78af_0": "sha256:e6a57c2c422223a193c3c002115bf8838368f2d4210628a2e9d7659570b77d71", "1.16.0--r40hdfd78af_1": "sha256:db23a04893d003a5e243f5adf72d763edc858614b93463132766460d62e254ac", "1.14.0--r40_0": "sha256:5d0fb48d1db3d6f39bb61c8d62ab5001e8cb501970eefa195ca4534200a73f2a"}, "docker": "quay.io/biocontainers/bioconductor-eegc", "aliases": {"udunits2": "/usr/local/bin/udunits2", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eegc.
shpc-registry automated BioContainers addition for bioconductor-eegc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eegc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eegc:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eegc/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-eegc/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eegc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eegc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eegc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eegc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eegc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eegc-inspect-deffile:

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