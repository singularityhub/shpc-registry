---
layout: container
name:  "quay.io/biocontainers/ghmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ghmm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ghmm/container.yaml"
updated_at: "2022-10-27 00:19:04.379009"
latest: "0.9--py27pl5321he3645e8_2"
container_url: "https://biocontainers.pro/tools/ghmm"
aliases:
 - "ghmm-config"
 - "probdist"
 - "scluster"
 - "smix_hmm"
versions:
 - "0.9--py27pl5321he3645e8_2"
description: "shpc-registry automated BioContainers addition for ghmm"
config: {"url": "https://biocontainers.pro/tools/ghmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ghmm", "latest": {"0.9--py27pl5321he3645e8_2": "sha256:9ec3a02057e24d11e36f53fdcca94e7f0f1526efc367e66b6c17742c88c12e6c"}, "tags": {"0.9--py27pl5321he3645e8_2": "sha256:9ec3a02057e24d11e36f53fdcca94e7f0f1526efc367e66b6c17742c88c12e6c"}, "docker": "quay.io/biocontainers/ghmm", "aliases": {"ghmm-config": "/usr/local/bin/ghmm-config", "probdist": "/usr/local/bin/probdist", "scluster": "/usr/local/bin/scluster", "smix_hmm": "/usr/local/bin/smix_hmm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ghmm.
shpc-registry automated BioContainers addition for ghmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ghmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ghmm:0.9--py27pl5321he3645e8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ghmm/0.9--py27pl5321he3645e8_2
$ module help quay.io/biocontainers/ghmm/0.9--py27pl5321he3645e8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ghmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ghmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ghmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ghmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ghmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ghmm-config

```bash
$ singularity exec <container> /usr/local/bin/ghmm-config
$ podman run --it --rm --entrypoint /usr/local/bin/ghmm-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghmm-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### probdist

```bash
$ singularity exec <container> /usr/local/bin/probdist
$ podman run --it --rm --entrypoint /usr/local/bin/probdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scluster

```bash
$ singularity exec <container> /usr/local/bin/scluster
$ podman run --it --rm --entrypoint /usr/local/bin/scluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smix_hmm

```bash
$ singularity exec <container> /usr/local/bin/smix_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/smix_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smix_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
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