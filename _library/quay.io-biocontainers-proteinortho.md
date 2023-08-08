---
layout: container
name:  "quay.io/biocontainers/proteinortho"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteinortho/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteinortho/container.yaml"
updated_at: "2023-08-08 03:00:38.910603"
latest: "6.1.1--hedee03e_0"
container_url: "https://biocontainers.pro/tools/proteinortho"
aliases:
 - "proteinortho"
 - "proteinortho2html.pl"
 - "proteinortho2tree.pl"
 - "proteinortho2xml.pl"
 - "proteinortho6.pl"
 - "proteinortho_cleanupblastgraph"
 - "proteinortho_clustering"
 - "proteinortho_compareProteinorthoGraphs.pl"
 - "proteinortho_do_mcl.pl"
 - "proteinortho_extract_from_graph.pl"
 - "proteinortho_ffadj_mcs.py"
 - "proteinortho_formatUsearch.pl"
 - "proteinortho_grab_proteins.pl"
 - "proteinortho_graphMinusRemovegraph"
 - "proteinortho_history.pl"
 - "proteinortho_singletons.pl"
 - "proteinortho_summary.pl"
 - "proteinortho_treeBuilderCore"
 - "diamond"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "6.1.1--hedee03e_0"
description: "shpc-registry automated BioContainers addition for proteinortho"
config: {"url": "https://biocontainers.pro/tools/proteinortho", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteinortho", "latest": {"6.1.1--hedee03e_0": "sha256:ca4852ad87a13e4f6f95f540c0839e9884ee42037562dbe80b0c40631070e6dc"}, "tags": {"6.1.1--hedee03e_0": "sha256:ca4852ad87a13e4f6f95f540c0839e9884ee42037562dbe80b0c40631070e6dc"}, "docker": "quay.io/biocontainers/proteinortho", "aliases": {"proteinortho": "/usr/local/bin/proteinortho", "proteinortho2html.pl": "/usr/local/bin/proteinortho2html.pl", "proteinortho2tree.pl": "/usr/local/bin/proteinortho2tree.pl", "proteinortho2xml.pl": "/usr/local/bin/proteinortho2xml.pl", "proteinortho6.pl": "/usr/local/bin/proteinortho6.pl", "proteinortho_cleanupblastgraph": "/usr/local/bin/proteinortho_cleanupblastgraph", "proteinortho_clustering": "/usr/local/bin/proteinortho_clustering", "proteinortho_compareProteinorthoGraphs.pl": "/usr/local/bin/proteinortho_compareProteinorthoGraphs.pl", "proteinortho_do_mcl.pl": "/usr/local/bin/proteinortho_do_mcl.pl", "proteinortho_extract_from_graph.pl": "/usr/local/bin/proteinortho_extract_from_graph.pl", "proteinortho_ffadj_mcs.py": "/usr/local/bin/proteinortho_ffadj_mcs.py", "proteinortho_formatUsearch.pl": "/usr/local/bin/proteinortho_formatUsearch.pl", "proteinortho_grab_proteins.pl": "/usr/local/bin/proteinortho_grab_proteins.pl", "proteinortho_graphMinusRemovegraph": "/usr/local/bin/proteinortho_graphMinusRemovegraph", "proteinortho_history.pl": "/usr/local/bin/proteinortho_history.pl", "proteinortho_singletons.pl": "/usr/local/bin/proteinortho_singletons.pl", "proteinortho_summary.pl": "/usr/local/bin/proteinortho_summary.pl", "proteinortho_treeBuilderCore": "/usr/local/bin/proteinortho_treeBuilderCore", "diamond": "/usr/local/bin/diamond", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteinortho.
shpc-registry automated BioContainers addition for proteinortho
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteinortho
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteinortho:6.1.1--hedee03e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteinortho/6.1.1--hedee03e_0
$ module help quay.io/biocontainers/proteinortho/6.1.1--hedee03e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteinortho-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteinortho-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteinortho-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteinortho-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteinortho-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteinortho-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proteinortho

```bash
$ singularity exec <container> /usr/local/bin/proteinortho
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho2html.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho2html.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho2html.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho2html.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho2xml.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho2xml.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho2xml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho2xml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho6.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho6.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho6.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho6.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_cleanupblastgraph

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_cleanupblastgraph
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_cleanupblastgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_cleanupblastgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_clustering

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_clustering
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_compareProteinorthoGraphs.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_compareProteinorthoGraphs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_compareProteinorthoGraphs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_compareProteinorthoGraphs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_do_mcl.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_do_mcl.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_do_mcl.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_do_mcl.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_extract_from_graph.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_extract_from_graph.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_extract_from_graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_extract_from_graph.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_ffadj_mcs.py

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_ffadj_mcs.py
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_ffadj_mcs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_ffadj_mcs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_formatUsearch.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_formatUsearch.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_formatUsearch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_formatUsearch.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_grab_proteins.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_grab_proteins.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_grab_proteins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_grab_proteins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_graphMinusRemovegraph

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_graphMinusRemovegraph
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_graphMinusRemovegraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_graphMinusRemovegraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_history.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_history.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_history.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_history.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_singletons.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_singletons.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_singletons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_singletons.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_summary.pl

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_summary.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_summary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_summary.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinortho_treeBuilderCore

```bash
$ singularity exec <container> /usr/local/bin/proteinortho_treeBuilderCore
$ podman run --it --rm --entrypoint /usr/local/bin/proteinortho_treeBuilderCore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinortho_treeBuilderCore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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