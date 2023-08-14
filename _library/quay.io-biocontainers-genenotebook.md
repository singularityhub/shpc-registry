---
layout: container
name:  "quay.io/biocontainers/genenotebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genenotebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genenotebook/container.yaml"
updated_at: "2023-08-14 03:37:54.514403"
latest: "0.3.2--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/genenotebook"
aliases:
 - "genenotebook"
 - "install_compass"
 - "mongo"
 - "mongod"
 - "mongos"
 - "node"
 - "npm"
 - "npx"
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
 - "0.3.1--h9f5acd7_1"
 - "0.3.2--h9f5acd7_1"
 - "0.3.2--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for genenotebook"
config: {"url": "https://biocontainers.pro/tools/genenotebook", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genenotebook", "latest": {"0.3.2--h4ac6f70_2": "sha256:72dbe5395ab1000b34f9e8fd3f3b4ef35240c104ab49496889886a1e2a756d15"}, "tags": {"0.3.1--h9f5acd7_1": "sha256:a30f10d56d1312fe0385ff04c55967b7073e782d8b38ef204e6b954701b15c41", "0.3.2--h9f5acd7_1": "sha256:1c473e5447ab6b7f68af14002412fc5d3a2dc167008705707e31b90b1602fa91", "0.3.2--h4ac6f70_2": "sha256:72dbe5395ab1000b34f9e8fd3f3b4ef35240c104ab49496889886a1e2a756d15"}, "docker": "quay.io/biocontainers/genenotebook", "aliases": {"genenotebook": "/usr/local/bin/genenotebook", "install_compass": "/usr/local/bin/install_compass", "mongo": "/usr/local/bin/mongo", "mongod": "/usr/local/bin/mongod", "mongos": "/usr/local/bin/mongos", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genenotebook.
shpc-registry automated BioContainers addition for genenotebook
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genenotebook
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genenotebook:0.3.2--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genenotebook/0.3.2--h4ac6f70_2
$ module help quay.io/biocontainers/genenotebook/0.3.2--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genenotebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genenotebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genenotebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genenotebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genenotebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genenotebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genenotebook

```bash
$ singularity exec <container> /usr/local/bin/genenotebook
$ podman run --it --rm --entrypoint /usr/local/bin/genenotebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genenotebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_compass

```bash
$ singularity exec <container> /usr/local/bin/install_compass
$ podman run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongo

```bash
$ singularity exec <container> /usr/local/bin/mongo
$ podman run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongod

```bash
$ singularity exec <container> /usr/local/bin/mongod
$ podman run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongos

```bash
$ singularity exec <container> /usr/local/bin/mongos
$ podman run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
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