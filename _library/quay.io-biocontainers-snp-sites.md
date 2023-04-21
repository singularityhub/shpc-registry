---
layout: container
name:  "quay.io/biocontainers/snp-sites"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snp-sites/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snp-sites/container.yaml"
updated_at: "2023-04-21 02:51:53.050870"
latest: "2.5.1--h7132678_2"
container_url: "https://biocontainers.pro/tools/snp-sites"
aliases:
 - "snp-sites"
versions:
 - "2.5.1--h7132678_2"
description: "shpc-registry automated BioContainers addition for snp-sites"
config: {"url": "https://biocontainers.pro/tools/snp-sites", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snp-sites", "latest": {"2.5.1--h7132678_2": "sha256:52d05918e0f415a835b380501fb6f62f94543ef3d0037dcc335a140ba174c826"}, "tags": {"2.5.1--h7132678_2": "sha256:52d05918e0f415a835b380501fb6f62f94543ef3d0037dcc335a140ba174c826"}, "docker": "quay.io/biocontainers/snp-sites", "aliases": {"snp-sites": "/usr/local/bin/snp-sites"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snp-sites.
shpc-registry automated BioContainers addition for snp-sites
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snp-sites
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snp-sites:2.5.1--h7132678_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snp-sites/2.5.1--h7132678_2
$ module help quay.io/biocontainers/snp-sites/2.5.1--h7132678_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snp-sites-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snp-sites-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snp-sites-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snp-sites-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snp-sites-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snp-sites-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snp-sites

```bash
$ singularity exec <container> /usr/local/bin/snp-sites
$ podman run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-sites   -v ${PWD} -w ${PWD} <container> -c " $@"
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