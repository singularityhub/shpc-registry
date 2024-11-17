---
layout: container
name:  "quay.io/biocontainers/vase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vase/container.yaml"
updated_at: "2024-11-17 03:09:34.200230"
latest: "0.5.1--pyh086e186_0"
container_url: "https://biocontainers.pro/tools/vase"
aliases:
 - "burden_test_vase"
 - "coordinates_from_genes"
 - "filter_gts"
 - "phase_by_transmission"
 - "remove_info_fields"
 - "vase"
 - "vase_reporter"
 - "xml2-config.bak"
 - "vba_extract.py"
 - "natsort"
 - "normalizer"
 - "xslt-config"
 - "xsltproc"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.5.1--pyh086e186_0"
description: "singularity registry hpc automated addition for vase"
config: {"url": "https://biocontainers.pro/tools/vase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vase", "latest": {"0.5.1--pyh086e186_0": "sha256:06d6f9114e3e3b367e71e090b2c92288efeed42c5377c59745fc42136a21b527"}, "tags": {"0.5.1--pyh086e186_0": "sha256:06d6f9114e3e3b367e71e090b2c92288efeed42c5377c59745fc42136a21b527"}, "docker": "quay.io/biocontainers/vase", "aliases": {"burden_test_vase": "/usr/local/bin/burden_test_vase", "coordinates_from_genes": "/usr/local/bin/coordinates_from_genes", "filter_gts": "/usr/local/bin/filter_gts", "phase_by_transmission": "/usr/local/bin/phase_by_transmission", "remove_info_fields": "/usr/local/bin/remove_info_fields", "vase": "/usr/local/bin/vase", "vase_reporter": "/usr/local/bin/vase_reporter", "xml2-config.bak": "/usr/local/bin/xml2-config.bak", "vba_extract.py": "/usr/local/bin/vba_extract.py", "natsort": "/usr/local/bin/natsort", "normalizer": "/usr/local/bin/normalizer", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vase.
singularity registry hpc automated addition for vase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vase:0.5.1--pyh086e186_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vase/0.5.1--pyh086e186_0
$ module help quay.io/biocontainers/vase/0.5.1--pyh086e186_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### burden_test_vase

```bash
$ singularity exec <container> /usr/local/bin/burden_test_vase
$ podman run --it --rm --entrypoint /usr/local/bin/burden_test_vase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/burden_test_vase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coordinates_from_genes

```bash
$ singularity exec <container> /usr/local/bin/coordinates_from_genes
$ podman run --it --rm --entrypoint /usr/local/bin/coordinates_from_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coordinates_from_genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_gts

```bash
$ singularity exec <container> /usr/local/bin/filter_gts
$ podman run --it --rm --entrypoint /usr/local/bin/filter_gts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_gts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phase_by_transmission

```bash
$ singularity exec <container> /usr/local/bin/phase_by_transmission
$ podman run --it --rm --entrypoint /usr/local/bin/phase_by_transmission   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phase_by_transmission   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_info_fields

```bash
$ singularity exec <container> /usr/local/bin/remove_info_fields
$ podman run --it --rm --entrypoint /usr/local/bin/remove_info_fields   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_info_fields   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vase

```bash
$ singularity exec <container> /usr/local/bin/vase
$ podman run --it --rm --entrypoint /usr/local/bin/vase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vase_reporter

```bash
$ singularity exec <container> /usr/local/bin/vase_reporter
$ podman run --it --rm --entrypoint /usr/local/bin/vase_reporter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vase_reporter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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