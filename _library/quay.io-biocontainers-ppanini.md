---
layout: container
name:  "quay.io/biocontainers/ppanini"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ppanini/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ppanini/container.yaml"
updated_at: "2024-03-30 02:57:54.316332"
latest: "0.7.4--py_0"
container_url: "https://biocontainers.pro/tools/ppanini"
aliases:
 - "ppanini"
 - "ppanini_barplot"
 - "ppanini_cluster2genes"
 - "ppanini_fasta_select"
 - "ppanini_gene_caller"
 - "ppanini_infer_gene"
 - "ppanini_join_tables"
 - "ppanini_press"
 - "ppanini_rename_contigs"
 - "ppanini_rev_uniref_mapper"
 - "ppanini_rocplot"
 - "ppanini_scatterplot"
 - "ppanini_test"
 - "qhelpconverter"
 - "f2py2"
 - "f2py2.7"
 - "qwebengine_convert_dict"
 - "canbusutil"
 - "qgltf"
 - "qmlcachegen"
 - "qscxmlc"
 - "qtattributionsscanner"
 - "repc"
versions:
 - "0.7.4--py_0"
description: "shpc-registry automated BioContainers addition for ppanini"
config: {"url": "https://biocontainers.pro/tools/ppanini", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ppanini", "latest": {"0.7.4--py_0": "sha256:73a5656fe0b2c7203454ae729052cf0154f6c17f10086770c4d3413aa8ac3976"}, "tags": {"0.7.4--py_0": "sha256:73a5656fe0b2c7203454ae729052cf0154f6c17f10086770c4d3413aa8ac3976"}, "docker": "quay.io/biocontainers/ppanini", "aliases": {"ppanini": "/usr/local/bin/ppanini", "ppanini_barplot": "/usr/local/bin/ppanini_barplot", "ppanini_cluster2genes": "/usr/local/bin/ppanini_cluster2genes", "ppanini_fasta_select": "/usr/local/bin/ppanini_fasta_select", "ppanini_gene_caller": "/usr/local/bin/ppanini_gene_caller", "ppanini_infer_gene": "/usr/local/bin/ppanini_infer_gene", "ppanini_join_tables": "/usr/local/bin/ppanini_join_tables", "ppanini_press": "/usr/local/bin/ppanini_press", "ppanini_rename_contigs": "/usr/local/bin/ppanini_rename_contigs", "ppanini_rev_uniref_mapper": "/usr/local/bin/ppanini_rev_uniref_mapper", "ppanini_rocplot": "/usr/local/bin/ppanini_rocplot", "ppanini_scatterplot": "/usr/local/bin/ppanini_scatterplot", "ppanini_test": "/usr/local/bin/ppanini_test", "qhelpconverter": "/usr/local/bin/qhelpconverter", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen", "qscxmlc": "/usr/local/bin/qscxmlc", "qtattributionsscanner": "/usr/local/bin/qtattributionsscanner", "repc": "/usr/local/bin/repc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ppanini.
shpc-registry automated BioContainers addition for ppanini
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ppanini
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ppanini:0.7.4--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ppanini/0.7.4--py_0
$ module help quay.io/biocontainers/ppanini/0.7.4--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ppanini-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ppanini-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ppanini-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ppanini-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ppanini-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ppanini-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ppanini

```bash
$ singularity exec <container> /usr/local/bin/ppanini
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_barplot

```bash
$ singularity exec <container> /usr/local/bin/ppanini_barplot
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_barplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_barplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_cluster2genes

```bash
$ singularity exec <container> /usr/local/bin/ppanini_cluster2genes
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_cluster2genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_cluster2genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_fasta_select

```bash
$ singularity exec <container> /usr/local/bin/ppanini_fasta_select
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_fasta_select   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_fasta_select   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_gene_caller

```bash
$ singularity exec <container> /usr/local/bin/ppanini_gene_caller
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_gene_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_gene_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_infer_gene

```bash
$ singularity exec <container> /usr/local/bin/ppanini_infer_gene
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_infer_gene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_infer_gene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_join_tables

```bash
$ singularity exec <container> /usr/local/bin/ppanini_join_tables
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_join_tables   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_join_tables   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_press

```bash
$ singularity exec <container> /usr/local/bin/ppanini_press
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_press   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_press   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_rename_contigs

```bash
$ singularity exec <container> /usr/local/bin/ppanini_rename_contigs
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_rename_contigs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_rename_contigs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_rev_uniref_mapper

```bash
$ singularity exec <container> /usr/local/bin/ppanini_rev_uniref_mapper
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_rev_uniref_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_rev_uniref_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_rocplot

```bash
$ singularity exec <container> /usr/local/bin/ppanini_rocplot
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_rocplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_rocplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_scatterplot

```bash
$ singularity exec <container> /usr/local/bin/ppanini_scatterplot
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_scatterplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_scatterplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanini_test

```bash
$ singularity exec <container> /usr/local/bin/ppanini_test
$ podman run --it --rm --entrypoint /usr/local/bin/ppanini_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanini_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qgltf

```bash
$ singularity exec <container> /usr/local/bin/qgltf
$ podman run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlcachegen

```bash
$ singularity exec <container> /usr/local/bin/qmlcachegen
$ podman run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qscxmlc

```bash
$ singularity exec <container> /usr/local/bin/qscxmlc
$ podman run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtattributionsscanner

```bash
$ singularity exec <container> /usr/local/bin/qtattributionsscanner
$ podman run --it --rm --entrypoint /usr/local/bin/qtattributionsscanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtattributionsscanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repc

```bash
$ singularity exec <container> /usr/local/bin/repc
$ podman run --it --rm --entrypoint /usr/local/bin/repc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repc   -v ${PWD} -w ${PWD} <container> -c " $@"
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