---
layout: container
name:  "quay.io/biocontainers/traitar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/traitar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/traitar/container.yaml"
updated_at: "2025-08-24 03:28:06.214288"
latest: "3.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/traitar"
aliases:
 - "domtblout2gene_generic.py"
 - "heatmap.py"
 - "hmm2gff.py"
 - "hmmer2filtered_best.py"
 - "merge_preds.py"
 - "predict.py"
 - "traitar"
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
 - "1.1.2--py_0"
 - "3.0.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for traitar"
config: {"url": "https://biocontainers.pro/tools/traitar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for traitar", "latest": {"3.0.1--pyhdfd78af_0": "sha256:fc1c56c277012c9061ef19f43403415d852850402feb17bff8360489bb5be4c0"}, "tags": {"1.1.2--py_0": "sha256:fee1195a60b294ad745e393d269b33325e4bcdf461fd3501ef87464d5e720d30", "3.0.1--pyhdfd78af_0": "sha256:fc1c56c277012c9061ef19f43403415d852850402feb17bff8360489bb5be4c0"}, "docker": "quay.io/biocontainers/traitar", "aliases": {"domtblout2gene_generic.py": "/usr/local/bin/domtblout2gene_generic.py", "heatmap.py": "/usr/local/bin/heatmap.py", "hmm2gff.py": "/usr/local/bin/hmm2gff.py", "hmmer2filtered_best.py": "/usr/local/bin/hmmer2filtered_best.py", "merge_preds.py": "/usr/local/bin/merge_preds.py", "predict.py": "/usr/local/bin/predict.py", "traitar": "/usr/local/bin/traitar", "qhelpconverter": "/usr/local/bin/qhelpconverter", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen", "qscxmlc": "/usr/local/bin/qscxmlc", "qtattributionsscanner": "/usr/local/bin/qtattributionsscanner", "repc": "/usr/local/bin/repc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/traitar.
shpc-registry automated BioContainers addition for traitar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/traitar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/traitar:3.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/traitar/3.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/traitar/3.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### traitar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### traitar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### traitar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### traitar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### traitar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### traitar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### domtblout2gene_generic.py

```bash
$ singularity exec <container> /usr/local/bin/domtblout2gene_generic.py
$ podman run --it --rm --entrypoint /usr/local/bin/domtblout2gene_generic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/domtblout2gene_generic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heatmap.py

```bash
$ singularity exec <container> /usr/local/bin/heatmap.py
$ podman run --it --rm --entrypoint /usr/local/bin/heatmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/heatmap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm2gff.py

```bash
$ singularity exec <container> /usr/local/bin/hmm2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmer2filtered_best.py

```bash
$ singularity exec <container> /usr/local/bin/hmmer2filtered_best.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmmer2filtered_best.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmer2filtered_best.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_preds.py

```bash
$ singularity exec <container> /usr/local/bin/merge_preds.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_preds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_preds.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### predict.py

```bash
$ singularity exec <container> /usr/local/bin/predict.py
$ podman run --it --rm --entrypoint /usr/local/bin/predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### traitar

```bash
$ singularity exec <container> /usr/local/bin/traitar
$ podman run --it --rm --entrypoint /usr/local/bin/traitar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/traitar   -v ${PWD} -w ${PWD} <container> -c " $@"
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