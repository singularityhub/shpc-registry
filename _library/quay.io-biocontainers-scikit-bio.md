---
layout: container
name:  "quay.io/biocontainers/scikit-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scikit-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scikit-bio/container.yaml"
updated_at: "2024-01-04 02:50:38.999993"
latest: "0.4.2--np112py35_0"
container_url: "https://biocontainers.pro/tools/scikit-bio"
aliases:
 - "nosetests-3.5"
 - "doesitcache"
 - "nosetests"
 - "ipython3"
 - "ipython"
 - "easy_install-3.5"
 - "natsort"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
versions:
 - "0.4.2--np112py35_0"
description: "shpc-registry automated BioContainers addition for scikit-bio"
config: {"url": "https://biocontainers.pro/tools/scikit-bio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scikit-bio", "latest": {"0.4.2--np112py35_0": "sha256:b374dc7700762fa375847657559b2899baf65f105ce31bf76765c5dfd2c95191"}, "tags": {"0.4.2--np112py35_0": "sha256:b374dc7700762fa375847657559b2899baf65f105ce31bf76765c5dfd2c95191"}, "docker": "quay.io/biocontainers/scikit-bio", "aliases": {"nosetests-3.5": "/usr/local/bin/nosetests-3.5", "doesitcache": "/usr/local/bin/doesitcache", "nosetests": "/usr/local/bin/nosetests", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "easy_install-3.5": "/usr/local/bin/easy_install-3.5", "natsort": "/usr/local/bin/natsort", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scikit-bio.
shpc-registry automated BioContainers addition for scikit-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scikit-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scikit-bio:0.4.2--np112py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scikit-bio/0.4.2--np112py35_0
$ module help quay.io/biocontainers/scikit-bio/0.4.2--np112py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scikit-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scikit-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scikit-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scikit-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scikit-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scikit-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nosetests-3.5

```bash
$ singularity exec <container> /usr/local/bin/nosetests-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.5

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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