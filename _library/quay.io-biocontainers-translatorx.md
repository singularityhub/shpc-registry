---
layout: container
name:  "quay.io/biocontainers/translatorx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/translatorx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/translatorx/container.yaml"
updated_at: "2023-08-12 02:44:14.137818"
latest: "1.1--2"
container_url: "https://biocontainers.pro/tools/translatorx"
aliases:
 - "translatorx"
 - "translatorx_vLocal.pl"
 - "muscle"
 - "perl5.26.2"
 - "podselect"
versions:
 - "1.1--2"
description: "shpc-registry automated BioContainers addition for translatorx"
config: {"url": "https://biocontainers.pro/tools/translatorx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for translatorx", "latest": {"1.1--2": "sha256:8977d56d4a9bc0e47f9a4c35797e97f91975a8bfc0666346fc8a936a00863c19"}, "tags": {"1.1--2": "sha256:8977d56d4a9bc0e47f9a4c35797e97f91975a8bfc0666346fc8a936a00863c19"}, "docker": "quay.io/biocontainers/translatorx", "aliases": {"translatorx": "/usr/local/bin/translatorx", "translatorx_vLocal.pl": "/usr/local/bin/translatorx_vLocal.pl", "muscle": "/usr/local/bin/muscle", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/translatorx.
shpc-registry automated BioContainers addition for translatorx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/translatorx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/translatorx:1.1--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/translatorx/1.1--2
$ module help quay.io/biocontainers/translatorx/1.1--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### translatorx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### translatorx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### translatorx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### translatorx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### translatorx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### translatorx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### translatorx

```bash
$ singularity exec <container> /usr/local/bin/translatorx
$ podman run --it --rm --entrypoint /usr/local/bin/translatorx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translatorx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translatorx_vLocal.pl

```bash
$ singularity exec <container> /usr/local/bin/translatorx_vLocal.pl
$ podman run --it --rm --entrypoint /usr/local/bin/translatorx_vLocal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translatorx_vLocal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
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