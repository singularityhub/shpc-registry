---
layout: container
name:  "quay.io/biocontainers/primedrpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primedrpa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primedrpa/container.yaml"
updated_at: "2025-09-11 05:02:22.306159"
latest: "1.0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/primedrpa"
aliases:
 - "PrimedRPA"
 - "clustalo"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
versions:
 - "1.0.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for primedrpa"
config: {"url": "https://biocontainers.pro/tools/primedrpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for primedrpa", "latest": {"1.0.3--pyhdfd78af_0": "sha256:7546facca1169d3c6547caea747fe429e622255cd635fe35d402fd4e9471387a"}, "tags": {"1.0.3--pyhdfd78af_0": "sha256:7546facca1169d3c6547caea747fe429e622255cd635fe35d402fd4e9471387a"}, "docker": "quay.io/biocontainers/primedrpa", "aliases": {"PrimedRPA": "/usr/local/bin/PrimedRPA", "clustalo": "/usr/local/bin/clustalo", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primedrpa.
shpc-registry automated BioContainers addition for primedrpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primedrpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primedrpa:1.0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primedrpa/1.0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/primedrpa/1.0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primedrpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primedrpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primedrpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primedrpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primedrpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primedrpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PrimedRPA

```bash
$ singularity exec <container> /usr/local/bin/PrimedRPA
$ podman run --it --rm --entrypoint /usr/local/bin/PrimedRPA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrimedRPA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xml

```bash
$ singularity exec <container> /usr/local/bin/csv2xml
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
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