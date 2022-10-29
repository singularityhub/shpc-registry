---
layout: container
name:  "quay.io/biocontainers/thapbi-pict"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/thapbi-pict/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/thapbi-pict/container.yaml"
updated_at: "2022-10-29 05:50:38.963407"
latest: "0.6.9--py_0"
container_url: "https://biocontainers.pro/tools/thapbi-pict"
aliases:
 - "amplicon_contingency_table.py"
 - "graph_plot.py"
 - "swarm"
 - "thapbi_pict"
 - "2to3-3.7"
 - "acyclic"
 - "alimask"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "aserver"
 - "asp-cp"
 - "asp-ls"
 - "bcomps"
 - "between-two-genes"
versions:
 - "0.6.9--py_0"
description: "shpc-registry automated BioContainers addition for thapbi-pict"
config: {"url": "https://biocontainers.pro/tools/thapbi-pict", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for thapbi-pict", "latest": {"0.6.9--py_0": "sha256:3e121a42248380dea6324a085d0058c246a3b81622463da45e63f255716a6ff3"}, "tags": {"0.6.9--py_0": "sha256:3e121a42248380dea6324a085d0058c246a3b81622463da45e63f255716a6ff3"}, "docker": "quay.io/biocontainers/thapbi-pict", "aliases": {"amplicon_contingency_table.py": "/usr/local/bin/amplicon_contingency_table.py", "graph_plot.py": "/usr/local/bin/graph_plot.py", "swarm": "/usr/local/bin/swarm", "thapbi_pict": "/usr/local/bin/thapbi_pict", "2to3-3.7": "/usr/local/bin/2to3-3.7", "acyclic": "/usr/local/bin/acyclic", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "aserver": "/usr/local/bin/aserver", "asp-cp": "/usr/local/bin/asp-cp", "asp-ls": "/usr/local/bin/asp-ls", "bcomps": "/usr/local/bin/bcomps", "between-two-genes": "/usr/local/bin/between-two-genes"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/thapbi-pict.
shpc-registry automated BioContainers addition for thapbi-pict
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/thapbi-pict
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/thapbi-pict:0.6.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/thapbi-pict/0.6.9--py_0
$ module help quay.io/biocontainers/thapbi-pict/0.6.9--py_0
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


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-cp

```bash
$ singularity exec <container> /usr/local/bin/asp-cp
$ podman run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-ls

```bash
$ singularity exec <container> /usr/local/bin/asp-ls
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### between-two-genes

```bash
$ singularity exec <container> /usr/local/bin/between-two-genes
$ podman run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/between-two-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
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