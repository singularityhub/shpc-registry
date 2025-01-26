---
layout: container
name:  "quay.io/biocontainers/sailfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sailfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sailfish/container.yaml"
updated_at: "2025-01-26 03:05:19.300527"
latest: "0.10.1--pl5321hf742e08_6"
container_url: "https://biocontainers.pro/tools/sailfish"
aliases:
 - "sailfish"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.10.1--pl5321hf742e08_6"
description: "shpc-registry automated BioContainers addition for sailfish"
config: {"url": "https://biocontainers.pro/tools/sailfish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sailfish", "latest": {"0.10.1--pl5321hf742e08_6": "sha256:0d00607f18734d639fe66519229424ce0d126cb85b2f5a2db3b3eb6f0c60b854"}, "tags": {"0.10.1--pl5321hf742e08_6": "sha256:0d00607f18734d639fe66519229424ce0d126cb85b2f5a2db3b3eb6f0c60b854"}, "docker": "quay.io/biocontainers/sailfish", "aliases": {"sailfish": "/usr/local/bin/sailfish", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sailfish.
shpc-registry automated BioContainers addition for sailfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sailfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sailfish:0.10.1--pl5321hf742e08_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sailfish/0.10.1--pl5321hf742e08_6
$ module help quay.io/biocontainers/sailfish/0.10.1--pl5321hf742e08_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sailfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sailfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sailfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sailfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sailfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sailfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sailfish

```bash
$ singularity exec <container> /usr/local/bin/sailfish
$ podman run --it --rm --entrypoint /usr/local/bin/sailfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sailfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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