---
layout: container
name:  "quay.io/biocontainers/mhcgnomes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mhcgnomes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mhcgnomes/container.yaml"
updated_at: "2026-06-23 06:51:56.642915"
latest: "3.32.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mhcgnomes"
aliases:
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.8.4--pyh7cba7a3_0"
 - "1.8.6--pyh7cba7a3_0"
 - "2.0--pyh7e72e81_0"
 - "2.0.2--pyh106432d_0"
 - "3.31.1--pyhdfd78af_0"
 - "3.22.0--pyhdfd78af_0"
 - "3.19.0--pyh106432d_0"
 - "3.18.0--pyh106432d_0"
 - "3.15.0--pyh106432d_0"
 - "3.32.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mhcgnomes"
config: {"url": "https://biocontainers.pro/tools/mhcgnomes", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mhcgnomes", "latest": {"3.32.0--pyhdfd78af_0": "sha256:d413bb18a12c4cb5ea1032b764f894b04908850a1c62c1de7a5200ba325197b7"}, "tags": {"1.8.4--pyh7cba7a3_0": "sha256:14dd2760511144b2d4ed7a2aa397144543f0b125d9b863e296bb777fe79b1c75", "1.8.6--pyh7cba7a3_0": "sha256:63eceabba32c9cb3dc5afa58fb88c5b0bc571c83777cdcc613dd299097bc556b", "2.0--pyh7e72e81_0": "sha256:83acd7b5bdee07be35a39f05b7fede06c324cfdd5714550a834ca3e1d3cb0169", "2.0.2--pyh106432d_0": "sha256:20f04c96909805845970004d2bd581393807a18948d77eaf4669b8462ab86436", "3.31.1--pyhdfd78af_0": "sha256:7b4c2f1a4a5ccae29be60cea6d2888e127c8de40413171f1748c5ed5967433f1", "3.22.0--pyhdfd78af_0": "sha256:b8615193c1c053b99827ed02246f01677c45e3ac6951fd689bac1922e5d65ce0", "3.19.0--pyh106432d_0": "sha256:d3a38da2bb27cf5c37bb9a41317069589b2cc80015fe1ed35678b642d94f1bac", "3.18.0--pyh106432d_0": "sha256:2c1429aa226c913d116b5f359968e5095ff9230e02945307142b5522e9f4d66e", "3.15.0--pyh106432d_0": "sha256:c4da124b3035c12da206e39fb02c754087f8bc029a52a2d3e393afbad233bcf9", "3.32.0--pyhdfd78af_0": "sha256:d413bb18a12c4cb5ea1032b764f894b04908850a1c62c1de7a5200ba325197b7"}, "docker": "quay.io/biocontainers/mhcgnomes", "aliases": {"f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mhcgnomes.
singularity registry hpc automated addition for mhcgnomes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mhcgnomes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mhcgnomes:3.32.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mhcgnomes/3.32.0--pyhdfd78af_0
$ module help quay.io/biocontainers/mhcgnomes/3.32.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mhcgnomes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mhcgnomes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mhcgnomes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mhcgnomes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mhcgnomes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mhcgnomes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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