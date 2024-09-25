---
layout: container
name:  "quay.io/biocontainers/rcorrector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rcorrector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rcorrector/container.yaml"
updated_at: "2024-09-25 03:09:51.871013"
latest: "1.0.7--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/rcorrector"
aliases:
 - "rcorrector"
 - "run_rcorrector.pl"
 - "jellyfish"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.5--h5b5514e_0"
 - "1.0.6--h43eeafb_0"
 - "1.0.7--h43eeafb_0"
description: "shpc-registry automated BioContainers addition for rcorrector"
config: {"url": "https://biocontainers.pro/tools/rcorrector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rcorrector", "latest": {"1.0.7--h43eeafb_0": "sha256:69baee338c5f676f9158c7c6a42144f4da22457083ab62b79d2b5f5edfbb558f"}, "tags": {"1.0.5--h5b5514e_0": "sha256:24a6e414ec511b813b45c63592cdbe60b6fc77f51ac5e16ee86d1712c902a96b", "1.0.6--h43eeafb_0": "sha256:a5cdaa876192b97f5f12ee1d50eb32da96e1700bce58f053a6c6067f7c88639a", "1.0.7--h43eeafb_0": "sha256:69baee338c5f676f9158c7c6a42144f4da22457083ab62b79d2b5f5edfbb558f"}, "docker": "quay.io/biocontainers/rcorrector", "aliases": {"rcorrector": "/usr/local/bin/rcorrector", "run_rcorrector.pl": "/usr/local/bin/run_rcorrector.pl", "jellyfish": "/usr/local/bin/jellyfish", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rcorrector.
shpc-registry automated BioContainers addition for rcorrector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rcorrector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rcorrector:1.0.7--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rcorrector/1.0.7--h43eeafb_0
$ module help quay.io/biocontainers/rcorrector/1.0.7--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rcorrector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rcorrector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rcorrector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rcorrector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rcorrector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rcorrector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rcorrector

```bash
$ singularity exec <container> /usr/local/bin/rcorrector
$ podman run --it --rm --entrypoint /usr/local/bin/rcorrector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcorrector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_rcorrector.pl

```bash
$ singularity exec <container> /usr/local/bin/run_rcorrector.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_rcorrector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_rcorrector.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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