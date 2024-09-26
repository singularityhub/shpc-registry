---
layout: container
name:  "quay.io/biocontainers/seq2c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seq2c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seq2c/container.yaml"
updated_at: "2024-09-26 10:32:44.043861"
latest: "2019.05.30--pl526_0"
container_url: "https://biocontainers.pro/tools/seq2c"
aliases:
 - "cov2lr.pl"
 - "lr2gene.pl"
 - "seq2cov.pl"
 - "perl5.26.2"
 - "podselect"
versions:
 - "2019.05.30--pl526_0"
description: "shpc-registry automated BioContainers addition for seq2c"
config: {"url": "https://biocontainers.pro/tools/seq2c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seq2c", "latest": {"2019.05.30--pl526_0": "sha256:b6af254e7b6caf197e5cdaf3f383fd7fd7d0a06023f07fe058acfeb3198732eb"}, "tags": {"2019.05.30--pl526_0": "sha256:b6af254e7b6caf197e5cdaf3f383fd7fd7d0a06023f07fe058acfeb3198732eb"}, "docker": "quay.io/biocontainers/seq2c", "aliases": {"cov2lr.pl": "/usr/local/bin/cov2lr.pl", "lr2gene.pl": "/usr/local/bin/lr2gene.pl", "seq2cov.pl": "/usr/local/bin/seq2cov.pl", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seq2c.
shpc-registry automated BioContainers addition for seq2c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seq2c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seq2c:2019.05.30--pl526_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seq2c/2019.05.30--pl526_0
$ module help quay.io/biocontainers/seq2c/2019.05.30--pl526_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seq2c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seq2c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seq2c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seq2c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seq2c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seq2c-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cov2lr.pl

```bash
$ singularity exec <container> /usr/local/bin/cov2lr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cov2lr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cov2lr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lr2gene.pl

```bash
$ singularity exec <container> /usr/local/bin/lr2gene.pl
$ podman run --it --rm --entrypoint /usr/local/bin/lr2gene.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lr2gene.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq2cov.pl

```bash
$ singularity exec <container> /usr/local/bin/seq2cov.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq2cov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq2cov.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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