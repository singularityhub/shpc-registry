---
layout: container
name:  "quay.io/biocontainers/diapysef"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/diapysef/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/diapysef/container.yaml"
updated_at: "2023-07-15 03:22:06.756246"
latest: "1.0.10--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/diapysef"
aliases:
 - "annotate_mq_ionmobility.py"
 - "convertTDFtoMzML.py"
 - "create_library.py"
 - "get_dia_windows.py"
 - "high_precision_irt.py"
 - "plot_dia_windows.py"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
versions:
 - "0.3.5--pyh864c0ab_1"
 - "1.0.10--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for diapysef"
config: {"url": "https://biocontainers.pro/tools/diapysef", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for diapysef", "latest": {"1.0.10--pyh7cba7a3_0": "sha256:5761aaabcdd2e6cc9b59f289c522977fdc5fa4ed1f2d3febe60e966a63e2cad3"}, "tags": {"0.3.5--pyh864c0ab_1": "sha256:ce948216dba925aa2849e1f548aa2c97e6604fa496599b41b25517b4b2b3e712", "1.0.10--pyh7cba7a3_0": "sha256:5761aaabcdd2e6cc9b59f289c522977fdc5fa4ed1f2d3febe60e966a63e2cad3"}, "docker": "quay.io/biocontainers/diapysef", "aliases": {"annotate_mq_ionmobility.py": "/usr/local/bin/annotate_mq_ionmobility.py", "convertTDFtoMzML.py": "/usr/local/bin/convertTDFtoMzML.py", "create_library.py": "/usr/local/bin/create_library.py", "get_dia_windows.py": "/usr/local/bin/get_dia_windows.py", "high_precision_irt.py": "/usr/local/bin/high_precision_irt.py", "plot_dia_windows.py": "/usr/local/bin/plot_dia_windows.py", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/diapysef.
shpc-registry automated BioContainers addition for diapysef
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/diapysef
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/diapysef:1.0.10--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/diapysef/1.0.10--pyh7cba7a3_0
$ module help quay.io/biocontainers/diapysef/1.0.10--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### diapysef-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### diapysef-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### diapysef-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### diapysef-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### diapysef-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### diapysef-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate_mq_ionmobility.py

```bash
$ singularity exec <container> /usr/local/bin/annotate_mq_ionmobility.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_mq_ionmobility.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_mq_ionmobility.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertTDFtoMzML.py

```bash
$ singularity exec <container> /usr/local/bin/convertTDFtoMzML.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertTDFtoMzML.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertTDFtoMzML.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_library.py

```bash
$ singularity exec <container> /usr/local/bin/create_library.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_library.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_library.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_dia_windows.py

```bash
$ singularity exec <container> /usr/local/bin/get_dia_windows.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_dia_windows.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_dia_windows.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### high_precision_irt.py

```bash
$ singularity exec <container> /usr/local/bin/high_precision_irt.py
$ podman run --it --rm --entrypoint /usr/local/bin/high_precision_irt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/high_precision_irt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_dia_windows.py

```bash
$ singularity exec <container> /usr/local/bin/plot_dia_windows.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_dia_windows.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_dia_windows.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /usr/local/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /usr/local/bin/DOMCount
$ podman run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /usr/local/bin/DOMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /usr/local/bin/EnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /usr/local/bin/MemParse
$ podman run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /usr/local/bin/PParse
$ podman run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /usr/local/bin/PSVIWriter
$ podman run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
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