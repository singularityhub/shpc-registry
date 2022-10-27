---
layout: container
name:  "quay.io/biocontainers/orthofinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orthofinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/orthofinder/container.yaml"
updated_at: "2022-10-27 00:59:59.986972"
latest: "2.5.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/orthofinder"
aliases:
 - "convert_orthofinder_tree_ids.py"
 - "make_ultrametric.py"
 - "orthofinder"
 - "primary_transcript.py"
 - "raxml-ng"
 - "raxml-ng-mpi"
versions:
 - "2.5.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for orthofinder"
config: {"url": "https://biocontainers.pro/tools/orthofinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for orthofinder", "latest": {"2.5.4--hdfd78af_0": "sha256:d71c5b9c9661e3ca7a612f9109a9f57627a2edecd418e8472608c3c0ef05ef5c"}, "tags": {"2.5.4--hdfd78af_0": "sha256:d71c5b9c9661e3ca7a612f9109a9f57627a2edecd418e8472608c3c0ef05ef5c"}, "docker": "quay.io/biocontainers/orthofinder", "aliases": {"convert_orthofinder_tree_ids.py": "/usr/local/bin/convert_orthofinder_tree_ids.py", "make_ultrametric.py": "/usr/local/bin/make_ultrametric.py", "orthofinder": "/usr/local/bin/orthofinder", "primary_transcript.py": "/usr/local/bin/primary_transcript.py", "raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orthofinder.
shpc-registry automated BioContainers addition for orthofinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orthofinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orthofinder:2.5.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orthofinder/2.5.4--hdfd78af_0
$ module help quay.io/biocontainers/orthofinder/2.5.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orthofinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orthofinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orthofinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orthofinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orthofinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orthofinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_orthofinder_tree_ids.py

```bash
$ singularity exec <container> /usr/local/bin/convert_orthofinder_tree_ids.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_orthofinder_tree_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_orthofinder_tree_ids.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_ultrametric.py

```bash
$ singularity exec <container> /usr/local/bin/make_ultrametric.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_ultrametric.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_ultrametric.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orthofinder

```bash
$ singularity exec <container> /usr/local/bin/orthofinder
$ podman run --it --rm --entrypoint /usr/local/bin/orthofinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orthofinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primary_transcript.py

```bash
$ singularity exec <container> /usr/local/bin/primary_transcript.py
$ podman run --it --rm --entrypoint /usr/local/bin/primary_transcript.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primary_transcript.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
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