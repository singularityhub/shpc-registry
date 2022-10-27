---
layout: container
name:  "quay.io/biocontainers/cnv_facets"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cnv_facets/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cnv_facets/container.yaml"
updated_at: "2022-10-27 00:50:33.116777"
latest: "v0.11.3--r351_2"
container_url: "https://biocontainers.pro/tools/cnv_facets"
aliases:
 - "cnv_facets.R"
 - "snp-pileup"
versions:
 - "v0.11.3--r351_2"
description: "shpc-registry automated BioContainers addition for cnv_facets"
config: {"url": "https://biocontainers.pro/tools/cnv_facets", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cnv_facets", "latest": {"v0.11.3--r351_2": "sha256:c6fb22e0ee176146131e9dfe8411b0e3e2128ec6a65c96441ca59c6fc1427068"}, "tags": {"v0.11.3--r351_2": "sha256:c6fb22e0ee176146131e9dfe8411b0e3e2128ec6a65c96441ca59c6fc1427068"}, "docker": "quay.io/biocontainers/cnv_facets", "aliases": {"cnv_facets.R": "/usr/local/bin/cnv_facets.R", "snp-pileup": "/usr/local/bin/snp-pileup"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cnv_facets.
shpc-registry automated BioContainers addition for cnv_facets
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cnv_facets
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cnv_facets:v0.11.3--r351_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cnv_facets/v0.11.3--r351_2
$ module help quay.io/biocontainers/cnv_facets/v0.11.3--r351_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cnv_facets-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cnv_facets-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cnv_facets-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cnv_facets-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cnv_facets-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cnv_facets-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cnv_facets.R

```bash
$ singularity exec <container> /usr/local/bin/cnv_facets.R
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_facets.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_facets.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp-pileup

```bash
$ singularity exec <container> /usr/local/bin/snp-pileup
$ podman run --it --rm --entrypoint /usr/local/bin/snp-pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
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