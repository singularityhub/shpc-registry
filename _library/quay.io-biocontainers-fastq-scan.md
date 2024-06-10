---
layout: container
name:  "quay.io/biocontainers/fastq-scan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-scan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-scan/container.yaml"
updated_at: "2024-06-10 03:06:51.895178"
latest: "1.0.1--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/fastq-scan"
aliases:
 - "fastq-scan"
 - "jq"
 - "onig-config"
versions:
 - "1.0.0--h9f5acd7_1"
 - "1.0.1--h9f5acd7_0"
 - "1.0.1--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for fastq-scan"
config: {"url": "https://biocontainers.pro/tools/fastq-scan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-scan", "latest": {"1.0.1--h4ac6f70_2": "sha256:679fdd3ffd61e54c2852221dfe9e9ed112c341e20514843ef40b337b11fd4969"}, "tags": {"1.0.0--h9f5acd7_1": "sha256:02ecc930d960f1e6861fa00afa4c143afa03ad6b98fc118aa118ee950cb5e27e", "1.0.1--h9f5acd7_0": "sha256:d20b2c80fff4cdebded1a7934aa857c880d2f3b7cb19d6c400ed667c250222ba", "1.0.1--h4ac6f70_2": "sha256:679fdd3ffd61e54c2852221dfe9e9ed112c341e20514843ef40b337b11fd4969"}, "docker": "quay.io/biocontainers/fastq-scan", "aliases": {"fastq-scan": "/usr/local/bin/fastq-scan", "jq": "/usr/local/bin/jq", "onig-config": "/usr/local/bin/onig-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-scan.
shpc-registry automated BioContainers addition for fastq-scan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-scan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-scan:1.0.1--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-scan/1.0.1--h4ac6f70_2
$ module help quay.io/biocontainers/fastq-scan/1.0.1--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-scan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-scan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-scan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-scan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-scan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-scan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-scan

```bash
$ singularity exec <container> /usr/local/bin/fastq-scan
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jq

```bash
$ singularity exec <container> /usr/local/bin/jq
$ podman run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onig-config

```bash
$ singularity exec <container> /usr/local/bin/onig-config
$ podman run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onig-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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