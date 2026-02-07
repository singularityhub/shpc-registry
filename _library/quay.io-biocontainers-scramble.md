---
layout: container
name:  "quay.io/biocontainers/scramble"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scramble/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scramble/container.yaml"
updated_at: "2026-02-07 04:29:22.020424"
latest: "1.0.2--h031d066_1"
container_url: "https://biocontainers.pro/tools/scramble"
aliases:
 - "cluster_identifier"
 - "scramble.sh"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
 - "disambiguate-nucleotides"
versions:
 - "1.0.2--hec16e2b_0"
 - "1.0.2--h031d066_1"
description: "shpc-registry automated BioContainers addition for scramble"
config: {"url": "https://biocontainers.pro/tools/scramble", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scramble", "latest": {"1.0.2--h031d066_1": "sha256:f3fc2be687f810977dc5ddff83f6dbddb4d06d3998172f6d1115e4abaf377d93"}, "tags": {"1.0.2--hec16e2b_0": "sha256:68d1452fa2ca389373a89c02ea7a83880e9332e5f839fafcca733859e5d9c97f", "1.0.2--h031d066_1": "sha256:f3fc2be687f810977dc5ddff83f6dbddb4d06d3998172f6d1115e4abaf377d93"}, "docker": "quay.io/biocontainers/scramble", "aliases": {"cluster_identifier": "/usr/local/bin/cluster_identifier", "scramble.sh": "/usr/local/bin/scramble.sh", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scramble.
shpc-registry automated BioContainers addition for scramble
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scramble
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scramble:1.0.2--h031d066_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scramble/1.0.2--h031d066_1
$ module help quay.io/biocontainers/scramble/1.0.2--h031d066_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scramble-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scramble-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scramble-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scramble-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scramble-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scramble-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cluster_identifier

```bash
$ singularity exec <container> /usr/local/bin/cluster_identifier
$ podman run --it --rm --entrypoint /usr/local/bin/cluster_identifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster_identifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scramble.sh

```bash
$ singularity exec <container> /usr/local/bin/scramble.sh
$ podman run --it --rm --entrypoint /usr/local/bin/scramble.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scramble.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### disambiguate-nucleotides

```bash
$ singularity exec <container> /usr/local/bin/disambiguate-nucleotides
$ podman run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
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