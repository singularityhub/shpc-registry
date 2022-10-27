---
layout: container
name:  "quay.io/biocontainers/ngs_te_mapper2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngs_te_mapper2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ngs_te_mapper2/container.yaml"
updated_at: "2022-10-27 00:56:56.543077"
latest: "1.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/ngs_te_mapper2"
aliases:
 - "ngs_te_mapper2"
 - "queryRepeatDatabase.pl"
 - "queryTaxonomyDatabase.pl"
versions:
 - "1.0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for ngs_te_mapper2"
config: {"url": "https://biocontainers.pro/tools/ngs_te_mapper2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngs_te_mapper2", "latest": {"1.0.2--pyhdfd78af_1": "sha256:db69be145358560534e88b04dc3dd60149e874dd60972d37f485b5634d3b44ab"}, "tags": {"1.0.2--pyhdfd78af_1": "sha256:db69be145358560534e88b04dc3dd60149e874dd60972d37f485b5634d3b44ab"}, "docker": "quay.io/biocontainers/ngs_te_mapper2", "aliases": {"ngs_te_mapper2": "/usr/local/bin/ngs_te_mapper2", "queryRepeatDatabase.pl": "/usr/local/bin/queryRepeatDatabase.pl", "queryTaxonomyDatabase.pl": "/usr/local/bin/queryTaxonomyDatabase.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngs_te_mapper2.
shpc-registry automated BioContainers addition for ngs_te_mapper2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngs_te_mapper2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngs_te_mapper2:1.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngs_te_mapper2/1.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/ngs_te_mapper2/1.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngs_te_mapper2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngs_te_mapper2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngs_te_mapper2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngs_te_mapper2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngs_te_mapper2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngs_te_mapper2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngs_te_mapper2

```bash
$ singularity exec <container> /usr/local/bin/ngs_te_mapper2
$ podman run --it --rm --entrypoint /usr/local/bin/ngs_te_mapper2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngs_te_mapper2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryRepeatDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryRepeatDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryRepeatDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queryTaxonomyDatabase.pl

```bash
$ singularity exec <container> /usr/local/bin/queryTaxonomyDatabase.pl
$ podman run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queryTaxonomyDatabase.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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