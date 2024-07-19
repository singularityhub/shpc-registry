---
layout: container
name:  "quay.io/biocontainers/tb_variant_filter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tb_variant_filter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tb_variant_filter/container.yaml"
updated_at: "2024-07-19 03:19:51.424165"
latest: "0.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tb_variant_filter"
aliases:
 - "tb_bed_to_region_list"
 - "tb_region_list_to_bed"
 - "tb_variant_filter"
 - "xslt-config"
 - "xsltproc"
 - "chardetect"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3.5--pyhdfd78af_0"
 - "0.3.6--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for tb_variant_filter"
config: {"url": "https://biocontainers.pro/tools/tb_variant_filter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tb_variant_filter", "latest": {"0.4.0--pyhdfd78af_0": "sha256:e9e76f89b63a5d5c791a8a02ffd6a0711812c09b83c6863e8497932566d76346"}, "tags": {"0.3.5--pyhdfd78af_0": "sha256:fd3838fb07d741603b1f1900c25076e6cdf03fc1eaadd78542d3ef5308de579b", "0.3.6--pyhdfd78af_0": "sha256:90eed76b423feb818ddb6b3d32134d95512656e24a44c6aac8f4be5e867a39d9", "0.4.0--pyhdfd78af_0": "sha256:e9e76f89b63a5d5c791a8a02ffd6a0711812c09b83c6863e8497932566d76346"}, "docker": "quay.io/biocontainers/tb_variant_filter", "aliases": {"tb_bed_to_region_list": "/usr/local/bin/tb_bed_to_region_list", "tb_region_list_to_bed": "/usr/local/bin/tb_region_list_to_bed", "tb_variant_filter": "/usr/local/bin/tb_variant_filter", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "chardetect": "/usr/local/bin/chardetect", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tb_variant_filter.
shpc-registry automated BioContainers addition for tb_variant_filter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tb_variant_filter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tb_variant_filter:0.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tb_variant_filter/0.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/tb_variant_filter/0.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tb_variant_filter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tb_variant_filter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tb_variant_filter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tb_variant_filter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tb_variant_filter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tb_variant_filter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tb_bed_to_region_list

```bash
$ singularity exec <container> /usr/local/bin/tb_bed_to_region_list
$ podman run --it --rm --entrypoint /usr/local/bin/tb_bed_to_region_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tb_bed_to_region_list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tb_region_list_to_bed

```bash
$ singularity exec <container> /usr/local/bin/tb_region_list_to_bed
$ podman run --it --rm --entrypoint /usr/local/bin/tb_region_list_to_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tb_region_list_to_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tb_variant_filter

```bash
$ singularity exec <container> /usr/local/bin/tb_variant_filter
$ podman run --it --rm --entrypoint /usr/local/bin/tb_variant_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tb_variant_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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