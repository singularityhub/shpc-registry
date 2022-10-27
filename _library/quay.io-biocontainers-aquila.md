---
layout: container
name:  "quay.io/biocontainers/aquila"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aquila/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/aquila/container.yaml"
updated_at: "2022-10-27 00:22:24.227113"
latest: "1.0.0--py_0"
container_url: "https://biocontainers.pro/tools/aquila"
aliases:
 - "Aquila_assembly_based_variants_call"
 - "Aquila_clean"
 - "Aquila_phasing_all_variants"
 - "Aquila_step0_sortbam"
 - "Aquila_step0_sortbam_multilibs"
 - "Aquila_step1"
 - "Aquila_step1_multilibs"
 - "Aquila_step2"
versions:
 - "1.0.0--py_0"
description: "shpc-registry automated BioContainers addition for aquila"
config: {"url": "https://biocontainers.pro/tools/aquila", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aquila", "latest": {"1.0.0--py_0": "sha256:f774c52e37a4022c2129fa3a27e530934a614c9f75cffa75bad3fcb63734b8fb"}, "tags": {"1.0.0--py_0": "sha256:f774c52e37a4022c2129fa3a27e530934a614c9f75cffa75bad3fcb63734b8fb"}, "docker": "quay.io/biocontainers/aquila", "aliases": {"Aquila_assembly_based_variants_call": "/usr/local/bin/Aquila_assembly_based_variants_call", "Aquila_clean": "/usr/local/bin/Aquila_clean", "Aquila_phasing_all_variants": "/usr/local/bin/Aquila_phasing_all_variants", "Aquila_step0_sortbam": "/usr/local/bin/Aquila_step0_sortbam", "Aquila_step0_sortbam_multilibs": "/usr/local/bin/Aquila_step0_sortbam_multilibs", "Aquila_step1": "/usr/local/bin/Aquila_step1", "Aquila_step1_multilibs": "/usr/local/bin/Aquila_step1_multilibs", "Aquila_step2": "/usr/local/bin/Aquila_step2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aquila.
shpc-registry automated BioContainers addition for aquila
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aquila
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aquila:1.0.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aquila/1.0.0--py_0
$ module help quay.io/biocontainers/aquila/1.0.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aquila-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aquila-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aquila-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aquila-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aquila-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aquila-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Aquila_assembly_based_variants_call

```bash
$ singularity exec <container> /usr/local/bin/Aquila_assembly_based_variants_call
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_assembly_based_variants_call   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_assembly_based_variants_call   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_clean

```bash
$ singularity exec <container> /usr/local/bin/Aquila_clean
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_phasing_all_variants

```bash
$ singularity exec <container> /usr/local/bin/Aquila_phasing_all_variants
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_phasing_all_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_phasing_all_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step0_sortbam

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step0_sortbam
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step0_sortbam_multilibs

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step0_sortbam_multilibs
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step1

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step1
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step1_multilibs

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step1_multilibs
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step1_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step1_multilibs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step2

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step2
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
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