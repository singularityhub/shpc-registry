---
layout: container
name:  "quay.io/biocontainers/htseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/htseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/htseq/container.yaml"
updated_at: "2024-07-14 03:12:19.845968"
latest: "2.0.5--py39h91a4a08_2"
container_url: "https://biocontainers.pro/tools/htseq"
aliases:
 - "htseq-count"
 - "htseq-qa"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "jpgicc"
versions:
 - "0.9.1--py37h70f9b12_3"
 - "0.12.4--py36h39af1c6_1"
 - "0.11.3--py27hb3f55d8_0"
 - "2.0.5--py310h5aa3a86_0"
 - "1.99.2--py39h919a90d_2"
 - "0.13.5--py39h70b41aa_1"
 - "0.12.4--py38h1773678_2"
 - "0.11.3--py37hb3f55d8_0"
 - "2.0.5--py38h8c35140_1"
 - "2.0.5--py39h91a4a08_2"
description: "shpc-registry automated BioContainers addition for htseq"
config: {"url": "https://biocontainers.pro/tools/htseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for htseq", "latest": {"2.0.5--py39h91a4a08_2": "sha256:02f89abe2a42958ea9cad8343e9f1ac3a744a41cfc57350b520cf111e1f5dc07"}, "tags": {"0.9.1--py37h70f9b12_3": "sha256:f10c9c62602ecef7b4c32ed64e506b4dc4d024d3d07aa45498fd18a684c17464", "0.12.4--py36h39af1c6_1": "sha256:07a8a108bcce188c6d35f46011ffec147df6d2eabe581033889745561fef579f", "0.11.3--py27hb3f55d8_0": "sha256:c81d4143ebeb36c829266bf585993405fadfc52c7954e7a6c40f4ba83713a6d3", "2.0.5--py310h5aa3a86_0": "sha256:fa62d637083ba2721efbba9e7adf64e6874ad934c425ca1344a24e84e18f71d8", "1.99.2--py39h919a90d_2": "sha256:00ded95ce65f126e3eb1ec9798f7ced64a94fdaa32387e9a078c16195203c96f", "0.13.5--py39h70b41aa_1": "sha256:27e176b86dcb5d2f3caf8a632429b1516ba455cd4fe1b689f489e3c8c9bb6b09", "0.12.4--py38h1773678_2": "sha256:d35acbe46e7ea06e0d519eb82ce483b4ad2d90825082a52762056f9cb7eb3bde", "0.11.3--py37hb3f55d8_0": "sha256:d8234dc9fe572f975ca32c155af097221eb068ed4261783b08dd714f9de407db", "2.0.5--py38h8c35140_1": "sha256:a58d928d043cbf46f9d53bc9cf9a23fb4b3769e1b4acf7dec4aa04b04c248a2d", "2.0.5--py39h91a4a08_2": "sha256:02f89abe2a42958ea9cad8343e9f1ac3a744a41cfc57350b520cf111e1f5dc07"}, "docker": "quay.io/biocontainers/htseq", "aliases": {"htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "jpgicc": "/usr/local/bin/jpgicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/htseq.
shpc-registry automated BioContainers addition for htseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/htseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/htseq:2.0.5--py39h91a4a08_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/htseq/2.0.5--py39h91a4a08_2
$ module help quay.io/biocontainers/htseq/2.0.5--py39h91a4a08_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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