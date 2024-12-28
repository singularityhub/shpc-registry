---
layout: container
name:  "quay.io/biocontainers/primer3-py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primer3-py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primer3-py/container.yaml"
updated_at: "2024-12-28 03:17:31.753349"
latest: "2.0.3--py310h1fe012e_4"
container_url: "https://biocontainers.pro/tools/primer3-py"
aliases:
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.6.1--py27h9801fc8_1"
 - "1.2.0--py311hec16e2b_0"
 - "1.2.1--py311hec16e2b_0"
 - "2.0.0--py311hec16e2b_0"
 - "1.2.2--py311hec16e2b_0"
 - "2.0.1--py311h031d066_0"
 - "2.0.1--py39hf95cd2a_1"
 - "2.0.3--py310h4b81fae_0"
 - "2.0.3--py38he5da3d1_0"
 - "0.6.1--py310h1425a21_1"
 - "2.0.3--py39hf95cd2a_1"
 - "2.0.3--py312hf67a6ed_2"
 - "2.0.3--py310h7c593f9_3"
 - "2.0.3--py310h1fe012e_4"
description: "shpc-registry automated BioContainers addition for primer3-py"
config: {"url": "https://biocontainers.pro/tools/primer3-py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for primer3-py", "latest": {"2.0.3--py310h1fe012e_4": "sha256:3bfa6a73d287f1db85379e9125a4d00c2a1bf6d61d000d830e4e64ab98f4d1bb"}, "tags": {"0.6.1--py27h9801fc8_1": "sha256:61a01cd51d6f5e74dff60f08b12aeefb44e74b51a26b2c7146d92fac7fa66593", "1.2.0--py311hec16e2b_0": "sha256:eb6a8c0d9785e85a23ec7427d77ff942f1cd6f5adefec875cd60ea7240ccb210", "1.2.1--py311hec16e2b_0": "sha256:52b73c4300355427a0707859457eb1cec8f32c148796f8b14e9ba16fe49c1e1e", "2.0.0--py311hec16e2b_0": "sha256:5f7ffb160d571bd27e41b3b15638f2ce0f56c92591e679d5626a23992fa37156", "1.2.2--py311hec16e2b_0": "sha256:6043cdd10fe44721b7ee33acb83d87bd7fbb612c783dda15e6d480485f532d97", "2.0.1--py311h031d066_0": "sha256:ca4233e61403c347ff4d15d670b33461b2215d988df036b8cde11e402f49122a", "2.0.1--py39hf95cd2a_1": "sha256:cae7b6397b67e8970d4165041b760c6993c9225bd054338aa390776651add91e", "2.0.3--py310h4b81fae_0": "sha256:8fa7b2bce1376b7c48357b93f969b4bb3fe0d286b2b52bd92f02bc08f29c0105", "2.0.3--py38he5da3d1_0": "sha256:3ae30d3b0e255aaae89ff12803047c2aeef024d80fecfdd190227f29631b692a", "0.6.1--py310h1425a21_1": "sha256:68087f5fcefd8d186f9dd363078ec57430e54342e9ec7af427b50e6893e22151", "2.0.3--py39hf95cd2a_1": "sha256:c7f6c2173f906865a52d40bfe24975fb37e6eb311526fecd4e1b544772b53224", "2.0.3--py312hf67a6ed_2": "sha256:b86ce467296e39d898591a4418372b63f47c048ace7ad90660c6ca20626272e5", "2.0.3--py310h7c593f9_3": "sha256:002b7de7942ba2facb418385561011665b6334304858cb93b3ed9c98e77ada29", "2.0.3--py310h1fe012e_4": "sha256:3bfa6a73d287f1db85379e9125a4d00c2a1bf6d61d000d830e4e64ab98f4d1bb"}, "docker": "quay.io/biocontainers/primer3-py", "aliases": {"python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primer3-py.
shpc-registry automated BioContainers addition for primer3-py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primer3-py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primer3-py:2.0.3--py310h1fe012e_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primer3-py/2.0.3--py310h1fe012e_4
$ module help quay.io/biocontainers/primer3-py/2.0.3--py310h1fe012e_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primer3-py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primer3-py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primer3-py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primer3-py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primer3-py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primer3-py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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