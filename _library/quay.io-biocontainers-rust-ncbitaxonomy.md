---
layout: container
name:  "quay.io/biocontainers/rust-ncbitaxonomy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust-ncbitaxonomy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust-ncbitaxonomy/container.yaml"
updated_at: "2025-09-29 03:40:40.447211"
latest: "1.0.7--hf9427c6_6"
container_url: "https://biocontainers.pro/tools/rust-ncbitaxonomy"
aliases:
 - "taxonomy_filter_fastq"
 - "taxonomy_filter_refseq"
 - "taxonomy_util"
versions:
 - "1.0.7--h94d9fb8_2"
 - "1.0.7--h6145f2c_4"
 - "1.0.7--h6e4802e_5"
 - "1.0.7--hf9427c6_6"
description: "shpc-registry automated BioContainers addition for rust-ncbitaxonomy"
config: {"url": "https://biocontainers.pro/tools/rust-ncbitaxonomy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rust-ncbitaxonomy", "latest": {"1.0.7--hf9427c6_6": "sha256:3e5b258f55b908a14a47d8d83b90af20f7c5b91318ad74f661a462e3514583b3"}, "tags": {"1.0.7--h94d9fb8_2": "sha256:2a15e01071448b8ceaa9ae7aea45da2b1f20a38afc8fda5f65099d68193f99a8", "1.0.7--h6145f2c_4": "sha256:31df5df71ebc0fa39dacacea9dfae46c496fc916c0f5811dc4aab39641d5912a", "1.0.7--h6e4802e_5": "sha256:b87025d6b72e22939041671f84a540613e4c8d03f5318a3a8a80ffefcefee51e", "1.0.7--hf9427c6_6": "sha256:3e5b258f55b908a14a47d8d83b90af20f7c5b91318ad74f661a462e3514583b3"}, "docker": "quay.io/biocontainers/rust-ncbitaxonomy", "aliases": {"taxonomy_filter_fastq": "/usr/local/bin/taxonomy_filter_fastq", "taxonomy_filter_refseq": "/usr/local/bin/taxonomy_filter_refseq", "taxonomy_util": "/usr/local/bin/taxonomy_util"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust-ncbitaxonomy.
shpc-registry automated BioContainers addition for rust-ncbitaxonomy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust-ncbitaxonomy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust-ncbitaxonomy:1.0.7--hf9427c6_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust-ncbitaxonomy/1.0.7--hf9427c6_6
$ module help quay.io/biocontainers/rust-ncbitaxonomy/1.0.7--hf9427c6_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-ncbitaxonomy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-ncbitaxonomy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-ncbitaxonomy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-ncbitaxonomy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-ncbitaxonomy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-ncbitaxonomy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### taxonomy_filter_fastq

```bash
$ singularity exec <container> /usr/local/bin/taxonomy_filter_fastq
$ podman run --it --rm --entrypoint /usr/local/bin/taxonomy_filter_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonomy_filter_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonomy_filter_refseq

```bash
$ singularity exec <container> /usr/local/bin/taxonomy_filter_refseq
$ podman run --it --rm --entrypoint /usr/local/bin/taxonomy_filter_refseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonomy_filter_refseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonomy_util

```bash
$ singularity exec <container> /usr/local/bin/taxonomy_util
$ podman run --it --rm --entrypoint /usr/local/bin/taxonomy_util   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonomy_util   -v ${PWD} -w ${PWD} <container> -c " $@"
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