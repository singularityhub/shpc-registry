---
layout: container
name:  "quay.io/biocontainers/migmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/migmap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/migmap/container.yaml"
updated_at: "2022-10-27 00:47:33.400221"
latest: "1.0.3--hdfd78af_6"
container_url: "https://biocontainers.pro/tools/migmap"
aliases:
 - "edit_imgt_file.pl"
 - "igblastn"
 - "igblastp"
 - "migmap"
versions:
 - "1.0.3--hdfd78af_6"
description: "shpc-registry automated BioContainers addition for migmap"
config: {"url": "https://biocontainers.pro/tools/migmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for migmap", "latest": {"1.0.3--hdfd78af_6": "sha256:cef67e1d5a609056408a4e21a3e7c3db79360ac9815ef272ab53c7cdbe8b637e"}, "tags": {"1.0.3--hdfd78af_6": "sha256:cef67e1d5a609056408a4e21a3e7c3db79360ac9815ef272ab53c7cdbe8b637e"}, "docker": "quay.io/biocontainers/migmap", "aliases": {"edit_imgt_file.pl": "/usr/local/bin/edit_imgt_file.pl", "igblastn": "/usr/local/bin/igblastn", "igblastp": "/usr/local/bin/igblastp", "migmap": "/usr/local/bin/migmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/migmap.
shpc-registry automated BioContainers addition for migmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/migmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/migmap:1.0.3--hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/migmap/1.0.3--hdfd78af_6
$ module help quay.io/biocontainers/migmap/1.0.3--hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### migmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### migmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### migmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### migmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### migmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### migmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### edit_imgt_file.pl

```bash
$ singularity exec <container> /usr/local/bin/edit_imgt_file.pl
$ podman run --it --rm --entrypoint /usr/local/bin/edit_imgt_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edit_imgt_file.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igblastn

```bash
$ singularity exec <container> /usr/local/bin/igblastn
$ podman run --it --rm --entrypoint /usr/local/bin/igblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igblastp

```bash
$ singularity exec <container> /usr/local/bin/igblastp
$ podman run --it --rm --entrypoint /usr/local/bin/igblastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igblastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### migmap

```bash
$ singularity exec <container> /usr/local/bin/migmap
$ podman run --it --rm --entrypoint /usr/local/bin/migmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/migmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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