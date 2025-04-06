---
layout: container
name:  "quay.io/biocontainers/concoct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/concoct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/concoct/container.yaml"
updated_at: "2025-04-06 03:11:32.685287"
latest: "1.1.0--py312h245ed52_6"
container_url: "https://biocontainers.pro/tools/concoct"
aliases:
 - "concoct"
 - "concoct_coverage_table.py"
 - "concoct_refine"
 - "cut_up_fasta.py"
 - "extract_fasta_bins.py"
 - "merge_cutup_clustering.py"
 - "nosetests-3.9"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
 - "oshfort"
 - "oshmem_info"
versions:
 - "1.1.0--py310h74abf4b_3"
 - "1.1.0--py311h245ed52_4"
 - "1.1.0--py312h245ed52_6"
description: "shpc-registry automated BioContainers addition for concoct"
config: {"url": "https://biocontainers.pro/tools/concoct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for concoct", "latest": {"1.1.0--py312h245ed52_6": "sha256:740d179e3ffc55778c2d06c04d1f56fd9f651708e8377e531e5a72b8e6f5794b"}, "tags": {"1.1.0--py310h74abf4b_3": "sha256:109756b95a510daac9a52b9bb54520c065694eccbaff5a1ff8a502747ec297f5", "1.1.0--py311h245ed52_4": "sha256:ca54fa0e5365a7676307befad617fbd646b3fb61fa7e686bd604a91eeec361b9", "1.1.0--py312h245ed52_6": "sha256:740d179e3ffc55778c2d06c04d1f56fd9f651708e8377e531e5a72b8e6f5794b"}, "docker": "quay.io/biocontainers/concoct", "aliases": {"concoct": "/usr/local/bin/concoct", "concoct_coverage_table.py": "/usr/local/bin/concoct_coverage_table.py", "concoct_refine": "/usr/local/bin/concoct_refine", "cut_up_fasta.py": "/usr/local/bin/cut_up_fasta.py", "extract_fasta_bins.py": "/usr/local/bin/extract_fasta_bins.py", "merge_cutup_clustering.py": "/usr/local/bin/merge_cutup_clustering.py", "nosetests-3.9": "/usr/local/bin/nosetests-3.9", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/concoct.
shpc-registry automated BioContainers addition for concoct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/concoct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/concoct:1.1.0--py312h245ed52_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/concoct/1.1.0--py312h245ed52_6
$ module help quay.io/biocontainers/concoct/1.1.0--py312h245ed52_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### concoct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### concoct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### concoct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### concoct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### concoct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### concoct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### concoct

```bash
$ singularity exec <container> /usr/local/bin/concoct
$ podman run --it --rm --entrypoint /usr/local/bin/concoct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct_coverage_table.py

```bash
$ singularity exec <container> /usr/local/bin/concoct_coverage_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/concoct_coverage_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct_coverage_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct_refine

```bash
$ singularity exec <container> /usr/local/bin/concoct_refine
$ podman run --it --rm --entrypoint /usr/local/bin/concoct_refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct_refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_up_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/cut_up_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_up_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_up_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fasta_bins.py

```bash
$ singularity exec <container> /usr/local/bin/extract_fasta_bins.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fasta_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fasta_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_cutup_clustering.py

```bash
$ singularity exec <container> /usr/local/bin/merge_cutup_clustering.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_cutup_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_cutup_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests-3.9

```bash
$ singularity exec <container> /usr/local/bin/nosetests-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshfort

```bash
$ singularity exec <container> /usr/local/bin/oshfort
$ podman run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshmem_info

```bash
$ singularity exec <container> /usr/local/bin/oshmem_info
$ podman run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
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