---
layout: container
name:  "quay.io/biocontainers/ebi-eva-common-pyutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ebi-eva-common-pyutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ebi-eva-common-pyutils/container.yaml"
updated_at: "2025-08-05 04:31:52.133190"
latest: "0.7.1--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/ebi-eva-common-pyutils"
aliases:
 - "archive_directory.py"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "xslt-config"
 - "xsltproc"
 - "normalizer"
versions:
 - "0.6.3--pyh7cba7a3_0"
 - "0.6.6--pyh7cba7a3_0"
 - "0.6.7--pyh7cba7a3_0"
 - "0.6.8--pyh7e72e81_0"
 - "0.6.10--pyh7e72e81_0"
 - "0.6.11--pyh7e72e81_0"
 - "0.6.12--pyh7e72e81_0"
 - "0.6.14--pyh7e72e81_0"
 - "0.7.0--pyh7e72e81_0"
 - "0.6.16--pyh7e72e81_0"
 - "0.7.1--pyh7e72e81_0"
description: "singularity registry hpc automated addition for ebi-eva-common-pyutils"
config: {"url": "https://biocontainers.pro/tools/ebi-eva-common-pyutils", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ebi-eva-common-pyutils", "latest": {"0.7.1--pyh7e72e81_0": "sha256:d829cd8b0f0c260fa00510deb69a43efc318dfa09951ce4131b7f50977e193c5"}, "tags": {"0.6.3--pyh7cba7a3_0": "sha256:db31057a9bfd43ad420626b42fa383c137baa3d964f1a16d84a7f6aef89ddf18", "0.6.6--pyh7cba7a3_0": "sha256:0491789dfef5a02db12ab18e8eff263a99f902e5f92d52ea5495faf6d5bed282", "0.6.7--pyh7cba7a3_0": "sha256:31ed4eec9142b77bd0be9a4928971a54f7a2ee56ec0a867b63b369e745b272df", "0.6.8--pyh7e72e81_0": "sha256:d7d587a89b266bf6890a7de2b9ab37964e3b12dec614771ee803cd0951d078c5", "0.6.10--pyh7e72e81_0": "sha256:9ba2f752277824d8d8f86495eb5d76288615ef2da6a236d1947972c1b3041cf6", "0.6.11--pyh7e72e81_0": "sha256:11314f9d43beaac6fd0161a06bd983e941e469108cf3052a5740821aff757687", "0.6.12--pyh7e72e81_0": "sha256:8fdde24afc54c48710169dfb5696dfcb01c19bee0ee39e935c6e9e61da8eae7f", "0.6.14--pyh7e72e81_0": "sha256:a7878da2288fead197d01eda864b7b68d61e76af9c912a49740763ba6e7508f7", "0.7.0--pyh7e72e81_0": "sha256:81263f654526c6705f05c654b4e68dff7be74bf3e23f9015d3e3e75e6ccaf230", "0.6.16--pyh7e72e81_0": "sha256:b33f6f903bbbd2e44e7e7912addbe8e2e88282cbe86398c134081c1b8daf657d", "0.7.1--pyh7e72e81_0": "sha256:d829cd8b0f0c260fa00510deb69a43efc318dfa09951ce4131b7f50977e193c5"}, "docker": "quay.io/biocontainers/ebi-eva-common-pyutils", "aliases": {"archive_directory.py": "/usr/local/bin/archive_directory.py", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ebi-eva-common-pyutils.
singularity registry hpc automated addition for ebi-eva-common-pyutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ebi-eva-common-pyutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ebi-eva-common-pyutils:0.7.1--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ebi-eva-common-pyutils/0.7.1--pyh7e72e81_0
$ module help quay.io/biocontainers/ebi-eva-common-pyutils/0.7.1--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ebi-eva-common-pyutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ebi-eva-common-pyutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ebi-eva-common-pyutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ebi-eva-common-pyutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ebi-eva-common-pyutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ebi-eva-common-pyutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### archive_directory.py

```bash
$ singularity exec <container> /usr/local/bin/archive_directory.py
$ podman run --it --rm --entrypoint /usr/local/bin/archive_directory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive_directory.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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