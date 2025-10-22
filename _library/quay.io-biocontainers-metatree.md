---
layout: container
name:  "quay.io/biocontainers/metatree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metatree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metatree/container.yaml"
updated_at: "2025-10-22 03:59:16.623384"
latest: "0.0.1--py_0"
container_url: "https://biocontainers.pro/tools/metatree"
aliases:
 - "genometreetk"
 - "metatree"
 - "phylorank"
 - "FastTree-2.1.10.c"
 - "ete3"
 - "FastTreeMP"
 - "FastTree"
 - "compile-et.pl"
 - "fasttree"
 - "prerr.properties"
 - "sumlabels.py"
 - "sumtrees.py"
 - "qdistancefieldgenerator"
versions:
 - "0.0.1--py_0"
description: "shpc-registry automated BioContainers addition for metatree"
config: {"url": "https://biocontainers.pro/tools/metatree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metatree", "latest": {"0.0.1--py_0": "sha256:bd67bc970e530439c7254daaf1a81a98b0da0c2ed8585a6f45dd3121671e426d"}, "tags": {"0.0.1--py_0": "sha256:bd67bc970e530439c7254daaf1a81a98b0da0c2ed8585a6f45dd3121671e426d"}, "docker": "quay.io/biocontainers/metatree", "aliases": {"genometreetk": "/usr/local/bin/genometreetk", "metatree": "/usr/local/bin/metatree", "phylorank": "/usr/local/bin/phylorank", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "ete3": "/usr/local/bin/ete3", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "compile-et.pl": "/usr/local/bin/compile-et.pl", "fasttree": "/usr/local/bin/fasttree", "prerr.properties": "/usr/local/bin/prerr.properties", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metatree.
shpc-registry automated BioContainers addition for metatree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metatree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metatree:0.0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metatree/0.0.1--py_0
$ module help quay.io/biocontainers/metatree/0.0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metatree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metatree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metatree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metatree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metatree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metatree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genometreetk

```bash
$ singularity exec <container> /usr/local/bin/genometreetk
$ podman run --it --rm --entrypoint /usr/local/bin/genometreetk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometreetk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metatree

```bash
$ singularity exec <container> /usr/local/bin/metatree
$ podman run --it --rm --entrypoint /usr/local/bin/metatree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metatree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylorank

```bash
$ singularity exec <container> /usr/local/bin/phylorank
$ podman run --it --rm --entrypoint /usr/local/bin/phylorank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylorank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree-2.1.10.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree-2.1.10.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerr.properties

```bash
$ singularity exec <container> /usr/local/bin/prerr.properties
$ podman run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
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