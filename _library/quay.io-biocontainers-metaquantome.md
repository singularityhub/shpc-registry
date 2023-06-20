---
layout: container
name:  "quay.io/biocontainers/metaquantome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaquantome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaquantome/container.yaml"
updated_at: "2023-06-20 02:54:32.640484"
latest: "2.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metaquantome"
aliases:
 - "fetch_associations.py"
 - "find_enrichment.py"
 - "map_to_slim.py"
 - "metaquantome"
 - "plot_go_term.py"
 - "write_hierarchy.py"
 - "vba_extract.py"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "ete3"
 - "cxpm"
 - "sxpm"
 - "delaunay"
versions:
 - "2.0.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for metaquantome"
config: {"url": "https://biocontainers.pro/tools/metaquantome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaquantome", "latest": {"2.0.2--pyhdfd78af_0": "sha256:63ecc9b2be8ab451aae2092d47d03e5f6e2d9217fa920e7bf488b1a6f1cb4f9e"}, "tags": {"2.0.2--pyhdfd78af_0": "sha256:63ecc9b2be8ab451aae2092d47d03e5f6e2d9217fa920e7bf488b1a6f1cb4f9e"}, "docker": "quay.io/biocontainers/metaquantome", "aliases": {"fetch_associations.py": "/usr/local/bin/fetch_associations.py", "find_enrichment.py": "/usr/local/bin/find_enrichment.py", "map_to_slim.py": "/usr/local/bin/map_to_slim.py", "metaquantome": "/usr/local/bin/metaquantome", "plot_go_term.py": "/usr/local/bin/plot_go_term.py", "write_hierarchy.py": "/usr/local/bin/write_hierarchy.py", "vba_extract.py": "/usr/local/bin/vba_extract.py", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "ete3": "/usr/local/bin/ete3", "cxpm": "/usr/local/bin/cxpm", "sxpm": "/usr/local/bin/sxpm", "delaunay": "/usr/local/bin/delaunay"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaquantome.
shpc-registry automated BioContainers addition for metaquantome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaquantome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaquantome:2.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaquantome/2.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/metaquantome/2.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaquantome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaquantome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaquantome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaquantome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaquantome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaquantome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fetch_associations.py

```bash
$ singularity exec <container> /usr/local/bin/fetch_associations.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_associations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_enrichment.py

```bash
$ singularity exec <container> /usr/local/bin/find_enrichment.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_enrichment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_to_slim.py

```bash
$ singularity exec <container> /usr/local/bin/map_to_slim.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_to_slim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaquantome

```bash
$ singularity exec <container> /usr/local/bin/metaquantome
$ podman run --it --rm --entrypoint /usr/local/bin/metaquantome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquantome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_go_term.py

```bash
$ singularity exec <container> /usr/local/bin/plot_go_term.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_go_term.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### write_hierarchy.py

```bash
$ singularity exec <container> /usr/local/bin/write_hierarchy.py
$ podman run --it --rm --entrypoint /usr/local/bin/write_hierarchy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/write_hierarchy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
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