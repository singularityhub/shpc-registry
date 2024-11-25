---
layout: container
name:  "quay.io/biocontainers/unitig-caller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unitig-caller/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unitig-caller/container.yaml"
updated_at: "2024-11-25 03:16:51.682747"
latest: "1.3.0--py311h6ecfb3b_4"
container_url: "https://biocontainers.pro/tools/unitig-caller"
aliases:
 - "Bifrost"
 - "unitig-caller"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.3.0--py39h307a098_0"
 - "1.3.0--py37h2c368fa_1"
 - "1.3.0--py310ha320341_2"
 - "1.3.0--py310ha320341_3"
 - "1.3.0--py39h4ebf491_3"
 - "1.3.0--py311h6ecfb3b_4"
description: "shpc-registry automated BioContainers addition for unitig-caller"
config: {"url": "https://biocontainers.pro/tools/unitig-caller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unitig-caller", "latest": {"1.3.0--py311h6ecfb3b_4": "sha256:499f2ac938c0236800d2327b97a1669ecd798211af65688ec2d4e58835f307a9"}, "tags": {"1.3.0--py39h307a098_0": "sha256:1ffab8eede992b34218a162fbb3eaf9173528818795eb1acad711172561912e8", "1.3.0--py37h2c368fa_1": "sha256:9e28fe200f439e20ba8a72e272312736561e32a86d2db03f9dc76a5f26211bcf", "1.3.0--py310ha320341_2": "sha256:2870911ee13b3d05caa9062917cd5603160536f49b63955acae18173f4f8cedb", "1.3.0--py310ha320341_3": "sha256:a5bf88de1be2bc9d544c1f37e6fc4b45e85d9d1989f7850ed93caeea0908c88e", "1.3.0--py39h4ebf491_3": "sha256:ad56dcf83a67e5ee917e4e84fa9e674e6d720de333ebbac6153613d0f399b917", "1.3.0--py311h6ecfb3b_4": "sha256:499f2ac938c0236800d2327b97a1669ecd798211af65688ec2d4e58835f307a9"}, "docker": "quay.io/biocontainers/unitig-caller", "aliases": {"Bifrost": "/usr/local/bin/Bifrost", "unitig-caller": "/usr/local/bin/unitig-caller", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unitig-caller.
shpc-registry automated BioContainers addition for unitig-caller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unitig-caller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unitig-caller:1.3.0--py311h6ecfb3b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unitig-caller/1.3.0--py311h6ecfb3b_4
$ module help quay.io/biocontainers/unitig-caller/1.3.0--py311h6ecfb3b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unitig-caller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unitig-caller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unitig-caller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unitig-caller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unitig-caller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unitig-caller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bifrost

```bash
$ singularity exec <container> /usr/local/bin/Bifrost
$ podman run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitig-caller

```bash
$ singularity exec <container> /usr/local/bin/unitig-caller
$ podman run --it --rm --entrypoint /usr/local/bin/unitig-caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitig-caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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