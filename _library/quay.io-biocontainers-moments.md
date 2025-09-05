---
layout: container
name:  "quay.io/biocontainers/moments"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moments/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moments/container.yaml"
updated_at: "2025-09-05 03:27:24.166985"
latest: "1.4.5--py312hc9302aa_0"
container_url: "https://biocontainers.pro/tools/moments"
aliases:
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.1.5--py38h9af456f_0"
 - "1.1.16--py38hf6cf242_4"
 - "1.3.1--py39hbcbf7aa_0"
 - "1.4.3--py310h1fe012e_0"
 - "1.4.4--py310h1fe012e_0"
 - "1.4.5--py312hc9302aa_0"
description: "shpc-registry automated BioContainers addition for moments"
config: {"url": "https://biocontainers.pro/tools/moments", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for moments", "latest": {"1.4.5--py312hc9302aa_0": "sha256:d81e4d02a95831a9345bfb90638db6499ac17118776ce98b375efe23aa7f757d"}, "tags": {"1.1.5--py38h9af456f_0": "sha256:6e5fe05c7146d9dd1c9f82c51428e21252136fe9d0af4e66749d954c2ebcc81a", "1.1.16--py38hf6cf242_4": "sha256:7c71fb2ee05fec2d677a342fc871aa0568f4fcee6fb29240bcbb2c949f510a87", "1.3.1--py39hbcbf7aa_0": "sha256:5a193f7124179ab168d870549f139a9d726d4e99eef858a10d007461b10f8a40", "1.4.3--py310h1fe012e_0": "sha256:af1e51788f1a511d93f982cf63dc2e99eb4a9831aef82ff929d8a5089225bb56", "1.4.4--py310h1fe012e_0": "sha256:7750608e9090c88b7c9c92f276e94b1b99ede0a579cb48ffec23f11b7ee7b25e", "1.4.5--py312hc9302aa_0": "sha256:d81e4d02a95831a9345bfb90638db6499ac17118776ce98b375efe23aa7f757d"}, "docker": "quay.io/biocontainers/moments", "aliases": {"f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moments.
shpc-registry automated BioContainers addition for moments
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moments
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moments:1.4.5--py312hc9302aa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moments/1.4.5--py312hc9302aa_0
$ module help quay.io/biocontainers/moments/1.4.5--py312hc9302aa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moments-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moments-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moments-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moments-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moments-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moments-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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