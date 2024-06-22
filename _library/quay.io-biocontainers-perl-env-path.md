---
layout: container
name:  "quay.io/biocontainers/perl-env-path"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-env-path/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-env-path/container.yaml"
updated_at: "2024-06-22 02:46:58.044897"
latest: "0.19--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/perl-env-path"
aliases:
 - "envpath"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.19--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for perl-env-path"
config: {"url": "https://biocontainers.pro/tools/perl-env-path", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-env-path", "latest": {"0.19--pl5321hdfd78af_3": "sha256:59a2ccb0dab71fe396ab3ed3e50a1b8123fac6eb81e9b7f50df05b8472790418"}, "tags": {"0.19--pl5321hdfd78af_3": "sha256:59a2ccb0dab71fe396ab3ed3e50a1b8123fac6eb81e9b7f50df05b8472790418"}, "docker": "quay.io/biocontainers/perl-env-path", "aliases": {"envpath": "/usr/local/bin/envpath", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-env-path.
shpc-registry automated BioContainers addition for perl-env-path
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-env-path
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-env-path:0.19--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-env-path/0.19--pl5321hdfd78af_3
$ module help quay.io/biocontainers/perl-env-path/0.19--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-env-path-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-env-path-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-env-path-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-env-path-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-env-path-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-env-path-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### envpath

```bash
$ singularity exec <container> /usr/local/bin/envpath
$ podman run --it --rm --entrypoint /usr/local/bin/envpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/envpath   -v ${PWD} -w ${PWD} <container> -c " $@"
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