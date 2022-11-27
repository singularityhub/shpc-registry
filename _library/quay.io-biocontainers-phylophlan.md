---
layout: container
name:  "quay.io/biocontainers/phylophlan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylophlan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylophlan/container.yaml"
updated_at: "2022-11-27 00:47:43.118940"
latest: "3.0--py_7"
container_url: "https://biocontainers.pro/tools/phylophlan"
aliases:
 - "phylophlan"
 - "phylophlan_draw_metagenomic"
 - "phylophlan_get_reference"
 - "phylophlan_metagenomic"
 - "phylophlan_setup_database"
 - "phylophlan_strain_finder"
 - "phylophlan_write_config_file"
 - "phylophlan_write_default_configs.sh"
 - "readal"
 - "statal"
 - "trimal"
 - "iqtree"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
versions:
 - "3.0--py_7"
description: "shpc-registry automated BioContainers addition for phylophlan"
config: {"url": "https://biocontainers.pro/tools/phylophlan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylophlan", "latest": {"3.0--py_7": "sha256:7ad925997528299766b3f7cab8b13ce447e3715c4010976556d6a014a2f4ac83"}, "tags": {"3.0--py_7": "sha256:7ad925997528299766b3f7cab8b13ce447e3715c4010976556d6a014a2f4ac83"}, "docker": "quay.io/biocontainers/phylophlan", "aliases": {"phylophlan": "/usr/local/bin/phylophlan", "phylophlan_draw_metagenomic": "/usr/local/bin/phylophlan_draw_metagenomic", "phylophlan_get_reference": "/usr/local/bin/phylophlan_get_reference", "phylophlan_metagenomic": "/usr/local/bin/phylophlan_metagenomic", "phylophlan_setup_database": "/usr/local/bin/phylophlan_setup_database", "phylophlan_strain_finder": "/usr/local/bin/phylophlan_strain_finder", "phylophlan_write_config_file": "/usr/local/bin/phylophlan_write_config_file", "phylophlan_write_default_configs.sh": "/usr/local/bin/phylophlan_write_default_configs.sh", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "iqtree": "/usr/local/bin/iqtree", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylophlan.
shpc-registry automated BioContainers addition for phylophlan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylophlan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylophlan:3.0--py_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylophlan/3.0--py_7
$ module help quay.io/biocontainers/phylophlan/3.0--py_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylophlan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylophlan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylophlan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylophlan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylophlan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylophlan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phylophlan

```bash
$ singularity exec <container> /usr/local/bin/phylophlan
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_draw_metagenomic

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_draw_metagenomic
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_draw_metagenomic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_draw_metagenomic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_get_reference

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_get_reference
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_get_reference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_get_reference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_metagenomic

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_metagenomic
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_metagenomic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_metagenomic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_setup_database

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_setup_database
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_setup_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_setup_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_strain_finder

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_strain_finder
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_strain_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_strain_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_write_config_file

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_write_config_file
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_write_config_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_write_config_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylophlan_write_default_configs.sh

```bash
$ singularity exec <container> /usr/local/bin/phylophlan_write_default_configs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/phylophlan_write_default_configs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylophlan_write_default_configs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
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