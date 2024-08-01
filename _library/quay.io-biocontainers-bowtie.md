---
layout: container
name:  "quay.io/biocontainers/bowtie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bowtie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bowtie/container.yaml"
updated_at: "2024-08-01 02:44:27.331406"
latest: "1.3.1--py310h4971c18_8"
container_url: "https://biocontainers.pro/tools/bowtie"
aliases:
 - "bowtie"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
 - "perl5.32.1"
versions:
 - "1.3.1--py36h769816f_3"
 - "1.3.1--py39h1a2fba0_7"
 - "1.3.1--py310h4971c18_8"
description: "shpc-registry automated BioContainers addition for bowtie"
config: {"url": "https://biocontainers.pro/tools/bowtie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bowtie", "latest": {"1.3.1--py310h4971c18_8": "sha256:f6d205b4457e3a75cb7ff9d4dd41d684ac60f4b1cb88a3c4384a144647944e93"}, "tags": {"1.3.1--py36h769816f_3": "sha256:ebfdf6379111f690154229e240b6d7e1b3556c99deb13abadee33c6b396c8373", "1.3.1--py39h1a2fba0_7": "sha256:10dc3387cddd49d8042864bf454d9101881d6b7eab4c1fdf54ad2343bd1819f7", "1.3.1--py310h4971c18_8": "sha256:f6d205b4457e3a75cb7ff9d4dd41d684ac60f4b1cb88a3c4384a144647944e93"}, "docker": "quay.io/biocontainers/bowtie", "aliases": {"bowtie": "/usr/local/bin/bowtie", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv", "perl5.32.1": "/usr/local/bin/perl5.32.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bowtie.
shpc-registry automated BioContainers addition for bowtie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bowtie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bowtie:1.3.1--py310h4971c18_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bowtie/1.3.1--py310h4971c18_8
$ module help quay.io/biocontainers/bowtie/1.3.1--py310h4971c18_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bowtie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bowtie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bowtie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bowtie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bowtie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bowtie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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