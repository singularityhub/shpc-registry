---
layout: container
name:  "quay.io/biocontainers/ebisearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ebisearch/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ebisearch/container.yaml"
updated_at: "2022-10-27 00:22:53.576229"
latest: "0.0.3--py_2"
container_url: "https://biocontainers.pro/tools/ebisearch"
aliases:
 - "ebi_metagenomics"
 - "ebisearch"
 - "flake8"
 - "pycodestyle"
 - "pyflakes"
versions:
 - "0.0.3--py_2"
description: "shpc-registry automated BioContainers addition for ebisearch"
config: {"url": "https://biocontainers.pro/tools/ebisearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ebisearch", "latest": {"0.0.3--py_2": "sha256:a525bf0301e81e0134d6d46356db1f2bd976805673598618994c52e8fa41f987"}, "tags": {"0.0.3--py_2": "sha256:a525bf0301e81e0134d6d46356db1f2bd976805673598618994c52e8fa41f987"}, "docker": "quay.io/biocontainers/ebisearch", "aliases": {"ebi_metagenomics": "/usr/local/bin/ebi_metagenomics", "ebisearch": "/usr/local/bin/ebisearch", "flake8": "/usr/local/bin/flake8", "pycodestyle": "/usr/local/bin/pycodestyle", "pyflakes": "/usr/local/bin/pyflakes"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ebisearch.
shpc-registry automated BioContainers addition for ebisearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ebisearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ebisearch:0.0.3--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ebisearch/0.0.3--py_2
$ module help quay.io/biocontainers/ebisearch/0.0.3--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ebisearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ebisearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ebisearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ebisearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ebisearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ebisearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ebi_metagenomics

```bash
$ singularity exec <container> /usr/local/bin/ebi_metagenomics
$ podman run --it --rm --entrypoint /usr/local/bin/ebi_metagenomics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ebi_metagenomics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ebisearch

```bash
$ singularity exec <container> /usr/local/bin/ebisearch
$ podman run --it --rm --entrypoint /usr/local/bin/ebisearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ebisearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flake8

```bash
$ singularity exec <container> /usr/local/bin/flake8
$ podman run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycodestyle

```bash
$ singularity exec <container> /usr/local/bin/pycodestyle
$ podman run --it --rm --entrypoint /usr/local/bin/pycodestyle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycodestyle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflakes

```bash
$ singularity exec <container> /usr/local/bin/pyflakes
$ podman run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
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