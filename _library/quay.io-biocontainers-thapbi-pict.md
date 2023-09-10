---
layout: container
name:  "quay.io/biocontainers/thapbi-pict"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/thapbi-pict/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/thapbi-pict/container.yaml"
updated_at: "2023-09-10 02:55:49.742965"
latest: "0.6.14--py_0"
container_url: "https://biocontainers.pro/tools/thapbi-pict"
aliases:
 - "amplicon_contingency_table.py"
 - "graph_plot.py"
 - "swarm"
 - "thapbi_pict"
 - "flash"
 - "igraph"
 - "cutadapt"
 - "vba_extract.py"
 - "trimmomatic"
 - "cxpm"
 - "sxpm"
 - "pigz"
 - "unpigz"
 - "fetch-extras"
versions:
 - "0.6.9--py_0"
 - "0.6.14--py_0"
description: "shpc-registry automated BioContainers addition for thapbi-pict"
config: {"url": "https://biocontainers.pro/tools/thapbi-pict", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for thapbi-pict", "latest": {"0.6.14--py_0": "sha256:6131cfe22d21355f9a7d1ae5540e6bafdd78d4cfbea1f5537c7c22f367fe9336"}, "tags": {"0.6.9--py_0": "sha256:3e121a42248380dea6324a085d0058c246a3b81622463da45e63f255716a6ff3", "0.6.14--py_0": "sha256:6131cfe22d21355f9a7d1ae5540e6bafdd78d4cfbea1f5537c7c22f367fe9336"}, "docker": "quay.io/biocontainers/thapbi-pict", "aliases": {"amplicon_contingency_table.py": "/usr/local/bin/amplicon_contingency_table.py", "graph_plot.py": "/usr/local/bin/graph_plot.py", "swarm": "/usr/local/bin/swarm", "thapbi_pict": "/usr/local/bin/thapbi_pict", "flash": "/usr/local/bin/flash", "igraph": "/usr/local/bin/igraph", "cutadapt": "/usr/local/bin/cutadapt", "vba_extract.py": "/usr/local/bin/vba_extract.py", "trimmomatic": "/usr/local/bin/trimmomatic", "cxpm": "/usr/local/bin/cxpm", "sxpm": "/usr/local/bin/sxpm", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "fetch-extras": "/usr/local/bin/fetch-extras"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/thapbi-pict.
shpc-registry automated BioContainers addition for thapbi-pict
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/thapbi-pict
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/thapbi-pict:0.6.14--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/thapbi-pict/0.6.14--py_0
$ module help quay.io/biocontainers/thapbi-pict/0.6.14--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### thapbi-pict-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### thapbi-pict-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### thapbi-pict-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### thapbi-pict-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### thapbi-pict-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### thapbi-pict-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplicon_contingency_table.py

```bash
$ singularity exec <container> /usr/local/bin/amplicon_contingency_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/amplicon_contingency_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicon_contingency_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph_plot.py

```bash
$ singularity exec <container> /usr/local/bin/graph_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/graph_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swarm

```bash
$ singularity exec <container> /usr/local/bin/swarm
$ podman run --it --rm --entrypoint /usr/local/bin/swarm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swarm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thapbi_pict

```bash
$ singularity exec <container> /usr/local/bin/thapbi_pict
$ podman run --it --rm --entrypoint /usr/local/bin/thapbi_pict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thapbi_pict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxpm

```bash
$ singularity exec <container> /usr/local/bin/cxpm
$ podman run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sxpm

```bash
$ singularity exec <container> /usr/local/bin/sxpm
$ podman run --it --rm --entrypoint /usr/local/bin/sxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sxpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
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