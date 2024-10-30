---
layout: container
name:  "quay.io/biocontainers/marge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/marge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/marge/container.yaml"
updated_at: "2024-10-30 03:41:30.559212"
latest: "1.0--py_2"
container_url: "https://biocontainers.pro/tools/marge"
aliases:
 - "bedClip"
 - "bigWigAverageOverBed"
 - "bigWigSummary"
 - "bigWigToBedGraph"
 - "marge"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "snakemake"
 - "snakemake-bash-completion"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "rst2html4.py"
versions:
 - "1.0--py_2"
description: "shpc-registry automated BioContainers addition for marge"
config: {"url": "https://biocontainers.pro/tools/marge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for marge", "latest": {"1.0--py_2": "sha256:10636dbc08cea413c7320684a1ee7b6e9ae80107715b7fe745d7ab5b2c85ff08"}, "tags": {"1.0--py_2": "sha256:10636dbc08cea413c7320684a1ee7b6e9ae80107715b7fe745d7ab5b2c85ff08"}, "docker": "quay.io/biocontainers/marge", "aliases": {"bedClip": "/usr/local/bin/bedClip", "bigWigAverageOverBed": "/usr/local/bin/bigWigAverageOverBed", "bigWigSummary": "/usr/local/bin/bigWigSummary", "bigWigToBedGraph": "/usr/local/bin/bigWigToBedGraph", "marge": "/usr/local/bin/marge", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "rst2html4.py": "/usr/local/bin/rst2html4.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/marge.
shpc-registry automated BioContainers addition for marge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/marge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/marge:1.0--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/marge/1.0--py_2
$ module help quay.io/biocontainers/marge/1.0--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### marge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### marge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### marge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### marge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### marge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### marge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedClip

```bash
$ singularity exec <container> /usr/local/bin/bedClip
$ podman run --it --rm --entrypoint /usr/local/bin/bedClip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedClip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigAverageOverBed

```bash
$ singularity exec <container> /usr/local/bin/bigWigAverageOverBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigSummary

```bash
$ singularity exec <container> /usr/local/bin/bigWigSummary
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigToBedGraph

```bash
$ singularity exec <container> /usr/local/bin/bigWigToBedGraph
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### marge

```bash
$ singularity exec <container> /usr/local/bin/marge
$ podman run --it --rm --entrypoint /usr/local/bin/marge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/marge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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